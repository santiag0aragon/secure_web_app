from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from messages_app.models import NotificationUser
from messages_app.views import load_user_objects
# from forms import UserProfileForm


def login(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('datata_profile/login/login.html', args)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        # return HttpResponseRedirect('/accounts/logged_in/')
        return HttpResponseRedirect('/messages/main')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

# TODO: este logged_in deberia ser usado y redirigir a demo

@login_required
def logged_in(request):
    n_user = NotificationUser.objects.filter(user=request.user, viewed=False)
    args = {}
    args['user'] = request.user
    args['first_name'] = request.user.first_name
    args['last_name'] = request.user.last_name
    args['notifications_user'] = n_user
    args['notifications_group'] = n_group
    return render_to_response('datata_profile/login/logged_in.html', args)


def invalid_login(request):
    args = load_user_objects(request)
    auth.logout(request)
    args['user'] = request.user
    return render_to_response('datata_profile/login/invalid_login.html', args)


@login_required
def logout(request):
    args = load_user_objects(request)
    auth.logout(request)
    args['user'] = request.user
    return render_to_response('datata_profile/login/logout.html', args)


@login_required
def profile(request):
    args = load_user_objects(request)
    return render_to_response('datata_profile/profile/profile.html', args)
