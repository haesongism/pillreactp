# Generated by Django 4.1.7 on 2023-03-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('views', models.IntegerField()),
                ('title', models.CharField(max_length=140)),
                ('content', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
