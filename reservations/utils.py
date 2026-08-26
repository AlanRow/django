from django.http import Http404
from .models import Owner

def get_owner_by_id(id):
    try:
        return Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Owner doesnt exist")