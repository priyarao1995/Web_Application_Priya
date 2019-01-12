# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Process
from django.utils import timezone

# Create your tests here.

class ProcessTest(TestCase):
      
      def create(self, title="only test", body=" this is only a test"):
           return Process.objects.create(title=title, feedback=body, submitted_at=timezone.now())
      def test_Process_creation(self):
          w=self.create()
          self.assertTrue(isinstance(w, Process))
          self.assertEqual(w.__unicode__(), w.title)  
