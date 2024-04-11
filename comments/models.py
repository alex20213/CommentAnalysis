from django.db import models

class Comment(models.Model):
    label = models.BooleanField(default=False)
    text = models.TextField()
    created_at = models.CharField(max_length=100, default='')
    note = models.IntegerField(blank=True, null=True)
    published_on = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.text