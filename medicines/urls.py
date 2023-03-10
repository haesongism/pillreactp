from django.urls import path
from . import views

urlpatterns = [
    path("", views.Medicines.as_view()),
]

# path('api/v1/medicines/', include("medicines.urls")),