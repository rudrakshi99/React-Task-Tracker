from django.db import models

class Todo(models.Model):
    text = models.TextField()
    day = models.DateField()
    reminder = models.BooleanField(default=False)

    class Meta:
        ordering = ('-day',)
    
    def __str__(self):
        return self.day.strftime('%Y-%m-%d') 