from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name="Products"),
    
    path('create/', views.createProduct, name="Product-create"),  
    path('upload/', views.uploadImage, name="image-upload"), 
    
    path('<str:pk>/reviews/', views.createProductReview, name="create-review"),  
    path('<str:pk>/', views.getProduct, name="Product"),  
    
    path('update/<str:pk>/', views.updateProduct, name="Product-update"),  
    path('delete/<str:pk>/', views.deleteProduct, name="Product-delete"),  
]