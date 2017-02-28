from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import UserProfile

User = get_user_model()


class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'

    def get_object(self):
        print('UserDetailView.get_object')
        print(self.kwargs.get('username'))
        return get_object_or_404(
            User,
            username__iexact=self.kwargs.get('username')
        )


class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        print('UserFollowView: ' + username)
        toggle_user = get_object_or_404(
            User,
            username__iexact=username
        )
        if request.user.is_authenticated():
            UserProfile.objects.user_follow(request.user, toggle_user)

        return redirect('profiles:detail', username=username)

