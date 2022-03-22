# Generated by Django 4.0.2 on 2022-03-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(through='news.PostCategory', to='news.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_types',
            field=models.CharField(choices=[('ar', 'Статья'), ('ne', 'Новость')], default='ne', max_length=2, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_add_post',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_post',
            field=models.CharField(max_length=128, verbose_name='Заголовок статьи'),
        ),
    ]