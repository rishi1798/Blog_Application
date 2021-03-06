# Generated by Django 4.0.1 on 2022-01-18 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0006_alter_blog_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='update_date',
            field=models.DateField(null=True),
        ),
    ]
