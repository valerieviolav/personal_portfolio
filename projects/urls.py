from django.urls import path 
from projects import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("training/", views.training_index, name="training_index"),
    path("training/<int:pk>/", views.training_detail, name="training_detail"),

]
