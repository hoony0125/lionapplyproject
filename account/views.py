from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import reset_queries
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # 전자가 로그인 폼, 후자가 회원가입 폼 
from django.contrib.auth import login, logout
from account.forms import RegisterForm
from django.contrib import messages
from account.models import CustomUser
# Create your views here.

def login_view(request):
    if request.method == "POST":
        auth_form = AuthenticationForm(request=request,data=request.POST)
        if auth_form.is_valid():
            v_username = auth_form.cleaned_data.get('username')
            v_password = auth_form.cleaned_data.get('password')
            auth_user = authenticate(request=request, username = v_username, password = v_password)
            login(request, auth_user)
            return redirect('urlnamehome')
        else:
            if CustomUser.objects.filter(username=request.POST['username']).exists():
                messages.info(request,'비밀번호가 일치하지 않습니다.')
                return redirect('urlnamelogin')
            else: 
                messages.info(request,'존재하지 않는 계정입니다.')
                return redirect('urlnamelogin')
    else:   
        login_form = AuthenticationForm()
        return render(request,'login.html',{'views_login_form':login_form})

def signup_view(request):
    if request.method =='POST': 
        new_signup_form = RegisterForm(request.POST)

        if CustomUser.objects.filter(phone_number = request.POST['phone_number']).exists():   #전화번호 중복체크
                messages.info(request,'이미 가입되어 있는 번호입니다.')
                return redirect('urlnamesignup')

        if new_signup_form.is_valid():
            user = new_signup_form.save()
            login(request, user)
            return redirect('urlnamehome')
        else:
            if CustomUser.objects.filter(username = request.POST['username']).exists():   #아이디 중복체크
                messages.info(request,'중복되는 ID가 존재합니다!')
                return redirect('urlnamesignup')

            elif request.POST['password1'] != request.POST['password2']:                  #비밀번호=비밀번호 확인
                messages.info(request,'비밀번호와 비밀번호 확인이 일치하지 않습니다!')
                return redirect('urlnamesignup')
            
            elif len(request.POST['password1']) < 8:                                       #비밀번호 8자리 이상 
                messages.info(request,'비밀번호는 8자리 이상으로 설정해주세요!')
                return redirect('urlnamesignup')

            elif request.POST['password1'].isdigit():
                messages.info(request,'비밀번호는 숫자로만 설정할 수 없습니다!')
                return redirect('urlnamesignup')

            elif request.POST['username'] in request.POST['password1']:
                messages.info(request,'비밀번호에 아이디가 포함될 수 없습니다')
                return redirect('urlnamesignup')

            elif CustomUser.objects.filter(student_id = request.POST['student_id']).exists():   #학번 중복체크
                messages.info(request,'이미 가입되어 있는 학번입니다.')
                return redirect('urlnamesignup')
            else:
                messages.info(request,'알 수 없는 에러가 발생했습니다. 관리자에게 문의하세요')
                return redirect('urlnamesignup')
            
            

    else:
        signup_form = RegisterForm()
        return render(request, 'signup.html',{'views_signup_form':signup_form})

def logout_view(request):
    logout(request)
    return redirect('urlnamehome')
    
