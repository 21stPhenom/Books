from django.db import models

# Create your models here.
plans = (
    ('level_1', 'Free'),
    ('level_2', 'Advanced'),
    ('level_3', 'Pro'),
    ('level_4', 'Premium'),
)

class Book(models.Model):
    title = models.CharField(verbose_name='Book title', max_length=500)
    author = models.CharField(verbose_name='Book author', max_length = 200)
    date_released = models.DateTimeField(auto_now_add=True)
    plan = models.CharField(verbose_name='Plan', choices=plans, max_length=7)

    def __str__(self):
        return f"'{self.title}' by '{self.author}'"
    
    