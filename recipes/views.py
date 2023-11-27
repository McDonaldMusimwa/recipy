from django.http import Http404
from .models import Recipe,Comments
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging

def index(request):
    list_of_recipes = Recipe.objects.order_by('pub_date')[:5]
    context = {"list_of_recipes": list_of_recipes}
    return render(request,'recipes/index.html',context)

"""
def home(request,question_id):
    try:
       list_of_recipes= Recipe.objects.order_by(pk=question_id)
    except Recipe.DoesNotExist:
       raise Http404('rECIPE DOES NOT EXIST')

    return render(request,'recipesviews/detail.html',{'recipe':recipe})
"""
def detail(request, recipe_id):
    
    recipe= get_object_or_404(Recipe,pk=recipe_id)
    comments = Comments.objects.filter(recipe=recipe)
    return render(request,'recipes/detail.html',{'recipe': recipe, 'comments': comments})

def about(request):
    return render(request,'recipes/about.html')

# add this at the beginning of your views.py file
logger = logging.getLogger(__name__)

def results(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    
    # Log information about the fetched recipe
    logger.debug(f"Fetched recipe with ID: {recipe.id}, Title: {recipe.recipe_title}")

    comments = Comments.objects.filter(recipe=recipe)
    
    # Log the number of comments fetched
    logger.debug(f"Fetched {comments.count()} comments for recipe with ID: {recipe.id}")

    return render(request, 'recipes/detail.html', {'recipe': recipe, 'comments': comments})


def addcomment(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    try:
        comment_text = request.POST["comment_text"]
    except KeyError:
        # Redisplay the recipe detail page with an error message.
        return render(
            request,
            "recipes/detail.html",
            {
                "recipe": recipe,
                "error_message": "You didn't enter a comment.",
            },
        )
    else:
        recipe.comments_set.create(choice_text=comment_text, votes=0)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("recipes:addcomment", args=(recipe.id,)))