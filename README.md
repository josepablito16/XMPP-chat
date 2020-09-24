# XMPP-chat

## Table of contents
* [Project description](#project-description)
* [Features](#features)
* [Installation](#installation)
* [Important files](#important-files)
* [Util references](#sleekxmpp-references)
* [How to use?](#how-to-use?)
* [Credits](#credits)

## Project description
This is a client with a clean and user-friendly console interface. The XMPP protocol is used with the help of the Python SleekXMPP library. To make an interface friendly, ANSI escape code was used to modify the terminal.

## Features
This XMPP client can interact with the server with:
* Create Account
*	log in
*	show all users on server
*	Show all users of the logged in account
*	Chat 1-1
*	Change presence message and status
*	Show notifications
*	Delete account

General Features
* Clean and friendly console interface

## Installation

```bash
# Clone this repository
$ git clone https://github.com/josepablito16/XMPP-chat.git

# Go into the repository
$ cd XMPP-chat

# Create a python virtual env
$ virtualenv env

# Activate the virtual environment Windows
$ cd env\Scripts\
$ activate.bat

# Activate the virtual environment Linux
$ source env/bin/activate

# Install the requirements packages
$ cd ../..
$ pip install -r requirements.txt
```

## Important files
* `MainClient.py`: terminal interface logic
* `Menus.py` : graphical console interaction
* `client.py`: all code related to the XMPP client

## SleekXMPP references 
[SleekXMPP Documentation](https://sleekxmpp.readthedocs.io/en/latest/index.html)
[SleekXMPP Wiki](https://github.com/fritzy/SleekXMPP/wiki)

## How to use?
```bash
# In the root folder of the repository: 
$ python3 MainClient.py
```
Then select the option 1 if you have already an account or 2 to create one. Finally, be free to select the desired options 

**Note:**
If you are in one chat and you want to return to the main menu type `exit()` and press Enter. 

Enjoy!

## Credits
José Cifuentes – 17509
Student from Universidad del Valle de Guatemala 

