# Generated by Django 4.2.8 on 2024-08-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]