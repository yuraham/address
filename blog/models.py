from django.db import models
from django.utils import timezone


class Address(models.Model):
    name = models.CharField(max_length=100)
    numb = models.IntegerField(max_length=10)
    numb_num = models.IntegerField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    open_addr = models.BooleanField(default=False)

    def addr(self):
        self.open_addr = True
        self.save()

    def __str__(self):
        return self.name
