from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from . import models

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)


        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        posts = []

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post

        context = { 'user_info' : user_info
                  , 'posts' : posts }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    if not request.user.is_authenticated:
        redirect('login:login_view')

    if request.method == 'POST':
        user_info = models.UserInfo.objects.get(user=request.user)
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('social:account_view')
        oldemployment = user_info.employment
        newemployment = request.POST['employment']
        if oldemployment != newemployment:
            user_info.employment = newemployment
        oldlocation = user_info.location
        newlocation = request.POST['location']
        if oldlocation != newlocation:
            user_info.location = newlocation
        oldbirthday = user_info.birthday
        newbirthday = request.POST['birthday']
        if oldbirthday != newbirthday:
            user_info.birthday = newbirthday
        interestChecker = 0
        newinterest = request.POST['interest']
        if newinterest == "":
            pass
        else:
            for interest in user_info.interests.all():
                if interest.label == newinterest:
                    interestChecker = 1
            if interestChecker == 0:
                checkInterest = 0
                for interest in models.Interest.objects.all():
                    if interest.label == newinterest:
                        checkInterest = 1
                if checkInterest == 0:
                    models.Interest.objects.create(label=newinterest)
                    user_info.interests.add(newinterest)
                else:
                    user_info.interests.add(newinterest)       
        user_info.save()
    else:
        form = PasswordChangeForm(request.user)
        user_info = models.UserInfo.objects.get(user=request.user)
    context = { 'user_info' : user_info,
                 'form' : form, 
                  'interests' : user_info.interests.all()}
    return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
        numberOfPeople = request.session.get('counter',1)
        people = []
        all_people = []
        
        for person in models.UserInfo.objects.all():
            if person not in user_info.friends.all() and person.user != user_info.user:
                people += [person]
        for number in range(numberOfPeople):
            if len(people) <= number:
                pass
            else:
                all_people += [people[num]]

        # TODO Objective 5: create a list of all friend requests to current user
        friend_requests = []

        for friend in models.FriendRequest.objects.all():
            if friend.to_user == user_info:
                friend_requests += [friend]

        context = { 'user_info' : user_info,
                    'all_people' : all_people,
                    'friend_requests' : friend_requests }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = 0

        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    if postContent is not None:
        if request.user.is_authenticated:

            # TODO Objective 8: Add a new entry to the Post model

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts dispalyed

        # TODO Objective 9: update how many posts are displayed/returned by messages_view

        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people dispalyed

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed
        count = request.session.get('counter',1)
        request.session['counter'] = count + 1
        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        username = frID[3:]

        if request.user.is_authenticated:
            user_info = models.UserInfo.objects.get(user=request.user)
            people = []
            for person in models.UserInfo.objects.all():
                if str(person.user) == username:
                    people += [person]
            toUser = people[0]
            userThere = 0
             
            for request in models.FriendRequest.objects.all():
                if request.to_user == toUser and request.from_user == user_info:
                    userThere = 1
            if userThere == 0:
                friend = models.FriendRequest(to_user=userThere,from_user=user_info)
                friend.save()
                    
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    if data is not None:
        # TODO Objective 6: parse decision from data
        data = decision[0]
        username = decision[2:]
        if request.user.is_authenticated:
           
            # TODO Objective 6: delete FriendRequest entry and update friends in both Users
            user_info = models.UserInfo.objects.get(user=request.user)
            people = []
            for person in models.UserInfo.objects.all():
                if str(person.user) == username:
                    people += [person]
            fromUser = people[0]
            
            if data == "A":
                user_info.friends.add(fromUser)
                fromUser.friends.add(user_info)
                for friend in models.FriendRequest.objects.all():
                    if friend.to_user == user_info and friend.from_user == fromUser:
                        friend.delete()
                    elif friend.to_user == fromUser and friend.from_user == user_info:
                        friend.delete()
            elif data == "D":
                friend = models.FriendRequest.objects.get(to_user=user_info,from_user=fromUser)
                friend.delete()
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
