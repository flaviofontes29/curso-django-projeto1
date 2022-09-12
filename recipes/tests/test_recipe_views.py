from django.test import TestCase
from django.urls import resolve
from recipes import views 


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve("/")
        self.assertIs(view.func, views.home)
