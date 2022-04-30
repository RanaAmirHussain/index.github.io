# Generated by Django 3.1.2 on 2022-04-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]