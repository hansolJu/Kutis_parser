from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView

from core.kutis_parser import *
from core.models import StudentInfo
from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        # Data bounded form인스턴스 생성
        login_form = LoginForm(request.POST)

        # 유효성 검증에 성공할 경우
        # form으로부터 username, password값을 가져옴
        hukbun = request.POST['hukbun']
        password = request.POST['password']
        parser = StudentInfoParser()
        b= parser.login(hukbun,password)
        parser2 = StudentGradePaser()
        a=parser2.login(hukbun, password)
        print(a)
        if(a==False):
            HttpResponse('로그인 실패. 비밀번호를 확인해주세요.')

        # 디비에 있는지 조사.
        try:
            user = StudentInfo.objects.get(hukbun=hukbun)
        except:
            user = None

        # 우리 디비에 존재했을때,-----> 쿠티스 로그인후, 다시 우리디비 정보 출력
        if True:
            print('login success')
            passingdata = parser.parse_item(parser2.studentInfoUrl)
            parser.save_info(hukbun,passingdata)

            passingdata = parser2.parse_item(parser2.studentgradeUrl)
            parser2.save_info(hukbun,passingdata)

            #return redirect('login')#출력하는 페이지로 가기.
            #중간보고서 야매 데이터 html
        # 우리 디비에 없을때 -----> 쿠티스 로그인후,  크롤링후 우리디비 정보출력
        else:
            #쿠티스 로그인####
            if False:#쿠티스 로그인 성공:
                return redirect('개인정보동의화면')
            else:
                return HttpResponse('로그인 실패. 다시 시도 해보세요.')
        #쿠티스에 로그인조차 안됨

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def logout(request):
    django_logout(request)
    return redirect('accounts:login')

class TestView(ListView):
    template_name = 'test.html'
    #context_object_name = 'student_list'

    def get_queryset(self):
        return StudentInfo.objects.all()