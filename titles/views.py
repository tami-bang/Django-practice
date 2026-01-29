# titles/views.py
from django.shortcuts import render
from django.views import View

# 최소 CBV
class TitlesListView(View):
    template_name = 'titles_list.html'  # 나중에 만들 템플릿

    def get(self, request):
        # 실제 데이터가 없으면 빈 context라도 줌
        context = {}
        return render(request, self.template_name, context)