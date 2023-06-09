# Generated by Django 4.2 on 2023-06-15 19:02

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestToSpeech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('novel_name', models.CharField(max_length=100)),
                ('chapter_name', models.FileField(upload_to='')),
                ('chapter_content', models.TextField()),
                ('chapter_url', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
