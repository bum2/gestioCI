#encoding=utf-8

from django.contrib import admin
from django.forms.extras import widgets

from django.utils.translation import ugettext as _

from mptt.admin import MPTTModelAdmin
from mptt.fields import TreeForeignKey, TreeManyToManyField
#from mptt.forms import MPTTAdminForm, TreeNodeChoiceField

from General.models import *  # Tree, Human, Adress, Region, Concept, Type, Being_Type

#class CustomMPTTModelAdmin(MPTTModelAdmin):
    # speficfy pixel amount for this ModelAdmin only:
    #fields = ['name']
#    mptt_level_indent = 20
#    mptt_indent_field = "name"


from itertools import chain
from django import forms
from django.conf import settings
from django.contrib.admin import widgets
from django.utils.encoding import smart_unicode, force_unicode
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape

class addressInline(admin.StackedInline):
    model = rel_Human_Addresses
    extra = 0
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('address','relation'),)
      }),
    )

class jobInline(admin.StackedInline):
    model = rel_Human_Jobs
    extra = 0
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('job','relation'),)
      }),
    )

class recordInline(admin.StackedInline):
    model = rel_Human_Records
    extra = 0
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('record','relation'),)
      }),
    )

class regionInline(admin.StackedInline):
    model = rel_Human_Regions
    extra = 0
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('region','relation'),)
      }),
    )

class materialInline(admin.StackedInline):
    model = rel_Human_Materials
    extra = 0
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('material','relation'),)
      }),
    )

class nonmaterialInline(admin.StackedInline):
    model = rel_Human_Nonmaterials
    extra = 0
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('nonmaterial','relation'),)
      }),
    )

class personInline(admin.StackedInline):
    model = rel_Human_Persons
    fk_name = 'human'
    extra = 0
    raw_id_fields = ('person',)
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('person','relation'),)
      }),
    )

class projectInline(admin.StackedInline):
    model = rel_Human_Projects
    fk_name = 'human'
    extra = 0
    raw_id_fields = ('project',)
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('project','relation'),)
      }),
    )

class companyInline(admin.StackedInline):
    model = rel_Human_Companies
    fk_name = 'human'
    extra = 0
    raw_id_fields = ('company',)
    fieldsets = (
      (' ', {
        'classes': ('collapse',),
        'fields': (('company','relation'),)
      }),
    )

class accountCesInline(admin.StackedInline):
  model = AccountCes
  extra = 0
  fk_name = 'human'
  fieldsets = (
    (' ', {
      'classes': ('collapse',),
      'fields': (
        ('record_type', 'entity', 'unit', 'code', 'number'),
      )
    }),
  )

class accountBankInline(admin.StackedInline):
  model = AccountBank
  extra = 0
  fk_name = 'human'
  fieldsets = (
    (' ', {
      'classes': ('collapse',),
      'fields': (
        ('record_type', 'company', 'unit', 'code', 'number'),
      )
    }),
  )

class accountCryptoInline(admin.StackedInline):
  model = AccountCrypto
  extra = 0
  fk_name = 'human'
  fieldsets = (
    (' ', {
      'classes': ('collapse',),
      'fields': (
        ('record_type', 'unit', 'number'),
      )
    }),
  )

class assetInline(admin.StackedInline):
  model = Asset
  extra = 0
  fk_name = 'human'
  fieldsets = (
    (' ', {
      'classes': ('collapse',),
      'fields': (
        ('name', 'material_type', 'description', 'reciprocity', 'address'),
      )
    }),
  )



class ProjectAdmin(MPTTModelAdmin): # admin.ModelAdmin):
  #class Media:
  #  js = ('mselect-to-mcheckbox.js', 'jquery-ui-1.10.2.custom.js',)
  #  css = {
  #    'all': ('css/mselect-to-mcheckbox.css',)
  #  }
  #list_select_related = True
  #select_related = ['accountsCes']
  #project_type = Being_Type.objects.all()

  list_display = ['name', 'nickname', 'project_type', '_is_collective']#, 'ref_persons']
  list_filter = ('project_type',)
  search_fields = ('name', 'nickname', 'project_type')

  def ref_persons(self, obj):
    return obj.project.get_ref_persons
  ref_persons.admin_order_field = 'project__get_ref_persons'
  #ref_persons.list = []
  #ref_persons.allow_tags = True

  fieldsets = (
    (None, {
      'fields':(('name', 'nickname'),
                ('website', 'socialweb'),
                ('project_type', 'parent'),
                ('email', 'email2', 'telephone'),
                ('ecommerce'))#, 'accounts'))
    }),
    #(_(u"Comptes"), {
    #  'classes': ('collapse',),
    #  'fields': ('accountsCes',)
    #}),
    #(_(u"Membres de referencia"), {
    #  'classes': ('collapse',),
    #  'fields':('ref_persons',),
    #}),
    #(_(u"Actius"), {
    #  'classes': ('collapse',),
    #  'fields':('assets',),
    #}),
    (_(u"Dates inici/fi"), {
      'classes': ('collapse',),
      'fields': (('birth_date', 'death_date'),)
    })
  )
  #filter_horizontal = ('ref_members',) # 'arts',) # 'addresses',)
  #filter_horizontal = ('accounts',) # 'arts',) # 'addresses',)

  inlines = [
    addressInline,
    jobInline,

    accountCesInline,
    accountBankInline,
    accountCryptoInline,

    personInline,
    projectInline,
    companyInline,

    assetInline,
    #regionInline,
    materialInline,
    nonmaterialInline,
    recordInline,
  ]

  #def is_collective(self, profile):
  #  return profile.project.is_collective
  #collective = admin_field('project__is_collective')
  #collective.admin_field = 'project__is_collective'


