from django.urls import path
from . import views

urlpatterns = [
    path("load-steps/", views.load_steps, name="ajax_load_steps"),
    path(
        "add/",
        views.add_milestone_with_achievement,
        name="add_milestone_with_achievement",
    ),
]
