"""fincaraiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from categories import views as views_categories
from reviews import views as views_reviews
from transactions import views as views_transactions
from cities import views as views_cities
from properties import views as views_properties
from propertytypes import views as views_propertyTypes
from states import views as views_states

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #Lists
    path('categories', views_categories.CategoryList.as_view()),
    path('reviews', views_reviews.ReviewList.as_view()),
    path('transactions', views_transactions.TransactionList.as_view()),
    path('cities', views_cities.CitiesList.as_view()),
    path('properties', views_properties.PropertiesList.as_view()),
    path('propertyTypes', views_propertyTypes.PropertyTypeList.as_view()),
    path('states', views_states.StateList.as_view()),
    #Details
    path('categories/<int:pk>/', views_categories.CategoryDetail.as_view()),
    path('reviews/<int:pk>/', views_reviews.ReviewDetail.as_view()),
    path('transactions/<int:pk>/', views_transactions.TransactionDetail.as_view()),
    path('cities/<int:pk>/', views_cities.CitiesDetail.as_view()),
    path('properties/<int:pk>/', views_properties.PropertiesDetail.as_view()),
    path('propertyTypes/<int:category>/', views_propertyTypes.PropertyDetail.as_view()),
    path('states/<int:pk>/', views_states.StateDetail.as_view()),
]