class PersonAdmin(admin.ModelAdmin):
  #class Media:
  #  js = ('mselect-to-mcheckbox.js', 'jquery-ui-1.10.2.custom.js',)
  #  css = {
  #    'all': ('css/mselect-to-mcheckbox.css',)
  #  }

  list_display = ['name', 'nickname', 'email']
  search_fields = ('name', 'nickname', 'email')

  fieldsets = (
    (None, {
      'fields':(('name', 'surnames', 'id_card'),
                ('nickname', 'nickname2'),
                ('email', 'email2'),
                ('website', 'telephone'))
    }),
    (_(u"Dates naixement/mort"), {
      'classes': ('collapse',),
      'fields': (('birth_date', 'death_date'),)
    })
  )
  #filter_horizontal = ('arts',)# 'projects',) # 'addresses',)
  inlines = [
    addressInline,
    jobInline,

    accountCesInline,
    accountBankInline,
    accountCryptoInline,

    #personInline,
    projectInline,
    companyInline,

    regionInline,
    materialInline,
    nonmaterialInline,
    recordInline,
  ]


class CompanyAdmin(admin.ModelAdmin): # admin.ModelAdmin):
  #class Media:
  #  js = ('mselect-to-mcheckbox.js', 'jquery-ui-1.10.2.custom.js',)
  #  css = {
  #    'all': ('css/mselect-to-mcheckbox.css',)
  #  }

  list_display = ['name', 'nickname', 'email', 'company_type']
  list_filter = ('company_type',)
  search_fields = ('name', 'nickname', 'email', 'company_type')

  fieldsets = (
    (None, {
      'fields':(('name', 'nickname', 'company_type'),
                ('legal_name', 'vat_number'),
                ('email', 'telephone', 'website'))
    }),
    #(_(u"Membres de referencia"), {
    #  'classes': ('collapse',),
    #  'fields':('ref_persons',),
    #}),
    (_(u"Dates inici/fi"), {
      'classes': ('collapse',),
      'fields': (('birth_date', 'death_date'),)
    })
  )
  #filter_horizontal = ('ref_members',) # 'jobs',) # 'addresses')
  inlines = [
    addressInline,
    jobInline,
    personInline,

    accountCesInline,
    accountBankInline,
    accountCryptoInline,

    #projectInline,
    #companyInline,

    materialInline,
    nonmaterialInline,
    regionInline,
    recordInline,
  ]

'''
class HumanAdmin(admin.ModelAdmin):
  list_display = ['name', 'nickname', 'email']
  search_fields = ('name','nickname','email',)
'''

# Register your models here.

#admin.site.register(Tree)

#admin.site.register(Being)
admin.site.register(Being_Type, MPTTModelAdmin) # Comment this line after creating 'Human', then 'Person', 'Project' and 'Company' under Human, inside Being_Types.
#admin.site.register(Human, HumanAdmin)
admin.site.register(Person, PersonAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Project_Type, MPTTModelAdmin)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Company_Type, MPTTModelAdmin)

#admin.site.register(rel_Human_Humans)

admin.site.register(Art, MPTTModelAdmin) # Comment this line after creating 'Relation' and 'Job' inside Arts.
admin.site.register(Relation, MPTTModelAdmin)
admin.site.register(Job, MPTTModelAdmin)


#admin.site.register(Artwork)
admin.site.register(Artwork_Type, MPTTModelAdmin) # Comment this line after creating 'Unit', 'Record', 'Material' and 'Nonmaterial' inside Artwork_Types
admin.site.register(Unit)
admin.site.register(Unit_Type, MPTTModelAdmin)
admin.site.register(UnitRatio)

admin.site.register(Nonmaterial)
admin.site.register(Nonmaterial_Type, MPTTModelAdmin)

admin.site.register(Material)
admin.site.register(Material_Type, MPTTModelAdmin)
admin.site.register(Asset)

admin.site.register(Record)
admin.site.register(Record_Type, MPTTModelAdmin)
admin.site.register(AccountCes)
admin.site.register(AccountBank)
admin.site.register(AccountCrypto)


#admin.site.register(Space)
admin.site.register(Space_Type, MPTTModelAdmin) # Comment this line after creating 'Address' and 'Region' inside Space_Types
admin.site.register(Address)
admin.site.register(Address_Type, MPTTModelAdmin)

admin.site.register(Region, MPTTModelAdmin)
admin.site.register(Region_Type, MPTTModelAdmin)

admin.site.register(Concept, MPTTModelAdmin)
admin.site.register(Type, MPTTModelAdmin) # Comment this line whenever you don't need to edit the main whole Types tree
