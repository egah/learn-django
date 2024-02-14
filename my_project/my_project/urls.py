from django.urls import re_path, include
from my_web_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("^$", views.homepage, name="homepage"),
    re_path("^reachout/$", views.reachout_vew, name="reachout"),
    re_path("^new_reachout$", views.new_reachout_view, name="new_reachout"),
    re_path("^comments/all/$", views.CommentView.as_view(), name="comments"),
    re_path("^sinscrire/$", views.register_view, name="register"),
    re_path("^seconnecter/$", views.login_view, name="seconnecter"),
    re_path("^logout/", views.logout_view, name="logout"),
    re_path("^school_list/all/$", views.SchoolListView.as_view(), name="school_list"),
    re_path(
        r"^school_list/all/(?P<pk>\d+)/$",
        views.SchoolDetailsView.as_view(),
        name="detail_view",
    ),
    re_path("^create_school/$", views.CreateSchoolView.as_view(), name="create_view"),
    re_path(
        r"^update_school_info/(?P<pk>\d+)/$",
        views.UpdateSchoolView.as_view(),
        name="update_view",
    ),
    re_path(
        r"^delete_school/(?P<pk>\d+)/$",
        views.SchoolDeteteView.as_view(),
        name="delete_view",
    ),
]
