# Generated by Django 4.2.3 on 2023-07-31 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_article_author_alter_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='ENTER A VALID TITLE', max_length=50, unique=True),
        ),
    ]
