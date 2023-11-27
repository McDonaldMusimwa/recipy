import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    pub_date = models.DateTimeField("date published")
    recipe_title = models.CharField(max_length=50)
    recipe_text = models.CharField(max_length=800)
    def __str__(self):
        return self.recipe_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comments(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)    
    def __str__(self):
        return self.choice_text