# Generated by Django 3.1.1 on 2020-10-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('blog', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='comment_section',
        ),
    ]
