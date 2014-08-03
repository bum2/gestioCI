from django.contrib import admin

from django.forms.extras import widgets

from django.utils.translation import ugettext as _

from mptt.admin import MPTTModelAdmin
from mptt.fields import TreeForeignKey, TreeManyToManyField
#from mptt.forms import MPTTAdminForm, TreeNodeChoiceField

from Welcome.models import *

class MembershipAdmin(admin.ModelAdmin):
  list_display = ['name', 'human', 'ic_CESnum', 'ic_project', '_join_fee_payed']

  fieldsets = (
    (None, {
      'fields':(('human', 'ic_project', 'name', 'ic_CESnum'),
                ('contribution', 'virtual_market', 'labor_contract'),
                ('join_fee', 'join_date', 'end_date'),
                ('expositors', 'comment'))
    }),
    #(_(u"Dates naixement/mort"), {
    #  'classes': ('collapse',),
    #  'fields': (('birth_date', 'death_date'),)
    #})
  )

# Register your models here.

admin.site.register(iC_Record) # es pot comentar
admin.site.register(iC_Membership, MembershipAdmin)
admin.site.register(iC_Self_Employed)
admin.site.register(iC_Stallholder)

#admin.site.register(iC_Document)
admin.site.register(iC_Document_Type)
admin.site.register(iC_Labor_Contract)
admin.site.register(iC_Address_Contract)
admin.site.register(iC_Insurance)
admin.site.register(iC_Licence)

admin.site.register(Fee)
admin.site.register(Learn_Session)
admin.site.register(Project_Accompaniment)
