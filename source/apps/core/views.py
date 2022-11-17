from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def home_view(request):

    context = {}

    return render(request, "home.html", context)


@require_http_methods(["GET"])
def privacypolicy_view(request):

    context = {}

    return render(request, "privacypolicy.html", context)
