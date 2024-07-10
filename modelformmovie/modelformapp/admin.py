from django.contrib import admin
from modelformapp.models import Movie
class MovieAdmin(admin.ModelAdmin):
    list_display=['title','rating','cast','release','gener']

admin.site.register(Movie,MovieAdmin)     
