from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('post_rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.author_user.comment_set.aggregate(commentRating=Sum('comment_rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.rating = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return f'{self.author_user}'


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    article = 'ar'
    news = 'ne'
    POST_TYPE = [
        (article, 'Статья'),
        (news,   'Новость'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE,verbose_name='Автор')
    post_types = models.CharField(max_length=2, choices=POST_TYPE, default=news, verbose_name='Тип')
    time_add_post = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    categories = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категория')
    title_post = models.CharField(max_length=128, verbose_name='Заголовок статьи')
    post_text = models.TextField(verbose_name='Текст статьи')
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post_text[0:124]+"..."

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    time_add_comment = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1


