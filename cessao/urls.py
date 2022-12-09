from django.urls import path
from . import views

urlpatterns = [
    path('csv/', views.ReadCSVView.as_view()),
    path('local-csv/', views.ReadLocalCsv.as_view())
]
