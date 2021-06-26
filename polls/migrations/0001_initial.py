# Generated by Django 3.1.7 on 2021-06-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=500)),
                ('option_one', models.CharField(max_length=50)),
                ('option_two', models.CharField(max_length=50)),
                ('option_three', models.CharField(blank=True, max_length=50)),
                ('option_four', models.CharField(blank=True, max_length=50)),
                ('option_one_count', models.PositiveIntegerField(default=0)),
                ('option_two_count', models.PositiveIntegerField(default=0)),
                ('option_three_count', models.PositiveIntegerField(default=0)),
                ('option_four_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
