from django.urls import path
from . import views

# アプリとして用意するURLのパターン定義している
# pathの第一引数がパス、第二引数がviewの種類、第三引数は名前
# ※第三引数が何に使われるのかはよくわからない

urlpatterns = [
    path('', views.index, name='index'),
]