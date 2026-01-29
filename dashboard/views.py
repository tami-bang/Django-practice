# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def chart_view(request):
    """
    로그인한 사용자의 이름을 context로 전달하여 chart.html 렌더링
    """
    context = {
        'name': request.user.get_full_name() or request.user.username,
        # 예시 데이터: 카드 내용 동적 처리 가능
        'cards': [
            {'title': 'Sales', 'value': '₩12,345', 'icon': 'fa-chart-line'},
            {'title': 'Users', 'value': '1,234', 'icon': 'fa-users'},
        ]
    }
    return render(request, 'chart.html', context)