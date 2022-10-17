from django.contrib import admin
from .models import User, Movies, Reviews

# Register your models here.
admin.site.register(User)
admin.site.register(Movies)
admin.site.register(Reviews)
