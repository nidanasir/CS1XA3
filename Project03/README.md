# CS 1XA3 Project03 - <nasirn4>

## Overview
Install conda enivornment with this [link]( https://docs.anaconda.com/anaconda/install/)

Activate the **djangoenv** through
`conda activate djangoenv`  

Run locally with
`python manage.py runserver localhost:8000`

Run on mac1xa3.ca with
`python manage.py runserver localhost:10072`

Log in with lalaland_123, password: #Umoklol12

## Objectives

### Objective 01

**Description:**
- this feature is displayed in *signup.djhtml* which is rendered by *signup_view* in *login/views.py*
- it makes a **POST** request sent by the form to create a new user
- user is then automatically logged in and redirected to the **messages page**

**Exceptions:**
 - If the /e/nasirn4/ is called without arguments the user is redirected to *login:login.djhtml*

### Objective 02

**Description:**
- this feature is displayed in *social_base.djhtml* which is located in *social/templates
- it implements a real Profile and Interests corresponding to the currently logged in user including birthday, location and employement.

### Objective 03

**Description:**
- this feature is displayed in *account.djhtml* which is located in *social/templates* rendered by *account_view*
- it provides forms for changing the users current password
- it also provides forms for updating user info such employment, location, birthday, interests
- it handles **POST** requests sent by the from's to update the UserInfo object

**Exceptions:**
- A birthday must be written in YYY-MM-DD form

### Objective 04

**Description:**
- this feature is displayed in *people.djhtml* which is located in *social/templates* rendered by *people_view*
- it displays the users in the middle column who **are not friends** of the current user
- it displays only one person at a time and displays more as you click the more button rendered in **people.js**
- a session variable is used to keep track of how many people can be displayed


### Objective 05

**Description:**
- this feature is displayed in *people.djhtml* which is located in *social/templates* rendered by *friend_request_view*
- the *people.djhtml* configures the Friend Request button so it's id contains the user who sent the friend request
- the *friend_request_view* handles the **POST** by adding an entry to the FriendRequest model

### Objective 06

**Description:**
- this feature is displayed in *people.djhtml* which is located in *social/templates* rendered by *accept_decline_view*
- the id's of the accept and decline buttons in *people.djhtml* contain the username of the user who sent the friend request
- the *people.js* contains a function that sends a **POST** to accept_decline_view if the accept or decline buttons are pushed
- the *accept_decline_view* handles the **POST** request and deletes the corresponding FriendRequest entry
- if the request is accepted it updates **both users** friends relation 

### Objective 07

**Description:**
- this feature is displayed in *messages.djhtml* which is located in *social/templates* rendered by *messages_view*
- it displays all friends of the current user    
