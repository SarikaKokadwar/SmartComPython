# Generated by Django 5.1.1 on 2024-10-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartcompythondemo', '0002_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
