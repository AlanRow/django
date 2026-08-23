from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.contrib.auth import login
from django.shortcuts import redirect

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
            return HttpResponseBadRequest("Invalid form")
    else:
        form = RegisterClientForm()

    template = loader.get_template("client_profile/signup.html")
    rendered = template.render({ "form": form }, request)
    return HttpResponse(rendered)