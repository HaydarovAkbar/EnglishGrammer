from django.db import models


# Create your models here.

class Grammer(models.Model):
    text = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    example = models.CharField(max_length=250, null=True)
    date_of_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['date_of_created', 'example', 'text'])
        ]
        db_table = 'Grammer'
        ordering = ['-id']
