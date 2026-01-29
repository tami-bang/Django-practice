# titles/urls.py
from django.urls import path
from . import views

app_name = 'titles'

urlpatterns = [
    path('', views.TitlesListView.as_view(), name='titles_list'),
    # 다른 URL 패턴
]