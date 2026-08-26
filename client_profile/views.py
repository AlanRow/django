from django.http import HttpResponse, Http404
from django.template import loader


def account(request):
    template = loader.get_template("client_profile/account.html")
    rendered = template.render({ }, request)

    return HttpResponse(rendered)


def register(request):
    pass
