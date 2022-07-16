from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def profile(request):
    return render(request, './user/profile.html')

# 註冊功能


def user_register(request):
    message = ''
    form = UserCreationForm()

    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # 密碼問題
        if password1 != password2:
            message = '兩次密碼輸入不同'
        elif len(password1) < 8:
            message = '密碼過短(至少8個字元)'
        else:
            # 帳號問題
            if User.objects.filter(username=username).exists():
                message = '帳號重複'
            else:
                user = User.objects.create_user(username=username,
                                                password=password1)
                message = '註冊失敗'
                if user:
                    user.save()
                    message = '註冊成功!'

        print(username, password1, password2)

    return render(request, './user/register.html', {'form': form, 'message': message})
