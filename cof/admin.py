from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *

class PersoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name","last_name",)}

class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("race_name",)}

class ProfileWeaponsInline(admin.TabularInline):
    model = ProfileWeapons

class ProfileArmorsInline(admin.TabularInline):
    model = ProfileArmors

class ProfileMaterialsInline(admin.TabularInline):
    model = ProfileMaterials

class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("profile_name",)}
    inlines = [
            ProfileWeaponsInline,
            ProfileArmorsInline,
            ProfileMaterialsInline,
    ]

class WeaponAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('weapon_name', 'weapon_category', ('price', 'rarity')),
        }),
        ('Informations', {
            'fields': ('weapon_range', ('nb_dice_damage', 'dice_side_damage'), 'critical', 'recharging'),
        }),
        ('Extra', {
            'fields': (('quantity', 'quantity_unit'),('is_magic', 'quality'), 'note'),
        }),
    )

class ArmorAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('armor_name', 'armor_category', ('price', 'rarity')),
        }),
        ('Informations', {
            'fields': ('armor_def',),
        }),
        ('Extra', {
            'fields': (('quantity', 'quantity_unit'),('is_magic', 'quality'), 'note'),
        }),
    )
    

admin.site.register(Perso, PersoAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(RaceTrait)
admin.site.register(RaceLimitation)
admin.site.register(BasicWay)
admin.site.register(RacialWay)
admin.site.register(Rank)
admin.site.register(Armor, ArmorAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(ArmorCategory)
admin.site.register(WeaponCategory)

