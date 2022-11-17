import zoneinfo

from django.utils import timezone


class TimezoneMiddleware:

    # One-time configuration and initialization.
    def __init__(self, get_response):
        self.get_response = get_response

    # Code to be executed for each request before the view and other middleware are called.
    def __call__(self, request):

        # Get django_timezone from the current session
        tzname = request.session.get("django_timezone")

        if tzname:
            # Use the defined django_timezone
            # Skip database lookups on the user profile as its already defined
            timezone.activate(zoneinfo.ZoneInfo(tzname))

        else:
            # Use user.profile.timezone as django_timezone is not defined
            if (
                request.user.is_authenticated
                and request.user.profile.timezone is not None
            ):
                # authenticated user: set django_timezone to user.profile.zonezone
                request.session["django_timezone"] = request.user.profile.timezone
                timezone.activate(zoneinfo.ZoneInfo(request.user.profile.timezone))
            else:
                # anonymous user: set django_timezone to UTC
                timezone.deactivate()
        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called

        return response
