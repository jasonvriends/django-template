import zoneinfo

from apps.profiles.forms import ProfileForm
from apps.profiles.models import Profile
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import UpdateView


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "profile.html"
    success_url = reverse_lazy("profiles:profile")
    form_class = ProfileForm

    # get user profile without PK=<id>
    def get_object(self):
        self.request.session["django_timezone"] = self.request.user.profile.timezone
        timezone.activate(zoneinfo.ZoneInfo(self.request.user.profile.timezone))
        return self.request.user.profile

    # determine which submit button was pressed
    def form_valid(self, form):

        if "delete-avatar" in self.request.POST:
            # remove avatar from user profile
            form.instance.image = ""

        return super().form_valid(form)
