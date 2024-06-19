from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategorie")
    description = models.TextField(blank=True, null=True, verbose_name="Popisek")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nadpis")
    content = models.TextField(max_length=155, verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvořeno")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Upraveno")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategorie")
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name="Obrázek")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at', 'updated_at', 'title']
        verbose_name = 'Příspěvek'
        verbose_name_plural = 'Příspěvky'

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name="Příspěvek")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    content = models.TextField(max_length=155, verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvořeno")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Upraveno")

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    class Meta:
        ordering = ['created_at', 'updated_at']
        verbose_name = 'Komentář'
        verbose_name_plural = 'Komentáře'