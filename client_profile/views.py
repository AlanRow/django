from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegisterClientForm


def account(request):
    template = loader.get_template("client_profile/account.html")
    rendered = template.render({ }, request)

    return HttpResponse(rendered)


def register(request):
    if request.method == "POST":
        form = RegisterClientForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("account")
    else:
        form = RegisterClientForm()

    return render(request, "client_profile/signup.html", {"form": form})
