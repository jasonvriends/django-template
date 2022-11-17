from apps.accounts.views import AccountDeleteView, delete_account_done_view
from django.urls import path

app_name = "accounts"


urlpatterns = [
    path("delete", view=AccountDeleteView.as_view(), name="deleteaccount"),
    path("delete/done", view=delete_account_done_view, name="deleteaccount_done"),
]
