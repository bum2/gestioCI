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



class ProjectAdmin(MPTTModelAdmin): # admin.ModelAdmin):
  #class Media:
  #  js = ('mselect-to-mcheckbox.js', 'jquery-ui-1.10.2.custom.js',)
  #  css = {
  #    'all': ('css/mselect-to-mcheckbox.css',)
  #  }

  fieldsets = (
    (None, {
      'fields':(('name', 'nickname'), ('website', 'socialweb'), ('being_type', 'parent'), ('email', 'email2', 'telephone'))
    }),
    (_(u"Membres de referencia"), {
      'classes': ('collapse',),
      'fields':('ref_members',),
      #'filter_horizontal': ('members', 'ref_members',)
    }),
    (_(u"Adreçes"), {
      'classes': ('collapse',),
      'fields': ('addresses',)
    }),
    (_("Arts"), {
      'classes': ('collapse',),
      'fields': ('jobs',)
    }),
    (_(u"Dates inici/fi"), {
      'classes': ('collapse',),
      'fields': (('birth_date', 'dead_date'),)
    })
  )
  filter_horizontal = ('ref_members', 'addresses', 'jobs')



class PersonAdmin(admin.ModelAdmin):

  #class Media:
  #  js = ('mselect-to-mcheckbox.js', 'jquery-ui-1.10.2.custom.js',)
  #  css = {
  #    'all': ('css/mselect-to-mcheckbox.css',)
  #  }


  fieldsets = (
    (None, {
      'fields':(('name', 'surnames'), ('nickname', 'nickname2'), ('email', 'email2'), ('website', 'telephone'))
    }),
    (_(u"Adreçes"), {
      'classes': ('collapse',),
      'fields': ('addresses',)
    }),
    (_("Arts"), {
      'classes': ('collapse',),
      'fields': ('jobs',)
    }),
    (_(u"Projectes"), {
      'classes': ('collapse',),
      'fields': ('projects',)
    }),
    (_(u"Dates naixement/mort"), {
      'classes': ('collapse',),
      'fields': (('birth_date', 'dead_date'),)
    })
  )
  filter_horizontal = ('addresses', 'jobs', 'projects',)



# Register your models here.
#admin.site.register(Tree)

#admin.site.register(Being)
admin.site.register(Being_Type, MPTTModelAdmin) # Comment this line after creating 'Human', then 'Person', 'Project' and 'Company' under Human, inside Being_Types.
#admin.site.register(Human)
admin.site.register(Person, PersonAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Project_Type, MPTTModelAdmin)

admin.site.register(Company)
admin.site.register(Company_Type, MPTTModelAdmin)


admin.site.register(Art, MPTTModelAdmin) # Comment this line after creating 'Relation' and 'Job' inside Arts.
admin.site.register(Relation, MPTTModelAdmin)
admin.site.register(Job, MPTTModelAdmin)


#admin.site.register(Artwork)
admin.site.register(Artwork_Type, MPTTModelAdmin) # Comment this line after creating 'Currency', 'Record', 'Material' and 'Nonmaterial' inside Artwork_Types
admin.site.register(Unit)
admin.site.register(Unit_Type, MPTTModelAdmin)
admin.site.register(UnitRatio)

admin.site.register(Nonmaterial)
admin.site.register(Nonmaterial_Type, MPTTModelAdmin)

admin.site.register(Material)
admin.site.register(Material_Type, MPTTModelAdmin)

admin.site.register(Record)
admin.site.register(Record_Type, MPTTModelAdmin)
admin.site.register(AccountCes)
admin.site.register(AccountBank)


#admin.site.register(Space)
admin.site.register(Space_Type, MPTTModelAdmin) # Comment this line after creating 'Address' and 'Region' inside Space_Types
admin.site.register(Address)
admin.site.register(Address_Type, MPTTModelAdmin)

admin.site.register(Region, MPTTModelAdmin)
admin.site.register(Region_Type, MPTTModelAdmin)

admin.site.register(Concept, MPTTModelAdmin)
admin.site.register(Type, MPTTModelAdmin) # Comment this line whenever you don't need to edit the main whole Types tree
