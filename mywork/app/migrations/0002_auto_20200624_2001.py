# Generated by Django 2.2.6 on 2020-06-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.IntegerField(default=False, unique=True)),
                ('email', models.EmailField(max_length=33)),
                ('business_profile', models.CharField(max_length=244)),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='ConsaltantProfile',
        ),
    ]