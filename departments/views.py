# from django.shortcuts import render
# from django.http import JsonResponse

# Create your views here.
# def read(request) :
#     # TODO : 비즈니스 로직 호출
#     print("departments/read")
#     return JsonResponse({
#         "message" : "read called"
#     })

# departments/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .form import DepartmentForm
from .models import Departments

def department_search(request):
    # Query Parameter 가져오기
    dept_no = request.GET.get("dept_no")
    dept_name = request.GET.get("dept_name")

    qs = Departments.objects.all()
    if dept_no:
        qs = qs.filter(dept_no=dept_no)
    if dept_name:
        qs = qs.filter(dept_name__icontains=dept_name)

    context = {"departments": qs}
    return render(request, "departments/table.html", context)

def department_search_api(request):
    dept_no = request.GET.get("dept_no")
    dept_name = request.GET.get("dept_name")

    qs = Departments.objects.all()
    if dept_no:
        qs = qs.filter(dept_no=dept_no)
    if dept_name:
        qs = qs.filter(dept_name__icontains=dept_name)

    data = [{"dept_no": d.dept_no, "dept_name": d.dept_name} for d in qs]
    return JsonResponse(data, safe=False)

class DepartmentsListView(ListView) :
    model = Departments
    template_name = "departments/department_list.html"
    content_object_name = "departments"

    def get_queryset(self) :
        queryset = super().get_queryset()
        dept_no = self.request.GET.get("dept_no")

        if dept_no :
            queryset = queryset.filter(dept_no=dept_no)
        
        queryset = queryset.order_by("dept_no")
        return queryset

class DepartmentsCreateView(CreateView) :
    model = Departments
    #fields = ["dept_no", "dept_name"]
    template_name = "departments/department_form.html"
    success_url = reverse_lazy("departments:department_list")
    form_class = DepartmentForm

class DepartmentsUpdateView(UpdateView) :
    model = Departments
    template_name = "departments/department_form.html"
    success_url = reverse_lazy("departments:department_list")
    form_class = DepartmentForm
    pk_url_kwarg = "dept_no"