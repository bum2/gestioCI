#encoding=utf-8

from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey, TreeManyToManyField
from datetime import date, timedelta
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal


# Create your models here.
'''
class Tree(models.Model):
  name = models.CharField(verbose_name=_(u"Nom"), max_length=30, help_text=_(u"El nom del Arbre"))
  clas = models.CharField(blank=True, verbose_name=_(u"Clase"), max_length=30,
                          help_text=_(u"Model de django per fer l'arbre (cal que tingui 'left' i 'right')"))
  TYPES = (
    ('A','Art'),
    ('B','Being'),
    ('W','Artwork'),
    ('S','Space'),
    ('C','Concept')
  )
  clas_type = models.CharField( choices = TYPES, blank=True, verbose_name=_(u"Tipus bàsic"),
                                max_length=1, help_text=_(u"El tipus bàsic de dada dels models que ordenem en l'arbre"))
  def __unicode__(self):
    return self.name
'''



# C O N C E P T S - (Conceptes...)

class Concept(MPTTModel):  # Create own ID's (TREE)
  name = models.CharField(unique=True, verbose_name=_(u"Nom"), max_length=30, help_text=_(u"El nom del Concepte"), default="")
  description = models.TextField(blank=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name = _(u"Concepte")
    verbose_name_plural = _(u"c- Conceptes")


class Type(Concept):
  concept = models.OneToOneField('Concept', primary_key=True, parent_link=True)
  clas = models.CharField(blank=True, verbose_name=_(u"Clase"), max_length=30,
                          help_text=_(u"Model de django o classe python associada al Tipus"))
  class Meta:
    verbose_name = _(u"c- Tipus")




# B E I N G S - (Éssers, Entitats, Projectes...)

class Being(models.Model):  # Abstract
  name = models.CharField(verbose_name=_(u"Nom"), max_length=50, help_text=_(u"El nom de la Entitat"))
  being_type = TreeForeignKey('Being_Type', blank=True, null=True, verbose_name=_(u"Tipus d'entitat"))
  birth_date = models.DateField(blank=True, null=True, verbose_name=_(u"Data de naixement"), help_text=_(u"El dia que va començar a existir"))
  dead_date = models.DateField(blank=True, null=True, verbose_name=_(u"Data d'acabament"), help_text=_(u"El dia que va deixar d'existir"))

  class Meta:
    abstract = True

  def __unicode__(self):
    return self.name

class Being_Type(Type):
  typ = models.OneToOneField('Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name= _(u"Tipus d'entitat")
    verbose_name_plural = _(u"e- Tipus d'entitats")


class Human(Being):  # Create own ID's
  nickname = models.CharField(max_length=20, blank=True, verbose_name=_(u"Sobrenom"), help_text=_(u"El sobrenom (nickname) de l'entitat Humana"))
  email = models.EmailField(max_length=40, blank=True, verbose_name=_(u"Email"), help_text=_(u"L'adreça d'email principal de l'entitat humana"))
  telephone = models.CharField(max_length=20, blank=True, verbose_name=_(u"Telèfon"), help_text=_(u"El telèfon principal de l'entitat Humana"))
  website = models.CharField(max_length=40, blank=True, verbose_name=_(u"Web"), help_text=_(u"L'adreça web principal de l'entitat humana"))
  jobs = models.ManyToManyField('Job', verbose_name=_(u"Activitats, Oficis"), blank=True, null=True)
  addresses = models.ManyToManyField('Address', verbose_name=_(u"Adreçes"), blank=True, null=True)
  #accountsCes = models.ManyToManyField('AccountCes', verbose_name=_(u"Comptes M.S."), blank=True, null=True, help_text=_(u"Comptes de Moneda Social de l'entitat (ICES/CES)"))

  class Meta:
    verbose_name = _(u"Humà")
    verbose_name_plural = _(u"e- Humans")


class Person(Human):
  human = models.OneToOneField('Human', primary_key=True, parent_link=True)
  surnames = models.CharField(max_length=40, blank=True, verbose_name=_(u"Cognoms"), help_text=_(u"Els cognoms de la Persona"))
  projects = TreeManyToManyField('Project', blank=True, null=True, verbose_name=_(u"Projectes"), help_text=_(u"Persona vinculada als projectes o col·lectius seleccionats"))
  id_card = models.CharField(max_length=9, blank=True, verbose_name=_(u"DNI/NIE"))
  email2 = models.EmailField(blank=True, verbose_name=_(u"Email alternatiu"))
  nickname2 = models.CharField(max_length=20, blank=True, verbose_name=_(u"Sobrenom a la Xarxa Social"))

  class Meta:
    verbose_name= _(u'Persona')
    verbose_name_plural= _(u'e- Persones')

  def __unicode__(self):
    if self.nickname is None or self.nickname == '':
      if self.surnames is None or self.surnames == '':
        return self.name+' '+self.nickname2
      else:
        return self.name+' '+self.surnames
    else:
      if self.surnames is None or self.surnames == '':
        return self.name+' '+self.nickname
      else:
        return self.name+' '+self.surnames



class Project(MPTTModel, Human):
  human = models.OneToOneField('Human', primary_key=True, parent_link=True)
  #members = models.ManyToManyField('Person', related_name='projects', blank=True, null=True, verbose_name=_(u"Persones/Membres"))
  ref_members = models.ManyToManyField('Person', related_name='ref_projects', blank=True, null=True, verbose_name=_(u"Persones de referencia"))
  parent = TreeForeignKey('self', null=True, blank=True, related_name='subprojects', verbose_name=_(u"Projecte Marc"))
  socialweb = models.CharField(max_length=30, blank=True, verbose_name=_(u"Web Social"))
  email2 = models.EmailField(blank=True, verbose_name=_(u"Email alternatiu"))

  class Meta:
    verbose_name= _(u'Projecte')
    verbose_name_plural= _(u'e- Projectes')



class Project_Type(Being_Type):
  being_type = models.OneToOneField('Being_Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name = _(u"Tipus de Projecte")
    verbose_name_plural = _(u"e- Tipus de Projectes")


class Company(Human):
  human = models.OneToOneField('Human', primary_key=True, parent_link=True)
  legal_name = models.CharField(max_length=40, blank=True, null=True, verbose_name=_(u"Nom Fiscal"))
  vat_number = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u"CIF"))
  ref_members = models.ManyToManyField('Person', related_name='ref_companies', blank=True, null=True, verbose_name=_(u"Persones de contacte"))
  #accountsBank
  class Meta:
    verbose_name = _(u"Empresa")
    verbose_name_plural = _(u"e- Empreses")

class Company_Type(Being_Type):
  being_type = models.OneToOneField('Being_Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name = _(u"Tipus d'Empresa")
    verbose_name_plural = _(u"e- Tipus d'Empreses")




# A R T S - (Verbs, Relacions, Arts, Oficis, Sectors...)

class Art(MPTTModel):  # Create own ID's (TREE)
  name = models.CharField(unique=True, max_length=30, verbose_name=_(u"Nom"), help_text=_(u"El nom de l'Art"))
  verb = models.CharField(max_length=30, blank=True, verbose_name=_(u"Verb"), help_text=_(u"El verb de la acció, infinitiu"))
  gerund = models.CharField(max_length=30, blank=True, verbose_name=_(u"Gerundi"), help_text=_(u"El verb en gerundi, present"))
  description = models.TextField(blank=True)

  parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

  def __unicode__(self):
    return self.name
  class Meta:
    verbose_name = _(u"Art")
    verbose_name_plural = _(u"a- Arts")


class Relation(Art):
  art = models.OneToOneField('Art', primary_key=True, parent_link=True)
  clas = models.CharField(blank=True, verbose_name=_(u"Clase"), max_length=30,
                          help_text=_(u"Model de django o classe python associada a la Relació"))
  #relation_type = models.ForeignKey('Relation_Type', blank=True, null=True, verbose_name=_(u"Tipus de Relació"))
  #record = models.OndeToOneField('Record', blank=True, null=True, verbose_name=_(u"Registre?"))
  class Meta:
    verbose_name= _(u'Relació')
    verbose_name_plural= _(u'a- Relacions')
  #pass

class Job(Art):
  art = models.OneToOneField('Art', primary_key=True, parent_link=True)
  clas = models.CharField(blank=True, verbose_name=_(u"Clase"), max_length=30,
                          help_text=_(u"Model de django o classe python associada a l'Ofici'"))
  #job_type = models.ForeignKey('Job_Type', blank=True, null=True, verbose_name=_(u"Tipus d'Ofici-Activitat"))
  class Meta:
    verbose_name= _(u'Ofici')
    verbose_name_plural= _(u'a- Oficis')
  #pass






# S P A C E S - (Regions, Espais, Adreçes...)

class Space(models.Model):  # Abstact
  name = models.CharField(verbose_name=_(u"Nom"), max_length=30, help_text=_(u"El nom de l'Espai"))
  space_type = TreeForeignKey('Space_Type', blank=True, null=True, verbose_name=_(u"Tipus d'espai"))
  #m2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  comment = models.TextField(blank=True, null=True, verbose_name=_(u"Comentari"), help_text=_(u"Localització exacta, indicacions per arribar o comentaris"))
  longitude = models.IntegerField(blank=True, null=True, verbose_name=_(u"Logitud (geo)"));
  latitude = models.IntegerField(blank=True, null=True, verbose_name=_(u"Latitud (geo)"));

  def __unicode__(self):
    return self.name

  class Meta:
    abstract = True;

class Space_Type(Type):
  typ = models.OneToOneField('Type', primary_key=True, parent_link=True)
  #concept = models.OneToOneField(Concept, parent_link=True)
  #tree = models.ForeignKey(Tree, limit_choices_to={'clas': 'Space_Type'})
  class Meta:
    verbose_name= _(u"Tipus d'Espai")
    verbose_name_plural= _(u"s- Tipus d'Espais")



class Address(Space):  # Create own ID's
  #space = models.OneToOneField('Space', primary_key=True, parent_link=True)

  p_address = models.CharField(max_length=50, verbose_name=_(u"Direcció"), help_text=_(u"Adreça postal vàlida per a enviaments"))
  town = models.CharField(max_length=40, verbose_name=_(u"Població"), help_text=_(u"Poble, ciutat o municipi"))
  postalcode = models.CharField(max_length=5, blank=True, null=True, verbose_name=_(u"Codi postal"))
  region = TreeForeignKey('Region', blank=True, null=True, related_name='addresses', verbose_name=_(u"Regió"))
  m2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_(u'M2'), help_text=_(u"Metres quadrats (accepta 2 decimals)"))

  class Meta:
    verbose_name= _(u'Adreça')
    verbose_name_plural= _(u's- Adreçes')


class Address_Type(Space_Type):
  space_type = models.OneToOneField('Space_Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name = _(u"Tipus d'Adreça")
    verbose_name_plural = _(u"s- Tipus d'Adreçes")



class Region(MPTTModel, Space):  # Create own ID's (TREE)
  #space = models.OneToOneField('Space', primary_key=True, parent_link=True)

  parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

  class Meta:
    verbose_name= _(u'Regió')
    verbose_name_plural= _(u's- Regions')

class Region_Type(Space_Type):
  space_type = models.OneToOneField('Space_Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name = _(u"Tipus de Regió")
    verbose_name_plural = _(u"s- Tipus de Regions")



# A R T W O R K S - (Obres, Coses, Registres, Documents...)

class Artwork(models.Model):  # Abstract
  name = models.CharField(verbose_name=_(u"Nom"), max_length=30, help_text=_(u"El nom de la Obra"))
  #artwork_type = TreeForeignKey('Artwork_Type', blank=True, verbose_name=_(u"Tipus d'Obra"))

  def __unicode__(self):
    return self.name

  class Meta:
    abstract = True

class Artwork_Type(Type):
  typ = models.OneToOneField('Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name = _(u"Tipus d'Obra")
    verbose_name_plural = _(u"o- Tipus d'Obres")



class Nonmaterial(Artwork):  # Create own ID's
  nonmaterial_type = TreeForeignKey('Nonmaterial_Type', blank=True, null=True, verbose_name=_(u"Tipus d'obra inmaterial"))
  class Meta:
    verbose_name = _(u"Obra Inmaterial")
    verbose_name_plural = _(u"o- Obres Inmaterials")

class Nonmaterial_Type(Artwork_Type):
  artwork_type = models.OneToOneField('Artwork_Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name= _(u"Tipus d'obra Inmaterial")
    verbose_name_plural= _(u"o- Tipus d'obres Inmaterials")



class Material(Artwork): # Create own ID's
  material_type = TreeForeignKey('Material_Type', blank=True, null=True, verbose_name=_(u"Tipus d'obra física"))
  class Meta:
    verbose_name = _(u"Obra Material")
    verbose_name_plural = _(u"o- Obres Materials")

class Material_Type(Artwork_Type):
  artwork_type = models.OneToOneField('Artwork_Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name= _(u"Tipus d'obra Material")
    verbose_name_plural= _(u"o- Tipus d'obres Materials")



class Record(Artwork):  # Create own ID's
  record_type = TreeForeignKey('Record_Type', blank=True, null=True, verbose_name=_(u"Tipus de Registre"))
  class Meta:
    verbose_name= _(u'Registre')
    verbose_name_plural= _(u'o- Registres')


class Record_Type(Artwork_Type):
  artwork_type = models.OneToOneField('Artwork_Type', primary_key=True, parent_link=True)
  class Meta:
    verbose_name= _(u'Tipus de Registre')
    verbose_name_plural= _(u'o- Tipus de Registres')



class Currency(Artwork):  # Create own ID's
  #artwork = models.OneToOneField('Artwork', primary_key=True, parent_link=True)
  currency_type = models.ForeignKey('Currency_Type', blank=True, null=True, verbose_name=_(u"Tipus de Moneda"))
  code = models.CharField(max_length=4, blank=True, null=True, verbose_name=_(u"Codi o Símbol"))
  region = TreeForeignKey('Region', blank=True, null=True, verbose_name=_(u"Regió d'us"))

  class Meta:
    verbose_name= _(u'Moneda')
    verbose_name_plural= _(u'o- Monedes')

class Currency_Type(Artwork_Type):
  artwork_type = models.OneToOneField('Artwork_Type', primary_key=True, parent_link=True)

  class Meta:
    verbose_name = _(u"Tipus de Moneda")
    verbose_name_plural = _(u"o- Tipus de Monedes")



class CurrencyRatio(Record):
  record = models.OneToOneField('Record', primary_key=True, parent_link=True)

  in_currency = models.ForeignKey('Currency', related_name='ratio_in', verbose_name=_(u"Moneda entrant"))
  rate = models.DecimalField(max_digits=6, decimal_places=3, verbose_name=_(u"Ratio multiplicador"))
  out_currency = models.ForeignKey('Currency', related_name='ratio_out',verbose_name=_(u"Moneda sortint"))

  class Meta:
    verbose_name = _(u"Equivalencia Monedes")
    verbose_name_plural = _(u"o- Equivalencies Monedes")



class AccountCes(Record):
  record = models.OneToOneField('Record', primary_key=True, parent_link=True)

  human = models.ForeignKey('Human', related_name='accountsCes', verbose_name=_(u"Entitat humana persuaria"))
  entity = models.ForeignKey('Project', blank=True, null=True, verbose_name=_(u"Xarxa del compte"))
  currency = models.ForeignKey('Currency', blank=True, null=True, verbose_name=_(u"Moneda"))
  code = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u"Codi"))
  number = models.CharField(max_length=4, blank=True, null=True, verbose_name=_(u"Número"))

  class Meta:
    verbose_name= _(u'Compte CES')
    verbose_name_plural= _(u'o- Comptes CES')

  def __unicode__(self):
    return self.name+'  ('+self.human.name+')'

class AccountBank(Record):
  record = models.OneToOneField('Record', primary_key=True, parent_link=True)

  human = models.ForeignKey('Human', related_name='accountsBank', verbose_name=_(u"Entitat humana titular"))
  company = models.ForeignKey('Company', blank=True, null=True, verbose_name=_(u"Entitat Bancaria"))
  currency = models.ForeignKey('Currency', blank=True, null=True, verbose_name=_(u"Moneda"))
  code = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u"Codi SWIF"))
  number = models.CharField(max_length=4, blank=True, null=True, verbose_name=_(u"Número de Compte IBAN"))

  class Meta:
    verbose_name= _(u'Compte Bancari')
    verbose_name_plural= _(u'o- Comptes Bancaris')

  def __unicode__(self):
    return self.name+'  ('+self.human.name+')'
