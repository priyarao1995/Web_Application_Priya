# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.

class Process(models.Model):
      title = models.CharField(max_length=100)
      feedback = models.TextField()
      submitted_at = models.DateTimeField(default=datetime.now, blank=True) 
      def __str__(self):
          return self.title
      class Meta:
         verbose_name_plural="Process"
