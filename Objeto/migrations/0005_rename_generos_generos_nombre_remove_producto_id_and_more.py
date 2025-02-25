# Generated by Django 5.1.3 on 2024-11-26 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Objeto', '0004_alter_generos_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generos',
            old_name='generos',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AlterField(
            model_name='generos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='generos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='Objeto.generos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
