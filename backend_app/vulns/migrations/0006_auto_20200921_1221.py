# Generated by Django 3.0.9 on 2020-09-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0005_auto_20200728_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exploitmetadata',
            name='trust_level',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='historicalexploitmetadata',
            name='trust_level',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='historicalorgexploitmetadata',
            name='trust_level',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='historicalorgthreatmetadata',
            name='trust_level',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='historicalthreatmetadata',
            name='trust_level',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='orgexploitmetadata',
            name='trust_level',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='orgthreatmetadata',
            name='trust_level',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='threatmetadata',
            name='trust_level',
            field=models.CharField(choices=[('unknown', 'Unknown'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='unknown', max_length=20),
        ),
    ]