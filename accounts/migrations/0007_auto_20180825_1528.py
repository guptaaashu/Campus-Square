# Generated by Django 2.1 on 2018-08-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180825_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_no',
            field=models.CharField(max_length=10, verbose_name='Roll No'),
        ),
    ]
