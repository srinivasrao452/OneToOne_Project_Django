# Generated by Django 3.0.5 on 2022-02-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OneToOne_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
