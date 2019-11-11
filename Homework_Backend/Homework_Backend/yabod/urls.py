from django.urls import path
from Homework_Backend.yabod import views

urlpatterns = [
    path('publisher', views.publisher_list),
    path('publisher/<int:pk>', views.publisher_detail),
]