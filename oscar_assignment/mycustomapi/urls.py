from django.urls import path

from .views import ProfileView


app_name = "getcustomer"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('getcustomer/', ProfileView.as_view()),
]