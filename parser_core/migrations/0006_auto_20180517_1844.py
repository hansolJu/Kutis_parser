# Generated by Django 2.0.5 on 2018-05-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_core', '0005_auto_20180517_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='hukbun',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]