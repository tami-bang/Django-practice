from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.http import require_GET
from django.views.generic import ListView, CreateView

from employees.form import EmployeeForm

from .models import Employees

# Create your views here.
def read(request):
    # TODO : service(비즈니스 로직) 호출
    return render(request, 'employees/list.html', 
        {"name" : "gorani"
    })

def table(request) :

    users = [ # 딕셔너리 여러개 해서 
        {"id" : 1, "first_name" : "Go"  , "last_name" : "rani"     , "email" : "gorani@email.com", "image": "img/default.jpg"},
        {"id" : 2, "first_name" : "Kim" , "last_name" : "doyun"    , "email" : "kimdy@email.com", "image": "img/default.jpg"},
        {"id" : 3, "first_name" : "Kang", "last_name" : "byoclearngchul", "email" : "kangbc@email.com", "image": "img/default.jpg"},
        {"id" : 4, "first_name" : "Bang", "last_name" : "Tami"     , "email" : "bangtm@email.com", "image": "img/tami_bang.jpg"}
    ]

    # 내 프로필 지정 (users에서 바로 가져오기)
    profile = next(user for user in users if user["first_name"] == "Bang" and user["last_name"] == "Tami")

    return render(request, "employees/table.html", {
        "users": users,
        "profile": profile,
        #"total_count": users.count(),
        "total_count": len(users),
    })


def search(request : WSGIRequest) :

    if request.method == "GET" :
        pass
    elif request.method == "POST" :
        emp_no = request.POST.get("emp_no")
        first_name = request.POST.get("first_name")
        qs = Employees.objects.all()
        if emp_no:
            qs = qs.filter(emp_no=emp_no)
        if first_name:
            qs = qs.filter(first_name__icontains=first_name)
        return render(request, "employees/employee_list.html", {"employees": qs})
    return render(request, "employees/employee_list.html", {"employees": Employees.objects.none()})

@require_GET
def search_get(request) :
    pass

class EmployeesView(View):
    def get(self, request):
        profile = {
            "first_name": "Bang",
            "last_name": "Tami",
            "image": "img/tami_bang.jpg"
        }
        context = {
            "employees": Employees.objects.none(),
            "profile": profile
        }
        return render(request, "employees/employee_list.html", context)
    def post(self, request):
        emp_no = request.POST.get("emp_no", "").strip()
        first_name = request.POST.get("first_name", "").strip()

        qs = Employees.objects.all()

        if emp_no.isdigit():
            qs = qs.filter(emp_no=int(emp_no))
        if first_name:
            qs = qs.filter(first_name__icontains=first_name)  # 부분 검색 가능
            # 필요시 last_name 도 같이 검색 가능
            # last_name = request.POST.get("last_name", "").strip()
            # if last_name:
            #     qs = qs.filter(last_name__icontains=last_name)
        
        profile = {
            "first_name": "Bang",
            "last_name": "Tami",
            "image": "img/tami_bang.jpg"
        }

        context = {"employees": qs, "profile": profile}

        print(f"검색 결과 개수: {qs.count()}")
        return render(request, "employees/employee_list.html", context)
    
def child_test(request) :
    return render(request, "employees/child.html")

class EmployeesSearchView(ListView):
    model = Employees # context에 employee.emp_no 이렇게 접근 가능하게 해줌
    template_name = "employees/employees_search.html"

class EmployeesCreateView(CreateView) :
    model = Employees
    template_name = "employees/employee_form.html"  # 새 폼 템플릿
    success_url = reverse_lazy("employees:employee_list")  # 완료 후 이동
    form_class = EmployeeForm