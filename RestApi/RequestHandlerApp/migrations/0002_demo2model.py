# Generated by Django 3.1.3 on 2020-11-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RequestHandlerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo2Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('collections', models.JSONField()),
            ],
        ),
    ]