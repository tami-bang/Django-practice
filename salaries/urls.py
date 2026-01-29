from django.urls import path
from . import views

app_name = 'salaries'

urlpatterns = [
    path('', views.salary_list, name='salary_list'),  # salary_list 뷰 이름 정의

]
