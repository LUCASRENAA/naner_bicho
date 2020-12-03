# Generated by Django 3.0.7 on 2020-07-27 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_evento_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='data',
        ),
        migrations.AddField(
            model_name='rodada',
            name='data',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
    ]