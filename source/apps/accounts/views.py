from apps.accounts.forms import DeleteAccountForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import DeleteView

User = get_user_model()


@require_http_methods(["GET"])
def delete_account_done_view(request):

    context = {}

    return render(request, "account/deleteaccount_done.html", context)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "account/deleteaccount.html"
    success_url = reverse_lazy("accounts:deleteaccount_done")
    form_class = DeleteAccountForm

    # get user account without PK=<id>
    def get_object(self):
        return self.request.user
