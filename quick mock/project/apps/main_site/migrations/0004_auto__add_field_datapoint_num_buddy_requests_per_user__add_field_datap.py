# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DataPoint.num_buddy_requests_per_user'
        db.add_column(u'main_site_datapoint', 'num_buddy_requests_per_user',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DataPoint.num_buddies_per_user'
        db.add_column(u'main_site_datapoint', 'num_buddies_per_user',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DataPoint.buddy_ratio'
        db.add_column(u'main_site_datapoint', 'buddy_ratio',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DataPoint.num_buddy_requests_per_user'
        db.delete_column(u'main_site_datapoint', 'num_buddy_requests_per_user')

        # Deleting field 'DataPoint.num_buddies_per_user'
        db.delete_column(u'main_site_datapoint', 'num_buddies_per_user')

        # Deleting field 'DataPoint.buddy_ratio'
        db.delete_column(u'main_site_datapoint', 'buddy_ratio')


    models = {
        u'main_site.datapoint': {
            'Meta': {'object_name': 'DataPoint'},
            'buddy_ratio': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_attended_one_event': ('django.db.models.fields.IntegerField', [], {}),
            'num_authenticated': ('django.db.models.fields.IntegerField', [], {}),
            'num_buddies_per_user': ('django.db.models.fields.IntegerField', [], {}),
            'num_buddy_requests_per_user': ('django.db.models.fields.IntegerField', [], {}),
            'num_filled_in_profile': ('django.db.models.fields.IntegerField', [], {}),
            'num_hit_home_page': ('django.db.models.fields.IntegerField', [], {}),
            'num_total_users': ('django.db.models.fields.IntegerField', [], {}),
            'num_with_one_buddy': ('django.db.models.fields.IntegerField', [], {}),
            'num_with_one_class': ('django.db.models.fields.IntegerField', [], {}),
            'recorded_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 5, 0, 0)'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main_site.milestone': {
            'Meta': {'ordering': "('recorded_at',)", 'object_name': 'Milestone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recorded_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 11, 5, 0, 0)'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main_site']