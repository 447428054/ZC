from django.shortcuts import render
from haystack.views import SearchView
import json
from . import models
from django.http import HttpResponse
from django.core import serializers
from QA.models import Question
from QA.models import UserToQuestion
from dataProcess import cutword
from django.db.models import Q



def toDicts(objects):
    obj_arr = []
    for o in objects:
        obj_arr.append(o.toDict())
    return obj_arr


# class MySearchView(SearchView):
#     def extra_context(self):
#         answers=serializers.serialize("json",models.Question.objects.all())
#         # answers_dicts=answers.toDicts(answers)
#         Answers = json.dumps(answers, ensure_ascii=False)
#         return HttpResponse(Answers, content_type='application/json')


# 返回最热门的前10个问题，返回的格式跟问答得到的形式相似
def index(request):
    if request.method == 'GET':
        print(request.GET)
        queryset = Question.objects.all().order_by('views')[:10]
        answer_dicts = toDicts(queryset)
        answer_jsons = json.dumps(answer_dicts, ensure_ascii=False)
        return HttpResponse(answer_jsons)


# 搜索函数，简单地来说就是将问题通过jieba提取TFIDF然后用关键词在数据库当中进行答案的提取，当数据库没有用户想要的答案时候
# 会同样也会返回一个关键词，让前台了解
def search_form(request):
    if request.method == 'POST':
        print(request.POST)
        q = request.POST.dict()
        question = q['question']
        print(question)
        list = cutword.cut(question)
        if len(list) == 1:
            queryset = Question.objects.filter(Q(keyword1__icontains=list[0])|Q(keyword2__icontains=list[0]))
            answer_dicts = toDicts(queryset)
        # 利用django中自带的模糊匹配来提高答案的精确度
        elif len(list) > 1:
            queryset = Question.objects.filter(Q(keyword1__icontains=list[1], keyword2__icontains=list[0])
                                               | Q(keyword1__icontains=list[0], keyword2__icontains=list[1])
                                               | Q(answer__icontains=list[0]))
            answer_dicts = toDicts(queryset)
        else:
            answer_dicts = [{'keyword1': -1,
                "keyword2":None,
                "answer":None,
                "views":None,
                }]
        answer_jsons = json.dumps(answer_dicts, ensure_ascii=False)
        return HttpResponse(answer_jsons)


# 用户的历史问题,使用数据库中用户的id来对用户曾经提过的问题进行回顾
def history_quesion(request):
    if request.method == 'POST':
        print(request.POST)
        userID = request.POST.dict()
        userid = userID['userid']
        print(userid)
        queryset = UserToQuestion.objects.filter(userid=userid)
        questions_dicts = toDicts(queryset)
        questions_jsons = json.dumps(questions_dicts, ensure_ascii=False)
        return HttpResponse(questions_jsons)
