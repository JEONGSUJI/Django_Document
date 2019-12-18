from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    shirt_size = models.CharField(
        '셔츠 사이즈',
        max_length=1, choices=SHIRT_SIZES, help_text="셔츠 사이즈")
    first_name = models.CharField('이름', max_length=30)
    last_name = models.CharField('성', max_length=30)