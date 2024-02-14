from django import forms
from .models import ReachoutModel, UserPofileModel
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def check_name(value):
    if not value.isalpha():
        raise forms.ValidationError("Your name must be alpha numeric")


class ReachoutForm(forms.Form):
    name = forms.CharField(max_length=155, validators=[check_name])
    prenom = forms.CharField(max_length=155)
    email = forms.EmailField()
    verify_email = forms.EmailField()
    commentaire = forms.CharField(max_length=500, widget=forms.Textarea)
    botcatcher = forms.CharField(
        max_length=55, required=False, widget=forms.HiddenInput
    )

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]
        if email != verify_email:
            raise forms.ValidationError("Email don't match")

    def clean_botcatcher(self):
        if len(self.cleaned_data["botcatcher"]) > 0:
            raise forms.ValidationError("Tu es un Robot")


class NewReachoutForm(forms.ModelForm):
    botcatcher = forms.CharField(
        max_length=55,
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
    )

    class Meta:
        model = ReachoutModel
        exclude = ("id",)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]
        if email != verify_email:
            raise forms.ValidationError("Email don't match")


class UserProfileForm(forms.ModelForm):
    botcatcher = forms.CharField(
        max_length=55,
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
    )

    class Meta:
        model = UserPofileModel
        fields = ("portfolio_site", "profile_pic")


class UserForm(forms.ModelForm):
    vemail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    vpassword = forms.CharField(widget=forms.PasswordInput)
    botcatcher = forms.CharField(
        max_length=55,
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def clean(self):
        all_clean_data = self.cleaned_data

        email = all_clean_data["email"]
        vemail = all_clean_data["vemail"]

        password = all_clean_data["password"]
        vpassword = all_clean_data["vpassword"]

        if email != vemail:
            raise forms.ValidationError("Email don't mach")
        if vpassword != password:
            raise ValidationError("Password don't match")
