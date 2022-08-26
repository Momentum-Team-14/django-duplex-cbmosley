from django.contrib import admin
from .models import Language, User, Snippet

# Register your models here.
admin.site.register(User)
admin.site.register(Snippet)
admin.site.register(Language)
