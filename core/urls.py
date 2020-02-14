from django.urls import path
from .api import ProjectList,ReviewCreateList

urlpatterns = [
    path('',ProjectList.as_view(),name="project_list"),
    path('review/',ReviewCreateList.as_view(),name="review_list")
]