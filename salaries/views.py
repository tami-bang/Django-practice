from django.shortcuts import render

def salary_list(request):
    return render(request, 'salaries/list.html', {})  # 나중에 템플릿 추가
