from django.contrib import admin
from web.models import CookingStep, Ingredient, Recipe

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(CookingStep)