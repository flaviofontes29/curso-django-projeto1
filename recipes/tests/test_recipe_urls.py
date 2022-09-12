from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse("home")
        self.assertEqual(url, "/")

    def test_category_url_is_correct(self):
        url = reverse("category", kwargs={"category_id": 1})
        self.assertEqual(url, "/recipes/category/1/")

    def test_recipe_url_is_correct(self):
        url = reverse("recipe", kwargs={"id": 1})
        self.assertEqual(url, "/recipes/1/")