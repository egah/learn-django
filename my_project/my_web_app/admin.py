from django.contrib import admin
from .models import (
    Client,
    Command,
    Product,
    ReachoutModel,
    UserPofileModel,
    SchoolModel,
    StudentModel,
)

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Command)
admin.site.register(ReachoutModel)
admin.site.register(UserPofileModel)
admin.site.register(StudentModel)
admin.site.register(SchoolModel)
