# Generated by Django 3.2.9 on 2021-12-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField()),
                ('bookname', models.CharField(max_length=20)),
                ('bookprice', models.IntegerField()),
                ('bookpublisher', models.CharField(max_length=50)),
            ],
        ),
    ]