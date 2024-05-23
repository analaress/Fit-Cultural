from django.contrib import admin
from django.contrib.admin import ModelAdmin

from fit_cultural.models import Pessoa

admin.site.register(Pessoa)
