# Generated by Django 4.2.9 on 2024-01-24 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_remove_review_film_title_review_film_review_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.film'),
        ),
    ]
