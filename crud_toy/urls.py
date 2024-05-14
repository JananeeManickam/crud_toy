"""
URL configuration for crud_toy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from toy.views import ToyCreate
from toy.views import ToyListView
from toy.views import ToyDetails
from toy.views import ToyUpdate
from toy.views import ToyDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ToyCreate.as_view()),
    path('list/', ToyListView.as_view()),
    path('details/<pk>/', ToyDetails.as_view()),
    path('update/<pk>/', ToyUpdate.as_view()),
    path('delete/<pk>/', ToyDelete.as_view()),
]
