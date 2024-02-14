from typing import Any
from django.db import models
import random
import uuid
from functools import wraps
from django.utils import timezone
from address.models import AddressField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


# Create your models here.
def product_price():
    return random.randrange(1000, 3000)


# utiliser un dcorateur
def identifiant_commande(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs))[:10] + str(random.randint(0, 10000))

    return wrapper


uuid0 = identifiant_commande(uuid.uuid4)


def validate(value):
    if value <= 0:
        raise ValidationError("The price must be positive")


def check_name(value):
    if not value.isalpha():
        raise ValidationError("Your name must be alpha numeric")


def payment():
    return random.choice(["Visa", "PayPal", "Klama", "MasterCard"])


class Product(models.Model):
    name = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(validators=[validate])

    def __str__(self):
        return self.name


class Client(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    # TODO address = AddressField(null=True)
    address = models.TextField(null=True, blank=True)
    MEN = "M"
    WOMEN = "F"
    SEX_OF_CUSTOMER = [(MEN, "Men"), (WOMEN, "Women")]
    sex = models.CharField(max_length=1, choices=SEX_OF_CUSTOMER, default=WOMEN)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.name, self.prenom)


class Command(models.Model):
    id = models.TextField(unique=True, default=uuid0, primary_key=True)
    payment_method = models.CharField(max_length=50, default=payment)
    date = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class ReachoutModel(models.Model):
    name = models.CharField(max_length=155, validators=[check_name])
    prenom = models.CharField(max_length=155)
    email = models.EmailField()
    commentaire = models.TextField(max_length=1500)

    def __str__(self):
        return "%s %s" % (self.name, self.prenom)


class UserPofileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class SchoolModel(models.Model):
    name = models.CharField(max_length=250)
    principal = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk": self.pk})


class StudentModel(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    school = models.ForeignKey(
        SchoolModel, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self):
        return self.name
