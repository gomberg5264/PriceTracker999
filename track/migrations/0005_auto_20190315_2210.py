# Generated by Django 2.1.7 on 2019-03-15 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0004_auto_20190315_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='url',
            new_name='myurl',
        ),
    ]
