# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0019_auto_20180212_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djcms_demo_block', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('content', djangocms_text_ckeditor.fields.HTMLField(blank=True, verbose_name='Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
