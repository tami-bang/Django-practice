# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

@login_required
def chart_view(request):
    """
    로그인한 사용자의 이름과 프로필 이미지 경로 전달
    """
    username = request.user.username
    default_image = 'img/user.jpg'
    user_image_path = f'static/img/{username}.jpg'  # 예: tami_bang.jpg

    # 실제 파일 존재 여부 체크
    full_path = os.path.join(settings.BASE_DIR, user_image_path)
    if os.path.exists(full_path):
        profile_image = f'img/{username}.jpg'
    else:
        profile_image = default_image

    context = {
        'name': request.user.get_full_name() or username,
        'profile_image': profile_image,
        'cards': [
            {'title': 'Sales', 'value': '₩12,345', 'icon': 'fa-chart-line'},
            {'title': 'Users', 'value': '1,234', 'icon': 'fa-users'},
        ]
    }
    return render(request, 'chart.html', context)