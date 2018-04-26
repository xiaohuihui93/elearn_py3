from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login  # 新增代码
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  # Q可以帮助实现并集
from django.views.generic.base import View  # import View
from .models import UserProfile


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(
                Q(username=username) | Q(email=username))  # 会用username或者email对传入的username进行匹配
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")  # 新增, 根据刚才断点的分析结果, 用字典方法取出username的值
        pass_word = request.POST.get("password","")
        user = authenticate(username=user_name, password=pass_word)  # 新增, 利用django自带的authenticate方法来确认这个用户是否合法, 如果合法, 则user是一个非空对象.
        if user is not None:  # 如果该用户合法, 则user非空.
            login(request, user)  # django自带的login方法
            return render(request, "index.html")  # 登录成功后返回首页
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误!"})
    elif request.method == "GET":
        return render(request, "login.html", {})
