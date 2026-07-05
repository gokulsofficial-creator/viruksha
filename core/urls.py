from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services_view, name='services'),
    path('products/', views.products_view, name='products'),
    path('products/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<slug:slug>/', views.project_detail_view, name='project_detail'),
    path('enquiry/', views.enquiry_view, name='enquiry'),
]






