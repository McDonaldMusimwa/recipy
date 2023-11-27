from django.urls import path
from . import views
app_name = 'recipes'
urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('<int:recipe_id>/results/', views.results, name='results'),
    path('<int:recipe_id>/addcomment/', views.addcomment,name='addcomment'),
]
