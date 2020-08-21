from django.db import models
from account.models import Profile

class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='receiver', on_delete=models.CASCADE)
    text = models.CharField(max_length=4096)
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.sender} to {self.receiver}: {self.text}'


    