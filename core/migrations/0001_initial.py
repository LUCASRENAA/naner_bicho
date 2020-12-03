# Generated by Django 3.0.7 on 2020-06-19 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rodada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodada', models.IntegerField()),
                ('primeira_milhar', models.IntegerField()),
                ('segunda_milhar', models.IntegerField()),
                ('terceira_milhar', models.IntegerField()),
                ('quarta_milhar', models.IntegerField()),
                ('quinta_milhar', models.IntegerField()),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milhar', models.DecimalField(decimal_places=0, max_digits=4)),
                ('rodada', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19)),
                ('data_criacao', models.DateTimeField(auto_now=True)),
                ('conferir', models.DecimalField(decimal_places=2, max_digits=19)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'evento',
            },
        ),
        migrations.CreateModel(
            name='Dinheiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
