from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    contents = models.TextField(null = True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    visit_count = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.visit_count = self.visit_count + 1
        self.save()

class RecordReview(models.Model):
    record = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null = True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.comment)