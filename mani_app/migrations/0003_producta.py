# Generated by Django 3.1.2 on 2020-11-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mani_app', '0002_auto_20201107_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
