from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRecords, name="records"),
    
    path('create/', views.createRecord, name="record-create"),
    path('<str:pk>/', views.getRecord, name="record"),

    path('update/<str:pk>/', views.updateRecord, name="record-update"),
    path('delete/<str:pk>/', views.deleteRecord, name="record-delete"),
]