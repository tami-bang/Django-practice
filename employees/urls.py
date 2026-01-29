# from django.urls import path
# from . import views

# app_name = "employees"

# urlpatterns = [
#     # 직원 검색 (CBV, GET 방식)
#     path(
#         "search/",
#         views.EmployeesSearchView.as_view(),
#         name="employee_list"
#     ),

#     # 직원 추가
#     path(
#         "add/",
#         views.EmployeesCreateView.as_view(),
#         name="employee_add"
#     ),

#     # (연습/테스트용 – 필요 없으면 나중에 제거)
#     path("read/", views.read),
#     path("table/", views.table),
#     path("search-list/", views.EmployeesView.as_view(), name="search_list"),
#     path("search-list/", views.EmployeesView.as_view(), name="search_list"),
#     path("child-test/", views.child_test),

# ]

from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    # 사원 조회
    path(
        "search/",
        views.EmployeesSearchView.as_view(),
        name="employee_list"
    ),

    # 사원 추가
    path(
        "add/",
        views.EmployeesCreateView.as_view(),
        name="employee_add"
    ),

    path('search-list/', views.EmployeesSearchView.as_view()),
]
