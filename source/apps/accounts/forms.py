import re

from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ValidationError

User = get_user_model()


def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

    # overall result
    password_ok = not (
        length_error
        or digit_error
        or uppercase_error
        or lowercase_error
        or symbol_error
    )

    return {
        "password_ok": password_ok,
        "length_error": length_error,
        "digit_error": digit_error,
        "uppercase_error": uppercase_error,
        "lowercase_error": lowercase_error,
        "symbol_error": symbol_error,
    }


class UserSignupForm(forms.ModelForm):
    """
    Form that will be rendered on a user sign up.
    Check UserSocialSignupForm for accounts created from social.
    """

    name = forms.CharField(max_length=191, label="Full name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("name", "email", "password")

    def clean_password(self):

        userpassword = password_check(self.data["password"])

        if userpassword["length_error"]:
            raise ValidationError("Password length must be at least 8 characters.")
        elif userpassword["digit_error"]:
            raise ValidationError("Password must contain at least 1 digit.")
        elif userpassword["uppercase_error"]:
            raise ValidationError(
                "Password must contain at least 1 uppercase character."
            )
        elif userpassword["lowercase_error"]:
            raise ValidationError(
                "Password must contain at least 1 lowercase character."
            )
        elif userpassword["symbol_error"]:
            raise ValidationError("Password must contain at least 1 special character.")
        else:
            return self.data["password"]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    See UserSignupForm otherwise.
    """

    name = forms.CharField(max_length=191, label="Full name")

    class Meta:
        model = User
        fields = ("name",)

    def save(self, request):
        user = super(UserSocialSignupForm, self).save(request)
        user.name = self.cleaned_data["name"]
        user.save()
        return user


class DeleteAccountForm(forms.Form):

    confirm = forms.BooleanField()
