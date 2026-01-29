from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    login_url = reverse("login")
    return redirect(login_url)

@login_required
def chart_view(request):
    """
    로그인한 사용자 이름을 context로 전달하여
    chart.html을 렌더링
    """
    context = {
        'name': request.user.get_full_name() or request.user.username
    }
    return render(request, 'chart.html', context)