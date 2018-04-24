from django.conf.urls import url,include
from QA import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # 问答系统的起初页面，会列出所有的答案记录,返回到前台的热门问题
    url(r'^search_form/$', views.search_form, name='search_form'),  # 问题提出并提交
    url(r'^history_question/$',views.history_quesion,name='history_quesion'),  # 取得用户的历史纪录
]