"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/',include('departments.urls')),
    path('employees/',include('employees.urls')),
    path('salaries/',include('salaries.urls')),
    path('titles/',include('titles.urls')),
    # #path('', include("departments.urls")),

    # 로그인 페이지
    path('signin/', auth_views.LoginView.as_view(template_name="signin.html"), name="login"),
    path('accounts/', include('accounts.urls')),

    # # 로그인 후 첫 화면 및 chart.html
    # path('chart/', views.chart_view, name='chart'),  # FBV 연결
    # path('', views.chart_view),  # 로그인 후 첫 페이지

    # 로그인 후 첫 화면 (dashboard.urls를 통해 chart.html)
    path('', include('dashboard.urls')),  # '/' 접속 시 chart.html
]
