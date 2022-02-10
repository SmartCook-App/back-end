"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from apps.recipe.views import Recipe_APIView, Recipe_APIView_Detail
from apps.user.views import User_APIView, User_APIView_Detail


urlpatterns = [
    path('recipes/', Recipe_APIView.as_view()),
    path('recipes/<int:pk>/', Recipe_APIView_Detail.as_view()),
    path('user/', User_APIView.as_view()),
    path('user/<int:pk>/', User_APIView_Detail.as_view()),
]
