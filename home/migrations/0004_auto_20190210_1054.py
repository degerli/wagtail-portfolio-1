# Generated by Django 2.1.5 on 2019-02-10 10:54

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_portfoliosettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='intro_left',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_right',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
