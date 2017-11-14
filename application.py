from flask import Flask, render_template, redirect
from flask import url_for, request, flash, jsonify
from flask import make_response
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from category_db_setup import Categories, Base, Brands, User
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import random
import string
import httplib2
import json
import requests


app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Gig Economy Catalog App"
# Create session, connectwith database

engine = create_engine('sqlite:///categorywithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Check state token if valid
    if request.args.get('state') != login_sessions['state']:
        response = make_response(json.dumps('Invalid state token.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Get authorization
    code = request.data
    try:
        # turn authorization code into credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmassage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps(
            'Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # check that the access token is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # if there was an error in access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    # verify that the access token is used for intended user
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # verify that the access token is valid for this app
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's"), 401)
        print "Token's client ID does not match app's client ID."
        response.headers['Content-Type'] = 'application/json'
        return response
    # check to see if user is already logged in
    stored_credentials = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    # store access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/usrinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data["name"]
    login_session['picture'] = data["picture"]
    login_session['email'] = data["email"]

    # see if user exists, if it doesn't it doesn't make one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += 'img src="'
    output += login_session['picture']
    output += ' " style="width: 300px; height: 300px; border-radius: 150px; -webskit-border-radius: 150px;-moz-border-radius: 150px;">'
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# disconnect - revoke a current user's token and reset their login_session.

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# Login with facebook


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
    return response
    access_token = request.data
    app_id = json.loads(open('fb_client_secrets.json'), 'r'())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    userinfo_url = "http://graph.facebook.com/v2.2/me"
    token = result.split("&")[0]
    url = 'https://graph.facebook.com/v2.8/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    result - h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_sessionp['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

# get user pic
    url = 'https://graph.facebook/v2.2/me/picture?%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)
    login_session['picture'] = data["data"]["url"]

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += 'img src="'
    output += login_session['picture']
    output += ' " style="width: 300px; height: 300px; border-radius: 150px; -webskit-border-radius: 150px;-moz-border-radius: 150px;">'
    flash("you are now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    url = 'https://graph.facebook.com/%s/permissions' % facebook_id
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['user_id']
    del login_session['facebook_id']
    return "you have been logged out"


@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['credentials']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showRestaurants'))
    else:
        flash("You were not logged in to begin with!")
        redirect(url_for('showCategories'))

# API Endpoints


@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Categories).all()
    return jsonify(Categories=[cat.serialize for cat in categories])


@app.route('/categories/<int:category_id>/brands/JSON')
def brandsJSON(category_id):
    category = session.query(Categories).filter_by(id=category_id).one()
    brands = session.query(Brands).filter_by(category_id=category_id).all()
    return jsonify(Brands=[inc.serialize for inc in brands])


@app.route('/categories/<int:category_id>/brands/<int:brand_id>/JSON')
def brandDataJSON(category_id, brand_id):
    brand = session.query(Brands).filter_by(id=brand_id).one()
    return jsonify(Info=brand.serialize)

# Show all categories


@app.route('/')
@app.route('/categories/')
def showCategories():
    category = session.query(Categories).order_by(Categories.category)
    if 'username' not in login_session:
        return render_template('publiccategory.html', category=category)
    else:
        return render_template('category.html', category=category)

# Add new a category


@app.route('/categories/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCategory = Categories(category=request.form['name'], user_id=login_session['user_id'])
        session.add(newCategory)
        flash('New category %s successfully added to list' % newCategory.category)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')

# Edit a category


@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedCategory = session.query(Categories).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.category = request.form['name']
            flash('This category was successfully edited: %s' % editedCategory.category)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)

# Delete a category


@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(Categories).filter_by(id=category_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('Sorry but you are not authorized to delete this category.');}</script>/body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('Category %s was successfully deleted' % categoryToDelete.category)
        session.commit()
        return redirect(url_for('showCategories', category_id=category_id))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)

# Show individual category's brands (previously GigEconomy)


@app.route('/categories/<int:category_id>/')
@app.route('/categories/<int:category_id>/brands/')
def showBrands(category_id):
    category = session.query(Categories).filter_by(id=category_id).one()
    owner = getUserInfo(category.user_id)
    brands = session.query(Brands).filter_by(category_id=category_id)
    if 'username' not in login_session or owner.id != login_session['user_id']:
        return render_template('publicbrands.html', brands=brands, category=category, owner=owner)
    else:
        return render_template('brands.html', category=category, brands=brands, owner=owner)

# Add a new brand


@app.route('/categories/<int:category_id>/brands/new/', methods=['GET', 'POST'])
def newBrand(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newBrand = Brands(name=request.form['name'], location=request.form['location'], description=request.form['description'], website=request.form['website'], category_id=category_id, user_id=login_session['user_id'])
        session.add(newBrand)
        session.commit()
        flash("A new brand has been added!")
        return redirect(url_for('showBrands', category_id=category_id))
    else:
        return render_template('newBrand.html', category_id=category_id)

# Edit a brand


@app.route('/categories/<int:category_id>/brands/<int:brand_id>/edit/', methods=['GET', 'POST'])
def editBrand(category_id, brand_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedBrand = session.query(Brands).filter_by(id=brand_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedBrand.name = request.form['name']
        if request.form['location']:
            editedBrand.location = request.form['location']
        if request.form['description']:
            editedBrand.description = request.form['description']
        if request.form['website']:
            editedBrand.website = request.form['website']
        session.add(editedBrand)
        session.commit()
        flash("This brand has been edited!")
        return redirect(url_for('showBrands', category_id=category_id))
    else:
        return render_template('editBrand.html', category_id=category_id, brand_id=brand_id, inc=editedBrand)

# Delete a brand


@app.route('/categories/<int:category_id>/brands/<int:brand_id>/delete/', methods=['GET', 'POST'])
def deleteBrand(category_id, brand_id):
    if 'username' not in login_session:
        return redirect('/login')
    deletedBrand = session.query(Brands).filter_by(id=brand_id).one()
    if request.method == 'POST':
        if request.form['name']:
            deletedBrand.name = request.form['name']
        session.add(deletedBrand)
        session.commit()
        flash("This brand has been deleted!")
        return redirect(url_for('showBrands', category_id=category_id))
    else:
        return render_template('deleteBrand.html', category_id=category_id, brand_id=brand_id, inc=deletedBrand)

# for users


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def createUser(login_session):
    newUser = User(name=login-session['username'], email=login_session['email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
