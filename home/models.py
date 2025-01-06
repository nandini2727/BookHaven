from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


