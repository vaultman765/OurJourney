# Generated by Django 3.2.4 on 2021-06-11 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0005_alter_adventures_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventures',
            name='category',
            field=models.CharField(choices=[('Outdoors', 'OUTDOORS'), ('Indoors', 'INDOORS'), ('Trip', 'TRIP'), ('Other', 'OTHER')], default='Other', max_length=10),
        ),
        migrations.AlterField(
            model_name='adventures',
            name='subcategory',
            field=models.CharField(choices=[('Exercise', 'EXERCISE'), ('Relaxation', 'RELAX'), ('Romantic', 'ROMANTIC'), ('Fun', 'FUN'), ('Other', 'OTHER')], default='Other', max_length=10),
        ),
    ]