from django.urls import include, path
from . import views

urlpatterns = [
    path('read/', views.read),
    path('table/', views.table),
    path('search/', views.search),
    #path('search-cbv/', views.EmployeesView.as_view())
    path('search-cbv/', views.EmployeesView.as_view(), name="search_cbv"),
    path('child-test/', views.child_test),
    path('search-list/', views.EmployeesSearchView.as_view()),
    path('add/', views.EmployeesCreateView.as_view()),
]

