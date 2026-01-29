from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Employees
from employees.form import EmployeeForm


class EmployeesSearchView(ListView):
    """
    사원 조회 (GET 검색)
    """
    model = Employees
    template_name = "employees/employees_list.html"
    context_object_name = "employees"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()

        emp_no = self.request.GET.get("emp_no", "").strip()
        first_name = self.request.GET.get("first_name", "").strip()

        if emp_no:
            qs = qs.filter(emp_no=emp_no)
        if first_name:
            qs = qs.filter(first_name__icontains=first_name)

        return qs.order_by("emp_no")
    


class EmployeesCreateView(CreateView):
    """
    사원 추가
    """
    model = Employees
    template_name = "employees/employee_form.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employees:employee_list")
