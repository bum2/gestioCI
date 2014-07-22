Doc
----------------
[Main site (Spanish)](https://wiki.enredaos.net/index.php?title=GestioCI)
[Dev site (Spanish)](https://wiki.enredaos.net/index.php?title=GestioCI-Desarrollo)

DEPENDENCIES
------------------
pip install south

pip install django-cron

pip install django-csvimport

pip install django-localflavor


About the General App
---------------------
This app is divided in 5 general types of information (Beings, Arts, Spaces, Artworks and Concepts), using a basic Class for each and then several Subclasses to meet the organisational purposes. Sometimes the basic Class is 'abstract' (without an own db table), and so their first Subclasses are creating real db tables and unique ID's for each row. That is for dividing up the unique id creation to each subclass, instead of unique id's for the whole basic types (if they are going to be too much Big tables, and we don't need uid's to avoid conflicts).

To start using the General app in a new database, the recommended starting process will be:

1- Create a Concept called 'Type' (using the 'Concepts' admin view).

2- Create 3 basic types (using the 'Types' admin view) as:

  2.1- 'Being' (or Entity)

  2.2- 'Artwork' (or Creation)

  2.3- 'Space' (or Place)

  These 3 types must be assigned to be under 'Type' concept, using the 'parent' field (generating a hierarchical tree). Also we can define the name of the django class-model for each type (nowadays only for remember purposes): 'Being' class for the Being type, 'Artwork' class for the Artwork type and 'Space' class for the Space type.

3- Inside 'Being_Types', create a subtype called 'Human', assign the parent type to be 'Being' and the related class to be 'Human'.

4- Inside 'Being_Types', create 3 more subtypes under Human parent:

  4.1- 'Person' (related class: 'Person').

  4.2- 'Project' (related class: 'Project').

  4.3- 'Company' (related class: 'Company').

5- Inside 'Artwork_Types', create 4 subtypes under Artwork parent:

  5.1- 'Record' (related class: 'Record').

  5.2- 'Currency' (related class: 'Currency').

  5.3- 'Material' (related class: 'Material').

  5.4- 'Non-material' (related class: 'Nonmaterial').

6- Inside 'Space_Types', create 2 subtypes under Space parent:

  6.1- 'Region' (related class: 'Region').

  6.2- 'Address' (related class: 'Address').

7- Inside 'Record_Types', create 3 starting rows (nowadays related to 3 django classes/models):

  7.1- 'Account Ces' (related class: 'AccountCes')

  7.2- 'Account Bank' (related class: 'AccountBank')

  7.3- 'Currency Ratio'(related class: 'CurrencyRatio')

8- At this point, we can exclude some admin menu items/views, editing the admin.py inside General app/folder and commenting some lines at the bottom of that file (these lines have a comment marking which ones and some info):

  8.1- Comment the line 'admin.site.register(Being_Type, MPTTModelAdmin)'.

  8.2- Comment the line 'admin.site.register(Art, MPTTModelAdmin)'.

  8.3- Comment the line 'admin.site.register(Artwork_Type, MPTTModelAdmin)'.

  8.4- Comment the line 'admin.site.register(Space_Type, MPTTModelAdmin)'.

  8.5- If you don't want to edit directly the whole Types tree, comment the line 'admin.site.register(Type, MPTTModelAdmin)' and perhaps also the Concept main tree (commenting the line 'admin.site.register(Concept, MPTTModelAdmin)').

9- Now we can start defining some production subtypes for each main subclasses, using the appropiate '*_Types' view, and assigning the correct parent for each one (for example: inside Currency_Types you can put 'Social currency', 'Fiat currency' and 'Cryptocurrency', all related to the same parent type 'Currency').

10- Also we can start defining Arts (they are all Verbs), as Jobs or Relation kinds, which can be nested.

11- Also we can start defining real items of each type: some Projects, some Persons (which can be related eachother), some Currencies, some Regions (which can be nested), some Addresses or Accounts (which can be assigned to a person or project), etc.
