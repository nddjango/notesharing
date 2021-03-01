# Generated by Django 3.1.5 on 2021-01-25 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20210120_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('p_file', models.FileField(upload_to='upload')),
                ('cmnt', models.CharField(max_length=500)),
            ],
        ),
    ]
