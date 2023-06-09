# Generated by Django 4.1.1 on 2023-04-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='test',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(help_text="<a href='/bboard'>side<a>", max_length=50, verbose_name='Товар'),
        ),
    ]
