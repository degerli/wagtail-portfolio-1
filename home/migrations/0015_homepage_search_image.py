# Generated by Django 2.1.7 on 2019-02-18 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0014_auto_20190218_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image'),
        ),
    ]
