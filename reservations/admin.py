from django.contrib import admin

from .models import Place, Owner, OwnerDocument

admin.site.register(Place)
admin.site.register(Owner)
admin.site.register(OwnerDocument)
