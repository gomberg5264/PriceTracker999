# Generated by Django 2.1.7 on 2019-03-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0006_auto_20190315_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_src',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
