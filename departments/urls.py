
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('read/', views.read),
# ]

# departments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # JSON 반환 API
    path('api/departments/search', views.department_search_api, name='search_api'),

    # HTML 렌더링
    path('list', views.department_search, name='department_list'),

    # search 경로도 HTML 렌더링에 연결
    path('search/', views.department_search, name='department_search'),
    
    path('search-list/', views.DepartmentsListView.as_view()),

]
