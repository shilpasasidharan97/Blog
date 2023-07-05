from django.contrib import admin
from web.models import Category, CookingStep, Ingredient, Profile, Recipe

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(CookingStep)