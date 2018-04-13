from django.conf.urls import url,include
from QA import views

urlpatterns = [
    url(r'^search/', views.MySearchView(),name='haystack_search'),
]