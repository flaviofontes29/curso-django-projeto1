from django.shortcuts import render, get_object_or_404
from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "recipes/pages/home.html",
        context={"recipes": recipes},
    )


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True)
    if not recipes:
        return render(request, "recipes/pages/404.html", status=404)

    return render(
        request,
        "recipes/pages/category.html",
        context={"recipes": recipes, "title": f"{recipes.first().category.name}"},
    )


def recipe(request, id):

    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={"recipe": recipe, "is_detail_page": True},
    )
