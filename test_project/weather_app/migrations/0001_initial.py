# Generated by Django 4.0.4 on 2022-04-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('weatherid', models.AutoField(db_column='weatherID', primary_key=True, serialize=False)),
                ('areano', models.BigIntegerField(db_column='areaNo')),
                ('si', models.CharField(max_length=30)),
                ('time', models.IntegerField()),
                ('condi', models.CharField(max_length=30)),
                ('isday', models.IntegerField(blank=True, db_column='isDay', null=True)),
                ('temp', models.IntegerField(blank=True, null=True)),
                ('humidity', models.IntegerField(blank=True, null=True)),
                ('rainratio', models.IntegerField(blank=True, db_column='rainRatio', null=True)),
                ('snowratio', models.IntegerField(blank=True, db_column='snowRatio', null=True)),
            ],
            options={
                'db_table': 'weather',
                'managed': False,
            },
        ),
    ]
