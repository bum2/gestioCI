# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Concept'
        db.create_table(u'General_concept', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['General.Concept'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'General', ['Concept'])

        # Adding model 'Type'
        db.create_table(u'General_type', (
            ('concept', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Concept'], unique=True, primary_key=True)),
            ('clas', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'General', ['Type'])

        # Adding model 'Being_Type'
        db.create_table(u'General_being_type', (
            ('typ', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Being_Type'])

        # Adding model 'Human'
        db.create_table(u'General_human', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('being_type', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Being_Type'], null=True, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('dead_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=40, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal(u'General', ['Human'])

        # Adding M2M table for field jobs on 'Human'
        m2m_table_name = db.shorten_name(u'General_human_jobs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('human', models.ForeignKey(orm[u'General.human'], null=False)),
            ('job', models.ForeignKey(orm[u'General.job'], null=False))
        ))
        db.create_unique(m2m_table_name, ['human_id', 'job_id'])

        # Adding M2M table for field addresses on 'Human'
        m2m_table_name = db.shorten_name(u'General_human_addresses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('human', models.ForeignKey(orm[u'General.human'], null=False)),
            ('address', models.ForeignKey(orm[u'General.address'], null=False))
        ))
        db.create_unique(m2m_table_name, ['human_id', 'address_id'])

        # Adding model 'Person'
        db.create_table(u'General_person', (
            ('human', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Human'], unique=True, primary_key=True)),
            ('surnames', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('id_card', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('email2', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('nickname2', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'General', ['Person'])

        # Adding M2M table for field projects on 'Person'
        m2m_table_name = db.shorten_name(u'General_person_projects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'General.person'], null=False)),
            ('project', models.ForeignKey(orm[u'General.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'project_id'])

        # Adding model 'Project'
        db.create_table(u'General_project', (
            ('human', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Human'], unique=True, primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='subprojects', null=True, to=orm['General.Project'])),
            ('socialweb', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email2', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'General', ['Project'])

        # Adding M2M table for field ref_members on 'Project'
        m2m_table_name = db.shorten_name(u'General_project_ref_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'General.project'], null=False)),
            ('person', models.ForeignKey(orm[u'General.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'person_id'])

        # Adding model 'Project_Type'
        db.create_table(u'General_project_type', (
            ('being_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Being_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Project_Type'])

        # Adding model 'Company'
        db.create_table(u'General_company', (
            ('human', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Human'], unique=True, primary_key=True)),
            ('legal_name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('vat_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'General', ['Company'])

        # Adding M2M table for field ref_members on 'Company'
        m2m_table_name = db.shorten_name(u'General_company_ref_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'General.company'], null=False)),
            ('person', models.ForeignKey(orm[u'General.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'person_id'])

        # Adding model 'Company_Type'
        db.create_table(u'General_company_type', (
            ('being_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Being_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Company_Type'])

        # Adding model 'Art'
        db.create_table(u'General_art', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('verb', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('gerund', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['General.Art'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'General', ['Art'])

        # Adding model 'Relation'
        db.create_table(u'General_relation', (
            ('art', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Art'], unique=True, primary_key=True)),
            ('clas', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'General', ['Relation'])

        # Adding model 'Job'
        db.create_table(u'General_job', (
            ('art', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Art'], unique=True, primary_key=True)),
            ('clas', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'General', ['Job'])

        # Adding model 'Space_Type'
        db.create_table(u'General_space_type', (
            ('typ', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Space_Type'])

        # Adding model 'Address'
        db.create_table(u'General_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('space_type', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Space_Type'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('p_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('postalcode', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('region', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='addresses', null=True, to=orm['General.Region'])),
            ('m2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'General', ['Address'])

        # Adding model 'Address_Type'
        db.create_table(u'General_address_type', (
            (u'type_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Type'], unique=True)),
            ('space_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Space_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Address_Type'])

        # Adding model 'Region'
        db.create_table(u'General_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('space_type', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Space_Type'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['General.Region'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'General', ['Region'])

        # Adding model 'Region_Type'
        db.create_table(u'General_region_type', (
            (u'type_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Type'], unique=True)),
            ('space_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Space_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Region_Type'])

        # Adding model 'Artwork_Type'
        db.create_table(u'General_artwork_type', (
            ('typ', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Artwork_Type'])

        # Adding model 'Nonmaterial'
        db.create_table(u'General_nonmaterial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nonmaterial_type', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Nonmaterial_Type'], null=True, blank=True)),
        ))
        db.send_create_signal(u'General', ['Nonmaterial'])

        # Adding model 'Nonmaterial_Type'
        db.create_table(u'General_nonmaterial_type', (
            ('artwork_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Artwork_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Nonmaterial_Type'])

        # Adding model 'Material'
        db.create_table(u'General_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('material_type', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Material_Type'], null=True, blank=True)),
        ))
        db.send_create_signal(u'General', ['Material'])

        # Adding model 'Material_Type'
        db.create_table(u'General_material_type', (
            ('artwork_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Artwork_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Material_Type'])

        # Adding model 'Record'
        db.create_table(u'General_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('record_type', self.gf('mptt.fields.TreeForeignKey')(to=orm['General.Record_Type'], null=True, blank=True)),
        ))
        db.send_create_signal(u'General', ['Record'])

        # Adding model 'Record_Type'
        db.create_table(u'General_record_type', (
            ('artwork_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Artwork_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Record_Type'])

        # Adding model 'Currency'
        db.create_table(u'General_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('currency_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Currency_Type'], null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Region'], null=True, blank=True)),
        ))
        db.send_create_signal(u'General', ['Currency'])

        # Adding model 'Currency_Type'
        db.create_table(u'General_currency_type', (
            ('artwork_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Artwork_Type'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'General', ['Currency_Type'])

        # Adding model 'CurrencyRatio'
        db.create_table(u'General_currencyratio', (
            ('record', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Record'], unique=True, primary_key=True)),
            ('in_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratio_in', to=orm['General.Currency'])),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('out_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ratio_out', to=orm['General.Currency'])),
        ))
        db.send_create_signal(u'General', ['CurrencyRatio'])

        # Adding model 'AccountCes'
        db.create_table(u'General_accountces', (
            ('record', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Record'], unique=True, primary_key=True)),
            ('human', self.gf('django.db.models.fields.related.ForeignKey')(related_name='accountsCes', to=orm['General.Human'])),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Project'], null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Currency'], null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'General', ['AccountCes'])

        # Adding model 'AccountBank'
        db.create_table(u'General_accountbank', (
            ('record', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['General.Record'], unique=True, primary_key=True)),
            ('human', self.gf('django.db.models.fields.related.ForeignKey')(related_name='accountsBank', to=orm['General.Human'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Company'], null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['General.Currency'], null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'General', ['AccountBank'])


    def backwards(self, orm):
        # Deleting model 'Concept'
        db.delete_table(u'General_concept')

        # Deleting model 'Type'
        db.delete_table(u'General_type')

        # Deleting model 'Being_Type'
        db.delete_table(u'General_being_type')

        # Deleting model 'Human'
        db.delete_table(u'General_human')

        # Removing M2M table for field jobs on 'Human'
        db.delete_table(db.shorten_name(u'General_human_jobs'))

        # Removing M2M table for field addresses on 'Human'
        db.delete_table(db.shorten_name(u'General_human_addresses'))

        # Deleting model 'Person'
        db.delete_table(u'General_person')

        # Removing M2M table for field projects on 'Person'
        db.delete_table(db.shorten_name(u'General_person_projects'))

        # Deleting model 'Project'
        db.delete_table(u'General_project')

        # Removing M2M table for field ref_members on 'Project'
        db.delete_table(db.shorten_name(u'General_project_ref_members'))

        # Deleting model 'Project_Type'
        db.delete_table(u'General_project_type')

        # Deleting model 'Company'
        db.delete_table(u'General_company')

        # Removing M2M table for field ref_members on 'Company'
        db.delete_table(db.shorten_name(u'General_company_ref_members'))

        # Deleting model 'Company_Type'
        db.delete_table(u'General_company_type')

        # Deleting model 'Art'
        db.delete_table(u'General_art')

        # Deleting model 'Relation'
        db.delete_table(u'General_relation')

        # Deleting model 'Job'
        db.delete_table(u'General_job')

        # Deleting model 'Space_Type'
        db.delete_table(u'General_space_type')

        # Deleting model 'Address'
        db.delete_table(u'General_address')

        # Deleting model 'Address_Type'
        db.delete_table(u'General_address_type')

        # Deleting model 'Region'
        db.delete_table(u'General_region')

        # Deleting model 'Region_Type'
        db.delete_table(u'General_region_type')

        # Deleting model 'Artwork_Type'
        db.delete_table(u'General_artwork_type')

        # Deleting model 'Nonmaterial'
        db.delete_table(u'General_nonmaterial')

        # Deleting model 'Nonmaterial_Type'
        db.delete_table(u'General_nonmaterial_type')

        # Deleting model 'Material'
        db.delete_table(u'General_material')

        # Deleting model 'Material_Type'
        db.delete_table(u'General_material_type')

        # Deleting model 'Record'
        db.delete_table(u'General_record')

        # Deleting model 'Record_Type'
        db.delete_table(u'General_record_type')

        # Deleting model 'Currency'
        db.delete_table(u'General_currency')

        # Deleting model 'Currency_Type'
        db.delete_table(u'General_currency_type')

        # Deleting model 'CurrencyRatio'
        db.delete_table(u'General_currencyratio')

        # Deleting model 'AccountCes'
        db.delete_table(u'General_accountces')

        # Deleting model 'AccountBank'
        db.delete_table(u'General_accountbank')


    models = {
        u'General.accountbank': {
            'Meta': {'object_name': 'AccountBank', '_ormbases': [u'General.Record']},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Company']", 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Currency']", 'null': 'True', 'blank': 'True'}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountsBank'", 'to': u"orm['General.Human']"}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Record']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.accountces': {
            'Meta': {'object_name': 'AccountCes', '_ormbases': [u'General.Record']},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Currency']", 'null': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Project']", 'null': 'True', 'blank': 'True'}),
            'human': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountsCes'", 'to': u"orm['General.Human']"}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Record']", 'unique': 'True', 'primary_key': 'True'})
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
            'Meta': {'object_name': 'Address_Type', '_ormbases': [u'General.Type']},
            'space_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Space_Type']", 'unique': 'True', 'primary_key': 'True'}),
            u'type_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Type']", 'unique': 'True'})
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
        u'General.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'currency_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Currency_Type']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['General.Region']", 'null': 'True', 'blank': 'True'})
        },
        u'General.currency_type': {
            'Meta': {'object_name': 'Currency_Type', '_ormbases': [u'General.Artwork_Type']},
            'artwork_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Artwork_Type']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'General.currencyratio': {
            'Meta': {'object_name': 'CurrencyRatio', '_ormbases': [u'General.Record']},
            'in_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratio_in'", 'to': u"orm['General.Currency']"}),
            'out_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratio_out'", 'to': u"orm['General.Currency']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'record': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Record']", 'unique': 'True', 'primary_key': 'True'})
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
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['General.Project']", 'null': 'True', 'blank': 'True'}),
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
            'Meta': {'object_name': 'Region_Type', '_ormbases': [u'General.Type']},
            'space_type': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Space_Type']", 'unique': 'True', 'primary_key': 'True'}),
            u'type_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['General.Type']", 'unique': 'True'})
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
        }
    }

    complete_apps = ['General']