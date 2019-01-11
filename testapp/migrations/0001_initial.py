# Generated by Django 2.0.3 on 2019-01-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateField()),
                ('movien', models.CharField(max_length=255)),
                ('hero', models.CharField(max_length=255)),
                ('heroin', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]