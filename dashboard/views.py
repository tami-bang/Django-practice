# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings
import os
import logging

# 로거 생성
logger = logging.getLogger(__name__)

def home(request: WSGIRequest):
    #logger.info("Login : " + request.user.firstname + request.user.last_name)
    logger.info(f"Login : {request.user.first_name} {request.user.last_name}")

    chart_labels = [40, 50, 60, 70, 80, 90, 100]
    chart_data = [10, 9, 8, 7, 8, 9, 10]

    return render(request, "dashboard/chart.html", {
        "chart_labels": chart_labels,
        "chart_data": chart_data,
        "name": request.user.get_full_name() or request.user.username,
        "cards": [
            {"title": "Sales", "value": "₩12,345", "icon": "fa-chart-line"},
            {"title": "Users", "value": "1,234", "icon": "fa-users"},
        ]
    })
    # """
    # 로그인 후 기본 페이지: chart.html
    # """
    # # 로그인 정보 로그 기록
    # user_name = f"{request.user.first_name} {request.user.last_name}".strip()
    # logger.info(f"Login: {user_name or request.user.username}")

    # username = request.user.username
    # default_image = 'img/user.jpg'
    # user_image_path = f'static/img/{username}.jpg'

    # # 프로필 이미지 존재 여부 확인
    # full_path = os.path.join(settings.BASE_DIR, user_image_path)
    # profile_image = f'img/{username}.jpg' if os.path.exists(full_path) else default_image

    # context = {
    #     'name': request.user.get_full_name() or username,
    #     'profile_image': profile_image,
    #     'cards': [
    #         {'title': 'Sales', 'value': '₩12,345', 'icon': 'fa-chart-line'},
    #         {'title': 'Users', 'value': '1,234', 'icon': 'fa-users'},
    #     ]
    # }
    # return render(request, "dashboard/chart.html", context)

@login_required
def chart_view(request: WSGIRequest):
    """
    로그인한 사용자의 이름과 프로필 이미지, 카드 정보 전달
    """
    username = request.user.username
    default_image = 'img/user.jpg'
    user_image_path = f'static/img/{username}.jpg'  # 예: tami_bang.jpg

    # 실제 파일 존재 여부 체크
    full_path = os.path.join(settings.BASE_DIR, user_image_path)
    profile_image = f'img/{username}.jpg' if os.path.exists(full_path) else default_image

    # 접근 로그 기록
    logger.info(f"Chart viewed by: {request.user.get_full_name() or username}")

    context = {
        'name': request.user.get_full_name() or username,
        'profile_image': profile_image,
    }
    return render(request, "dashboard/chart.html", context)
