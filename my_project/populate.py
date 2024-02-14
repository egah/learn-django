import os
import random
from itertools import product

import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")
django.setup()

from my_web_app.models import Client, Command, Product, product_price

fake = Faker("fr_FR")
liste_product = [
    "Montre",
    "Veste",
    "Chaussue",
    "Sac",
    "Chemise",
    "Pull",
    "Lunette",
    "Fourrure",
]
liste_marque = ["Prada", "Gucci", "Versace", "Levis", "Zalando"]
product_marque = [*product(liste_product, liste_marque)]


def create_client():
    first_name = fake.first_name()
    last_name = fake.last_name()
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=80)
    address = fake.address()
    sex = random.choice(["M", "F"])
    email = fake.email()

    data_dict = {
        "name": first_name,
        "prenom": last_name,
        "date_naissance": birthday,
        "address": address,
        "sex": sex,
        "email": email,
    }
    return Client.objects.get_or_create(**data_dict)[0]


def create_product():
    produit = random.choice(product_marque)
    price = product_price()

    data_dict = {"name": produit[0], "marque": produit[1], "price": price}

    return Product.objects.get_or_create(**data_dict)[0]


def populate(N=500):
    liste_client = []
    liste_produit = []
    for _ in range(100):
        liste_produit.append(create_product())
    for _ in range(200):
        liste_client.append(create_client())
    for _ in range(N):
        cl = random.choice(liste_client)
        pr = random.choice(liste_produit)
        Command.objects.get_or_create(product=pr, client=cl)


if __name__ == "__main__":
    print("Starting population script")
    populate(1000)
    print("Finished population script")
