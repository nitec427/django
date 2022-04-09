from django.urls import path

from . import views

urlpatterns = [
    # path("jan", views.index),
    # path("feb", views.feb),
    path("<str:name>", views.navigation_page),
    path("<int:number>/<str:name>", views.months_by_number),
    path("<str:month>/<str:name>", views.remaining_months, name="month-str"),
] 