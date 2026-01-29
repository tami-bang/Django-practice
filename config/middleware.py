from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class LoginRequireMiddleware :

    def __init__(self, get_response) :
        self.get_response = get_response
        self.login_url = reverse('login')

    def __call__(self, request):

        # 로그인 페이지, 로그아웃 페이지 등 로그인 관련 URL은 통과
        if request.path == self.login_url or request.path == reverse('logout') :
            return self.get_response(request)
        
         # 로그인 안 된 경우 리다이렉트
        if not request.user.is_authenticated :
            return redirect(self.login_url)
        
        # 로그인 된 사용자라면 다음 미들웨어 또는 뷰 처리 진행
        response = self.get_response(request)
        return response
