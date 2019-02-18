# Generated by Django 2.1.5 on 2019-02-10 15:17

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20190210_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologyUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.RemoveField(
            model_name='individualprojectspage',
            name='category2',
        ),
        migrations.RemoveField(
            model_name='individualprojectspage',
            name='technology_used',
        ),
        migrations.AddField(
            model_name='individualprojectspage',
            name='technologies',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='projects.TechnologyUsed'),
        ),
    ]
