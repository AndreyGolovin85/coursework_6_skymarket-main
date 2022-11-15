# Generated by Django 4.1.3 on 2022-11-15 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ad",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
            },
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.AddField(
            model_name="ad",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ad",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="ad",
            name="description",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ad",
            name="price",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ad",
            name="title",
            field=models.CharField(
                default=1, max_length=60, verbose_name="Название товара"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comment",
            name="ad",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="text",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
