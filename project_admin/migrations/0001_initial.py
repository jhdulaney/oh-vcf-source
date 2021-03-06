# Generated by Django 2.0.1 on 2018-01-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(default='My Open Humans Project', max_length=50)),
                ('oh_client_id', models.CharField(default='replace-with-Open-Humans-Client-ID', max_length=40)),
                ('oh_client_secret', models.CharField(default='replace-with-Open-Humans-Client-secret', max_length=128)),
                ('project_description', models.TextField(default='This template demonstrates how you can run your own Open Humans data upload project.', help_text='Project description, displayed on the front page.')),
                ('oh_activity_page', models.TextField(default='https://www.openhumans.org/activity/your-project', help_text='The URL where we can find your project in Open Humans.')),
                ('file_description', models.TextField(default="This is an example file that doesn't have any meaning.", help_text='Description of the type of data being uploaded.')),
                ('file_tags', models.TextField(default='["tags", "are a good way to", "describe the files you are uploading"]', help_text='List of tags that describe file uploads, stored as a JSON-formatted array')),
                ('logo_url', models.TextField(blank=True, help_text='URL with logo of your project. If left blank, /static/default_logo.png will be used.')),
                ('more_info_url', models.TextField(blank=True, help_text='URL to find more information about your project.')),
                ('about', models.TextField(blank=True)),
                ('faq', models.TextField(blank=True)),
                ('homepage_text', models.TextField(blank=True)),
                ('overview', models.TextField(blank=True)),
                ('upload_description', models.TextField(blank=True)),
            ],
        ),
    ]
