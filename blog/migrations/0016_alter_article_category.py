# Generated by Django 4.2.3 on 2023-07-31 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_category_remove_article_pub_date_alter_article_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(null=True, to='blog.category'),
        ),
    ]
