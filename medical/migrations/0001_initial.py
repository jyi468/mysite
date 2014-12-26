# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('coverage_period_start', models.DateTimeField()),
                ('unit_of_analysis', models.CharField(max_length=200)),
                ('hd2_workflow_id', models.IntegerField()),
                ('agency', models.CharField(max_length=200)),
                ('bureau_code', models.CharField(max_length=200)),
                ('geographic_granularity', models.CharField(max_length=200)),
                ('technical_documentation', models.URLField()),
                ('collection_frequency', models.CharField(max_length=200)),
                ('agency_program_url', models.URLField()),
                ('date_updated', models.DateTimeField()),
                ('date_released', models.DateTimeField()),
                ('author_id', models.URLField()),
                ('migration_notes_json', models.TextField()),
                ('subject_area_1', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('groups', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('license_title', models.CharField(max_length=200)),
                ('maintainer', models.CharField(max_length=200)),
                ('private', models.BooleanField()),
                ('maintainer_email', models.EmailField(max_length=75)),
                ('num_tags', models.IntegerField()),
                ('metadata_created', models.DateTimeField()),
                ('license', models.CharField(max_length=200)),
                ('metadata_modified', models.DateTimeField()),
                ('author', models.CharField(max_length=200)),
                ('author_email', models.EmailField(max_length=75)),
                ('state', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('license_id', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('ratings_count', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('revision_id', models.CharField(max_length=200)),
                ('num_resources', models.IntegerField()),
                ('organization', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('isopen', models.BooleanField()),
                ('notes_rendered', models.TextField()),
                ('ckan_url', models.URLField()),
                ('notes', models.TextField()),
                ('owner_org', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('medical_info', models.ForeignKey(to='medical.MedicalInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('resource_group_id', models.CharField(max_length=200)),
                ('cache_last_updated', models.DateTimeField()),
                ('size', models.CharField(max_length=200)),
                ('last_modified', models.DateTimeField()),
                ('hash', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('format', models.CharField(max_length=200)),
                ('mimetype_inner', models.CharField(max_length=200)),
                ('cache_url', models.URLField()),
                ('webstore_url', models.URLField()),
                ('position', models.IntegerField()),
                ('resource_type', models.CharField(max_length=200)),
                ('ratings_count', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tags', models.CharField(max_length=200)),
                ('medical_info', models.ForeignKey(to='medical.MedicalInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrackingSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('total', models.IntegerField()),
                ('recent', models.IntegerField()),
                ('medical_info', models.ForeignKey(to='medical.MedicalInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='groups',
            name='tracking_summary',
            field=models.ForeignKey(to='medical.TrackingSummary'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extras',
            name='medical_info',
            field=models.ForeignKey(to='medical.MedicalInfo'),
            preserve_default=True,
        ),
    ]
