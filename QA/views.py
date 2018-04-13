from django.shortcuts import render
from haystack.views import SearchView
import json
from . import models
from django.http import HttpResponse
from django.core import serializers

# def toDicts(objects):
#     obj_arr = []
#     for o in objects:
#         obj_arr.append(o.toDict())
#     return obj_arr

class MySearchView(SearchView):
    def extra_context(self):
        answers=serializers.serialize("json",models.Question.objects.all())
        # answers_dicts=answers.toDicts(answers)
        Answers = json.dumps(answers, ensure_ascii=False)
        return HttpResponse(Answers, content_type='application/json')
