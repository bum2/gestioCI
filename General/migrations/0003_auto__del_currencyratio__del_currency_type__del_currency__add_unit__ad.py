# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CurrencyRatio'
        db.delete_table(u'General_currencyratio')

        # Deleting model 'Currency_Type'
        db.delete_table(u'General_currency_type')

        # Deleting model 'Currency'
        db.delete_table(u'General_currency')

        # Adding model 'Unit'
        db.create_table(u'General_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('unit_type', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Unit_Type'], null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('rel_region', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Region'], null=True, blank=True)),
            ('rel_human', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Human'], null=True, blank=True)),
        ))
        db.send_create_signal(u'General', ['Unit'])

        # Adding model 'Unit_Type'
        db.create_table(u'General_unit_type', (
            ('artwork_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Artwork_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Unit_Type'])

        # Adding model 'UnitRatio'
        db.create_table(u'General_unitratio', (
            ('record', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Record'], unique=True, primary_key=True)),
            ('in_unit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratio_in', to=orm['General.Unit'])),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('out_unit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratio_out', to=orm['General.Unit'])),
        ))
        db.send_create_signal(u'General', ['UnitRatio'])

        # Deleting field 'AccountCes.currency'
        db.delete_column(u'General_accountces', 'currency_id')

        # Adding field 'AccountCes.unit'
        db.add_column(u'General_accountces', 'unit',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Unit'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'AccountBank.currency'
        db.delete_column(u'General_accountbank', 'currency_id')

        # Adding field 'AccountBank.unit'
        db.add_column(u'General_accountbank', 'unit',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Unit'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'CurrencyRatio'
        db.create_table(u'General_currencyratio', (
            ('record', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Record'], unique=True, primary_key=True)),
            ('in_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratio_in', to=orm['General.Currency'])),
            ('out_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratio_out', to=orm['General.Currency'])),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
        ))
        db.send_create_signal(u'General', ['CurrencyRatio'])

        # Adding model 'Currency_Type'
        db.create_table(u'General_currency_type', (
            ('artwork_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Artwork_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Currency_Type'])

        # Adding model 'Currency'
        db.create_table(u'General_currency', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Region'], null=True, blank=True)),
            ('currency_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Currency_Type'], null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Currency'])

        # Deleting model 'Unit'
        db.delete_table(u'General_unit')

        # Deleting model 'Unit_Type'
        db.delete_table(u'General_unit_type')

        # Deleting model 'UnitRatio'
        db.delete_table(u'General_unitratio')

        # Adding field 'AccountCes.currency'
        db.add_column(u'General_accountces', 'currency',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Currency'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'AccountCes.unit'
        db.delete_column(u'General_accountces', 'unit_id')

        # Adding field 'AccountBank.currency'
        db.add_column(u'General_accountbank', 'currency',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Currency'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'AccountBank.unit'
        db.delete_column(u'General_accountbank', 'unit_id')


    models = {
        u'General.accountbank': {
            'Meta': {'object_name': 'AccountBank', '_ormbases': [u'General.Record']},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Company']", 'null': 'True', 'blank': 'True'}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountsBank'", 'to': u"orm['General.Human']"}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Record']", 'unique': 'True', 'primary_key': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Unit']", 'null': 'True', 'blank': 'True'})
        },
        u'General.accountces': {
            'Meta': {'object_name': 'AccountCes', '_ormbases': [u'General.Record']},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Project']", 'null': 'True', 'blank': 'True'}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountsCes'", 'to': u"orm['General.Human']"}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Record']", 'unique': 'True', 'primary_key': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Unit']", 'null': 'True', 'blank': 'True'})
        },
        u'General.address': {
            'Meta': {'object_name': 'Address'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'm2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'p_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'postalcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'region': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'addresses'", 'null': 'True', 'to': u"orm['General.Region']"}),
            'space_type': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Space_Type']", 'null': 'True', 'blank': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'General.address_type': {
            'Meta': {'object_name': 'Address_Type', '_ormbases': [u'General.Space_Type']},
            'space_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Space_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.art': {
            'Meta': {'object_name': 'Art'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gerund': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['General.Art']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'General.artwork_type': {
            'Meta': {'object_name': 'Artwork_Type', '_ormbases': [u'General.Type']},
            'typ': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.being_type': {
            'Meta': {'object_name': 'Being_Type', '_ormbases': [u'General.Type']},
            'typ': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.company': {
            'Meta': {'object_name': 'Company', '_ormbases': [u'General.Human']},
            'human': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Human']", 'unique': 'True', 'primary_key': 'True'}),
            'legal_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'ref_members': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ref_companies'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['General.Person']"}),
            'vat_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'General.company_type': {
            'Meta': {'object_name': 'Company_Type', '_ormbases': [u'General.Being_Type']},
            'being_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Being_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.concept': {
            'Meta': {'object_name': 'Concept'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '30'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['General.Concept']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'General.human': {
            'Meta': {'object_name': 'Human'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['General.Address']", 'null': 'True', 'blank': 'True'}),
            'being_type': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Being_Type']", 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dead_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '40', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['General.Job']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        u'General.job': {
            'Meta': {'object_name': 'Job', '_ormbases': [u'General.Art']},
            'art': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Art']", 'unique': 'True', 'primary_key': 'True'}),
            'clas': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'General.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_type': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Material_Type']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'General.material_type': {
            'Meta': {'object_name': 'Material_Type', '_ormbases': [u'General.Artwork_Type']},
            'artwork_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Artwork_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.nonmaterial': {
            'Meta': {'object_name': 'Nonmaterial'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nonmaterial_type': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Nonmaterial_Type']", 'null': 'True', 'blank': 'True'})
        },
        u'General.nonmaterial_type': {
            'Meta': {'object_name': 'Nonmaterial_Type', '_ormbases': [u'General.Artwork_Type']},
            'artwork_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Artwork_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.person': {
            'Meta': {'object_name': 'Person', '_ormbases': [u'General.Human']},
            'email2': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'human': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Human']", 'unique': 'True', 'primary_key': 'True'}),
            'id_card': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'nickname2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'projects': ('mptt.fields.TreeManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['General.Project']", 'null': 'True', 'blank': 'True'}),
            'surnames': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        },
        u'General.project': {
            'Meta': {'object_name': 'Project', '_ormbases': [u'General.Human']},
            'email2': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'human': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Human']", 'unique': 'True', 'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'subprojects'", 'null': 'True', 'to': u"orm['General.Project']"}),
            'ref_members': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ref_projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['General.Person']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'socialweb': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'General.project_type': {
            'Meta': {'object_name': 'Project_Type', '_ormbases': [u'General.Being_Type']},
            'being_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Being_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.record': {
            'Meta': {'object_name': 'Record'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'record_type': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Record_Type']", 'null': 'True', 'blank': 'True'})
        },
        u'General.record_type': {
            'Meta': {'object_name': 'Record_Type', '_ormbases': [u'General.Artwork_Type']},
            'artwork_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Artwork_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.region': {
            'Meta': {'object_name': 'Region'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'longitude': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['General.Region']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'space_type': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Space_Type']", 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'General.region_type': {
            'Meta': {'object_name': 'Region_Type', '_ormbases': [u'General.Space_Type']},
            'space_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Space_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.relation': {
            'Meta': {'object_name': 'Relation', '_ormbases': [u'General.Art']},
            'art': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Art']", 'unique': 'True', 'primary_key': 'True'}),
            'clas': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'General.space_type': {
            'Meta': {'object_name': 'Space_Type', '_ormbases': [u'General.Type']},
            'typ': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.type': {
            'Meta': {'object_name': 'Type', '_ormbases': [u'General.Concept']},
            'clas': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'concept': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Concept']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.unit': {
            'Meta': {'object_name': 'Unit'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rel_human': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Human']", 'null': 'True', 'blank': 'True'}),
            'rel_region': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Region']", 'null': 'True', 'blank': 'True'}),
            'unit_type': ('mptt.fields.TreeForeignKey', [], {'to': u"orm['General.Unit_Type']", 'null': 'True', 'blank': 'True'})
        },
        u'General.unit_type': {
            'Meta': {'object_name': 'Unit_Type', '_ormbases': [u'General.Artwork_Type']},
            'artwork_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Artwork_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.unitratio': {
            'Meta': {'object_name': 'UnitRatio', '_ormbases': [u'General.Record']},
            'in_unit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratio_in'", 'to': u"orm['General.Unit']"}),
            'out_unit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratio_out'", 'to': u"orm['General.Unit']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'record': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Record']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['General']