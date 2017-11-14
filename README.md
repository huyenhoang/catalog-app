# Gig Economy Catalog App

This application written using the Flask framework allows users to securely sign-in with OAuth 2.0 and add information about the gig economy platforms they are participating in. Authentication ensures that users cannot modify content that they themselves did not input into the app. New users can explore categories and find gig economy platforms that suits them from user generated content. The data is accessible via JSON API endpoints.

# Getting Started

## Prerequisites

Make sure to have the following installed:
1. Python 2.7.0 (at least)
2. VirtualBox
3. Vagrant

## Installations

### 1. Python

#### On Mac
To determine if you have Python 2.7, open the Terminal application, type the following, and press Return:

`python -V`

This command will report the version of Python:

`Python 2.7.9`

Any version between 2.7.0 and 2.7.10 is fine.

#### On Windows 7

To get to the command line, open the Windows menu and type “command” in the search bar. Select Command Prompt from the search results. In the Command Prompt window, type the following and press Enter.

`python`

If Python is installed and in your path, then this command will run python.exe and show you the version number.

`Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.`

Otherwise, you will see:

`'python' is not recognized as an internal or external command, operable program or batch file.`

#### On Linux

Open a shell and type

`which python`

If Python is installed, you will get back its location, which may or may not include the version number. If the location does not include a version number, then ask for it:

`python -V`

This command returns the version

`Python 2.7.9`

### 2. VirtualBox
Can be downloaded here: (https://www.virtualbox.org/wiki/Downloads)

### 3. Vagrant
Download Vagrant here: https://www.vagrantup.com/downloads.html

To check if you've successfully installed, vagrant, type:
`vagrant --version`

The vagrant configuration file, named vagrantfile, can be forked from this Udacity respository: https://github.com/udacity/fullstack-nanodegree-vm

To launch the virtual VM, change directory to where the vagrantfile is and use the following command:

`vagrant up`

To log into the virtual machine:
`vagrant ssh`

Before loading the data, `cd` into the `vagrant` directory.

## Running the Python program

From the command line, type `python application.py` to run the module.

Visit localhost:8000 or 5000 (depending on the vagrantfile configuration) to view the application.
