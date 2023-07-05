from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class Category(models.Model):
    title = models.CharField(max_length=225)


class Recipe(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)
    cooking_time = models.DurationField()
    serving_people = models.IntegerField()

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Recipe, self).save(*args, **kwargs)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class CookingStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='cooking_steps')
    step_number = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='cooking_steps/')

    def __str__(self):
        return f"Step {self.step_number}: {self.description}"


