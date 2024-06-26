# Generated by Django 4.2.13 on 2024-05-26 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='post',
            name='continent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.continent', verbose_name='Материк'),
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.country', verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='post',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.region', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='posts.tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.region', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
        migrations.AddField(
            model_name='city',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.area', verbose_name='Область'),
        ),
        migrations.AddField(
            model_name='area',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.country', verbose_name='Страна'),
        ),
    ]
