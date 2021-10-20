from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import *
class Bank(models.Model):
    user = models.CharField(max_length=200)
    text = models.TextField()
    translation = models.TextField()
    assessment_correct = models.TextField()
    assessment_counter = models.TextField()
    assessment_temp = models.TextField()
    assessment_type = models.TextField()
    assessment_count = models.TextField()
    assessment_results = models.TextField()
    def publish(self):
        self.save()

    def __str__(self):
        return self.user



