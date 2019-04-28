from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=120, blank=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "post"
        ordering = ('created_at',)
    
    def __str__(self):
        return f'{self.id} - {self.content} BY {self.author}'


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.email}'