from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView
from panel.forms import RegisterForm, LoginForm
from panel.models import User


class HomeView(TemplateView):
    template_name = 'panel/index.html'


class RegisterUserView(View):
    def get(self,request):
        register_form = RegisterForm()
        context = {
            'register_form' : register_form
        }
        return render(request,'panel/register_page.html',context)

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user : bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email','این ایمیل در سیستم وجود دارد .')
            else:
                new_user = User(
                    email= user_email,
                    is_active= False,
                    username= user_email
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login'))

class LoginUserView(View):
    def get(self,request):
        login_form = LoginForm()
        context = {
            'login_form' : login_form
        }
        return render(request,'panel/login.html',context)

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user :
                is_password_correct = user.check_password(user_password)
                if is_password_correct:
                    login(request,user)
                    return redirect(reverse('home_page'))
                else:
                    login_form.add_error('password','کلمه عبور اشتباه است.')
            else:
                login_form.add_error('email','چنین حسابی یافت نشد.')

        context = {
            'login_form' : login_form
        }
        return render(request,'panel/login.html',context)





