# Generated by Django 4.2.4 on 2023-10-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='exibir',
            field=models.BooleanField(default=False),
        ),
    ]