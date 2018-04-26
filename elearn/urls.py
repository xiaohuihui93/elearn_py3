"""elearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
#    url('^$', TemplateView.as_view(template_name="index.html"), name="index")  # 新增代码
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url('^login/$', TemplateView.as_view(template_name="login.html"), name="login")  # 新增代码, 写法与index类似.
#    url('^login/$', <span style="font-family:Arial, Helvetica, sans-serif;">user_</span><span style="font-family:Arial, Helvetica, sans-serif;">login, name="login")  # 将原来的login写法修改成这样</span>
 ]
