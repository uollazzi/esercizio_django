from django.db import models

# Create your models here.
class Log(models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
    