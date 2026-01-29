# dashboard/urls.py
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.chart_view, name='chart'),  # 로그인 후 기본 화면
]
