# Generated by Django 2.0.1 on 2018-01-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0002_auto_20180111_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='descricao',
            field=models.CharField(default='', max_length=250, verbose_name='Descrição'),
            preserve_default=False,
        ),
    ]
