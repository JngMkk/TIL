# Generated by Django 4.0.2 on 2022-02-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('mytitle', models.CharField(max_length=500)),
                ('mycontent', models.CharField(max_length=1000)),
                ('mydate', models.DateTimeField()),
            ],
        ),
    ]
