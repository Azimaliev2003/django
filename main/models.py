from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='books/')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title