# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DataPoint'
        db.create_table(u'main_site_datapoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('recorded_at', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 28, 0, 0))),
            ('num_total_users', self.gf('django.db.models.fields.IntegerField')()),
            ('num_authenticated', self.gf('django.db.models.fields.IntegerField')()),
            ('num_filled_in_profile', self.gf('django.db.models.fields.IntegerField')()),
            ('num_hit_home_page', self.gf('django.db.models.fields.IntegerField')()),
            ('num_with_one_class', self.gf('django.db.models.fields.IntegerField')()),
            ('num_with_one_buddy', self.gf('django.db.models.fields.IntegerField')()),
            ('num_attended_one_event', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'main_site', ['DataPoint'])

        # Adding model 'Milestone'
        db.create_table(u'main_site_milestone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('recorded_at', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 28, 0, 0))),
        ))
        db.send_create_signal(u'main_site', ['Milestone'])


    def backwards(self, orm):
        # Deleting model 'DataPoint'
        db.delete_table(u'main_site_datapoint')

        # Deleting model 'Milestone'
        db.delete_table(u'main_site_milestone')


    models = {
        u'main_site.datapoint': {
            'Meta': {'object_name': 'DataPoint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_attended_one_event': ('django.db.models.fields.IntegerField', [], {}),
            'num_authenticated': ('django.db.models.fields.IntegerField', [], {}),
            'num_filled_in_profile': ('django.db.models.fields.IntegerField', [], {}),
            'num_hit_home_page': ('django.db.models.fields.IntegerField', [], {}),
            'num_total_users': ('django.db.models.fields.IntegerField', [], {}),
            'num_with_one_buddy': ('django.db.models.fields.IntegerField', [], {}),
            'num_with_one_class': ('django.db.models.fields.IntegerField', [], {}),
            'recorded_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 28, 0, 0)'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main_site.milestone': {
            'Meta': {'ordering': "('recorded_at',)", 'object_name': 'Milestone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recorded_at': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 28, 0, 0)'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main_site']