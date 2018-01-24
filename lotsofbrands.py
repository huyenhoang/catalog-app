# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from category_db_setup import Categories, Base, Brands, User

engine = create_engine('sqlite:///categorywithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Brands for Rideshare Category
category1 = Categories(user_id=1, id=1,
        image="https://images.unsplash.com/photo-1482029255085-35a4a48b7084?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e39f4577aaa96dc4c2806e7d890a656e&auto=format&fit=crop&w=1489&q=80",
        category="Rideshare")

session.add(category1)
session.commit()

#uber
brand1 = Brands(user_id=1, name="Uber", location="San Francisco, CA",
       description="Uber is a mobile app connecting passengers with drivers for hire.", website="Uber.com",
       industry=category1)

session.add(brand1)
session.commit()

#lyft
brand2 = Brands(user_id=1, name="Lyft", location="San Francisco, CA",
       description="Lyft is reconnecting people and communities through better transportation.", website="Lyft.com",
       industry=category1)

session.add(brand2)
session.commit()

#GetAround
brand3 = Brands(user_id=1, name="GetAround", location="San Francisco, CA",
       description="Getaround is a mobile application and a peer-to-peer car sharing marketplace that enables car owners to rent out their cars.", website="getaround.com",
       industry=category1)

session.add(brand3)
session.commit()

# Brands for Food Delivery Category
category2 = Categories(user_id=1, id=2,
        image="https://images.unsplash.com/photo-1428660386617-8d277e7deaf2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=d85cfa1d6d003f6e82f46bc5a394a592&auto=format&fit=crop&w=1567&q=80",
        category="Food Delivery")

session.add(category2)
session.commit()

#Postmates
brand4 = Brands(user_id=1, name="Postmates", location="San Francisco, CA",
       description="Postmates powers local, on-demand logistics focused on fast deliveries from any type of merchant at scale.", website="Postmates.com",
       industry=category2)

session.add(brand4)
session.commit()

#Caviar
brand5 = Brands(user_id=1, name="Caviar", location="San Francisco, CA",
       description="Caviar is a delivery solution for consumers to order food from local eateries with the ability to live-track the order on a map.", website="TryCaviar.com",
       industry=category2)

session.add(brand5)
session.commit()

#GrubHub
brand6 = Brands(user_id=1, name="GrubHub", location="Chicago, IL",
       description="GrubHub allows users to find and order food from restaurants in their vicinity that deliver or offer pickup, via an app and a website.", website="GrubHub.com",
       industry=category2)

session.add(brand6)
session.commit()

#Favor
brand7 = Brands(user_id=1, name="Favor", location="Austin, TX",
       description="Favor enables small businesses to provide its customers with local delivery services. Truly Personal Service. Once you've placed an order you'll be assigned your own personal delivery assistant.", website="favordelivery.com",
       industry=category2)

session.add(brand7)
session.commit()

#Instacart
brand8 = Brands(user_id=1, name="Instacart", location="San Francisco, CA",
       description="Instacart is a same-day grocery delivery company delivering groceries and home essentials from a variety of local stores.", website="Instacart.com",
       industry=category2)

session.add(brand8)
session.commit()

#Deliveroo
brand9 = Brands(user_id=1, name="Deliveroo", location="London, UK",
       description="Deliveroo is a technology company that focuses on marketing, selling, and delivering restaurant meals to the household or office.", website="deliveroo.co.uk",
       industry=category2)

session.add(brand9)
session.commit()

#DoorDash
brand10 = Brands(user_id=1, name="DoorDash", location="San Francisco, CA",
       description="DoorDash enables small businesses to provide its customers with local delivery services.", website="DoorDash.com",
       industry=category2)

session.add(brand10)
session.commit()

# Brands for Travel Category
category3 = Categories(user_id=1, id=3,
        image="https://images.unsplash.com/photo-1484544808355-8ec84e534d75?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=fc1407c2a550b0ebf3def8b81fa7b4a2&auto=format&fit=crop&w=1366&q=80",
        category="Travel")

session.add(category3)
session.commit()

#Airbnb
brand11 = Brands(user_id=1, name="Airbnb", location="San Francisco, CA",
       description="Airbnb is an online community marketplace for people to list, discover, and book accommodations around the world.", website="Airbnb.com",
       industry=category3)

session.add(brand11)
session.commit()

#CouchSurfing
brand12 = Brands(user_id=1, name="CouchSurfing", location="San Francisco, CA",
       description="Couchsurfing is a travel community connecting a network of travelers, adventure seekers, and lifelong learners to share their experiences.", website="Couchsurfing.com",
       industry=category3)

session.add(brand12)
session.commit()

#HoneAway
brand13 = Brands(user_id=1, name="HomeAway", location="Austin, TX",
       description="HomeAway offers a platform in which travelers can browse and book vacation homes, and rental owners can advertise and manage bookings.", website="HomeAway.com",
       industry=category3)

session.add(brand13)
session.commit()

# Brands for Home Services Category
category4 = Categories(user_id=1, id=4,
        image="https://images.unsplash.com/photo-1504148455328-c376907d081c?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8aa0df958e322abceb9b1ac178669cae&auto=format&fit=crop&w=1443&q=80",
        category="Home Services")

session.add(category4)
session.commit()

#TaskRabbit
brand14 = Brands(user_id=1, name="TaskRabbit", location="San Francisco, CA",
       description="TaskRabbit is an app that allows users to get help with their everyday chores such as cleaning, delivery, moving, and handyman services.", website="TaskRabbit.com",
       industry=category4)

session.add(brand14)
session.commit()

#HomeJoy
brand15 = Brands(user_id=1, name="HomeJoy", location="San Francisco, CA",
       description="Homejoy is an online platform connecting professional cleaners with clients for $20 per hour.", website="HomeJoy.com",
       industry=category4)

session.add(brand15)
session.commit()

#Handy
brand16 = Brands(user_id=1, name="Handy", location="New York City, NY",
       description="Handy, formerly Handybook, is an app through which users can book cleaners, plumbers, handymen, and other household service providers.", website="handy.com",
       industry=category4)

session.add(brand16)
session.commit()

# Brands for Pet Care Category
category5 = Categories(user_id=1, id=5,
        image="https://images.unsplash.com/photo-1504803542671-cb92eb06a148?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=0c453a62d33c0c3a2b43fcb44152504f&auto=format&fit=crop&w=1350&q=80",
        category="Pet Care")

session.add(category5)
session.commit()

#Rover
brand17 = Brands(user_id=1, name="Rover", location="Seattle, WA",
       description="Rover is the largest network of loving and trustworthy pet sitters and dog walkers.", website="Rover.com",
       industry=category5)

session.add(brand17)
session.commit()

#Wag
brand18 = Brands(user_id=1, name="Wag", location="San Francisco, CA",
       description="Wag is a mobile application used to instantly find trusted and certified dog walkers.", website="Wagwalking.com",
       industry=category5)

session.add(brand18)
session.commit()

# Brands for Health Category
category6 = Categories(user_id=1, id=6,
        image="https://images.unsplash.com/photo-1434494878577-86c23bcb06b9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=d95859639b5694086008907139a72294&auto=format&fit=crop&w=1350&q=80",
        category="Health")

session.add(category6)
session.commit()

#Zeel
brand19 = Brands(user_id=1, name="Zeel", location="New York, CA",
       description="Zeel delivers on-demand massage from vetted therapists.", website="zeel.com",
       industry=category6)

session.add(brand19)
session.commit()

#Soothe
brand20 = Brands(user_id=1, name="Soothe", location="Los Angeles, CA",
       description="Soothe delivers world-class massages to your door in as little as 1 hour.", website="soothe.com",
       industry=category6)

session.add(brand20)
session.commit()

# Brands for Writing Category
category7 = Categories(user_id=1, id=7,
        image="https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=349f0586d07c10fdf29da504276b5407&auto=format&fit=crop&w=1350&q=80",
        category="Writing")

session.add(category7)
session.commit()

#blogmutt
brand21 = Brands(user_id=1, name="BlogMutt", location="Boulder, CO",
       description="No time? No writers? No blog posts? No problem. We are the simple, straightforward way to original blog content for your business or agency.", website="blogmutt.com",
       industry=category7)

session.add(brand21)
session.commit()

#iwriter
brand22 = Brands(user_id=1, name="iWriter", location="Carmel, IN",
       description="iWriter is a marketplace to outsource your business' content writing needs.", website="iwriter.com",
       industry=category7)

session.add(brand22)
session.commit()

# Brands for Programming Category
category8 = Categories(user_id=1, id=8,
        image="https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=a00dd14dd25d32b799b8e6e0270fd535&auto=format&fit=crop&w=1352&q=80",
        category="Programming")

session.add(category8)
session.commit()

#UpWork
brand23 = Brands(user_id=1, name="UpWork", location="San Francisco, CA",
       description="Upwork, formerly Elance-oDesk, is a global freelancing platform where businesses and independent professionals connect and collaborate remotely.", website="upwork.com",
       industry=category8)

session.add(brand23)
session.commit()

#PeoplePerHour
brand24 = Brands(user_id=1, name="PeoplePerHour", location="London, UK",
       description="PH is a community of talent available to work for you remotely, online, at a click of a button.", website="PeoplePerHour.com",
       industry=category8)

session.add(brand24)
session.commit()


print "added brands to categories!"
