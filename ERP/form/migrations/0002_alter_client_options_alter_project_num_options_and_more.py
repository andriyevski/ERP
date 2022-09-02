# Generated by Django 4.1 on 2022-09-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'ID департаменту та клієнта', 'verbose_name_plural': 'ID департаменту та клієнтів'},
        ),
        migrations.AlterModelOptions(
            name='project_num',
            options={'verbose_name': 'Проект №', 'verbose_name_plural': 'Проект №'},
        ),
        migrations.AlterField(
            model_name='client',
            name='id_dep_client',
            field=models.TextField(max_length=100, verbose_name='ID департаменту та клієнта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name_client',
            field=models.TextField(max_length=100, verbose_name='ПІБ клиента'),
        ),
        migrations.AlterField(
            model_name='project_num',
            name='id',
            field=models.IntegerField(max_length=11, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='project_num',
            name='id_dep_client',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project_num',
            name='id_project',
            field=models.PositiveIntegerField(verbose_name='ID проекту'),
        ),
    ]