"""blogSample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

import blogSample

# blogSample名前空間で使用したいアプリのurls.pyをincludeするために
# 以下のurlpatternsにinclude('DBlog.urls')を指定している。
# また、blogSample名前空間共通の管理者ページとしてadmin.site.urlsを同じくincludeしている。

urlpatterns = [
    # DBlogはアプリとしてのルートパスになる想定。
    # その配下に表示させるためのパスをinclude('DBlog.urls')で指定している
    path('DBlog/', include('DBlog.urls')),
    path('admin/', admin.site.urls),
]
