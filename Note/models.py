# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Note.SAL import finalGet


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    summay=models.TextField(null=True)
    label=models.TextField(null=True)


    def toDict(self):
        return {'title':self.title,
                'content':self.content,
                'summary':self.summay,
                'label':self.label
                }

