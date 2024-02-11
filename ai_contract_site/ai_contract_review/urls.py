from django.urls import path
from . import views

app_name = "ai_contract_review"
urlpatterns = [
    path("", views.index, name="index")
]