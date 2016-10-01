from models import NotificationUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from forms import NotificationForm


@login_required
def main(request):

    args = load_user_objects(request)
    user = request.user
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = user
            f.save()
    else:
        form = NotificationForm()
    args = load_user_objects(request)
    args['form'] = form
    args.update(csrf(request))
    return render(request, 'datata_notification/notification/db.html', args)


@login_required
def load_user_objects(request):
    '''
    Loads user objects needed to render the templates
    i.e.
        + User
        + First name
        + Last name
        + User notification
        + Group notification
        + User id
        + Logo
        + BG color
        + Link color
        + Active tab color
    '''
    user = request.user
    n_user = NotificationUser.objects.filter(user=user, viewed=False)
    args = {}
    args['user'] = user
    args['first_name'] = user.first_name
    args['last_name'] = user.last_name
    args['notifications_user'] = n_user
    args['id'] = str(user.id)
    return args


@login_required
def show_notification(request, notification_id):
    n = NotificationUser.objects.get(id=notification_id)
    return render_to_response(
        "messages/notification/notification.html",
        {"notification": n})


@login_required
def delete_notification(request, notification_id):
    n = NotificationUser.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect("/messages/main/")

