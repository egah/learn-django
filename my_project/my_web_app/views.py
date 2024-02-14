from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import ReachoutForm, NewReachoutForm, UserProfileForm, UserForm
from django.urls import reverse, reverse_lazy
from .models import ReachoutModel
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import SchoolModel, StudentModel


def homepage(request):
    return render(request, "my_web_app/homepage.html")


class CBV(View):
    pass


def reachout_vew(request):
    if request.method == "POST":
        form = ReachoutForm(request.POST)
        if form.is_valid():
            print("Ton email est :", form.cleaned_data["email"])
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = ReachoutForm()
    return render(request, "my_web_app/reachout.html", {"form": form})


def new_reachout_view(request):
    if request.method == "POST":
        form = NewReachoutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Good Job")
    else:
        form = NewReachoutForm()

    return render(request, "my_web_app/new_reachout.html", {"form": form})


class CommentView(TemplateView):
    template_name = "my_web_app/comment.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["users"] = ReachoutModel.objects.all()
        return context


def register_view(request):
    if request.method == "POST":
        user = UserForm(request.POST)
        info = UserProfileForm(request.POST)

        if user.is_valid() and info.is_valid():
            #! je creer un utilisateur
            user_info = user.save(commit=False)
            #! set password qui va permettre le hashage du password
            user_info.set_password(user_info.password)
            #! j'enregistre le password hasher
            user_info.save()

            profile = info.save(commit=False)
            profile.user = user_info
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            return HttpResponse("Merci de vous être inscrit")
    else:
        user = UserForm()
        info = UserProfileForm()
    return render(request, "my_web_app/register.html", {"user": user, "info": info})


def login_view(request):
    if request.method == "POST":
        user = request.POST.get("user")
        passwd = request.POST.get("passwd")

        connect = authenticate(username=user, password=passwd)

        if connect:
            if connect.is_active:
                login(request, connect)
                return HttpResponseRedirect(reverse("homepage"))
            else:
                return HttpResponse("Your account is not active")
        else:
            return HttpResponse("your account don't exits")
    return render(request, "my_web_app/login.html", {})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


class SchoolListView(ListView):
    context_object_name = "school_list"
    model = SchoolModel
    template_name = "my_web_app/school_list.html"


class SchoolDetailsView(DetailView):
    context_object_name = "school_details"
    model = SchoolModel
    template_name = "my_web_app/school_details.html"


class CreateSchoolView(CreateView):
    model = SchoolModel
    fields = ("name", "principal", "location")

    success_url = reverse_lazy("school_list")


class UpdateSchoolView(UpdateView):
    model = SchoolModel
    fields = ("name", "principal")


class SchoolDeteteView(DeleteView):
    model = SchoolModel

    success_url = reverse_lazy("school_list")
