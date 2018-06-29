from django.db import models
from django.utils import timezone


class Address(models.Model):
    name = models.CharField(max_length=100)
    numb = models.IntegerField()
    numb_num = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    open_addr = models.BooleanField(default=True)

    def openaddr(self):
        self.open_addr = False
        self.save()

    def noopenaddr(self):
        self.open_addr = True
        self.save()

    def __str__(self):
        return self.name

