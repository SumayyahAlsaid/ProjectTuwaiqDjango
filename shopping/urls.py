"""
URL configuration for shopping project.

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
from skinCare import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v1.landingPage,name='landingPage'),
    path("showSkincare/", v1.showSkincare,name='showSkincare'),
    path("productDetails/<int:id>", v1.productDetails,name='productDetails'),
    path("auth_login/", v1.auth_login,name='auth_login'),
    path("auth_register/", v1.auth_register,name='auth_register'),
    path("auth_logout/", v1.auth_logout,name='auth_logout'),
    path("checkout/", v1.checkout,name='checkout'),
    path("add_to_cart/<int:id>", v1.add_to_cart,name='add_to_cart'),
]
