from django.db import models

class Equipment(models.Model):
    price = models.PositiveSmallIntegerField(default=1)
    note = models.TextField(blank=True)

    RARITY_CHOICES = (
        (1, 'Ordinaire'),
        (2, 'Précieux'),
        (3, 'Exotique'),
        (4, 'Rare'),
        (5, 'Très rare'),
    )
    rarity = models.PositiveSmallIntegerField(choices=RARITY_CHOICES, default=1)
    quality = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    quantity_unit = models.CharField(max_length=30, blank=True)
    is_magic = models.BooleanField(default=False)

    class Meta:
        abstract = True

class EquipmentCategory(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return self.category_name

class WeaponCategory(EquipmentCategory):
    pass

class ArmorCategory(EquipmentCategory):
    pass

class Weapon(Equipment):
    weapon_name = models.CharField(max_length=30)
    weapon_category = models.ForeignKey(WeaponCategory, on_delete=models.CASCADE)
    weapon_range = models.PositiveSmallIntegerField(blank=True, default=0)
    nb_dice_damage = models.PositiveSmallIntegerField(default=1)
    dice_side_damage = models.PositiveSmallIntegerField(default=6)
    critical = models.CharField(max_length=30, blank=True)

    RECHARGING_CHOICES = (
            ('simple', '1 action simple'),
            ('limited', '1 action limitée'),
        )
    recharging = models.CharField(max_length=7,choices=RECHARGING_CHOICES, blank=True)

    def __str__(self):
        return self.weapon_name

    def _get_damage_dice(self):
        """
        Return the damage dice for a weapon.
        """
        return '%sd%s' %(self.nb_dice_damage, self.dice_side_damage)
    damage_dice = property(_get_damage_dice)

class Armor(Equipment):
    armor_name = models.CharField(max_length=30)
    armor_def = models.PositiveSmallIntegerField(default=1)
    armor_category = models.ForeignKey(ArmorCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.armor_name

    def _display_armor_def(self):
        """
        Return the sign + for armor_def
        """
        return '+%s' % (self.armor_def)
    armor_def_value = property(_display_armor_def)


class Material(Equipment):
    material_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.material_name

class Rank(models.Model):
    rank_name = models.CharField(max_length=50)
    rank_description = models.TextField()
    rank_level = models.PositiveSmallIntegerField(default=1)
    limited = models.BooleanField(default=False)
    spell = models.BooleanField(default=False)
    
    def __str__(self):
        return self.rank_name

class RaceTrait(models.Model):
    race_trait_name = models.CharField(max_length=30)
    trait_description = models.TextField()

    def __str__(self):
        return self.race_trait_name

class RaceLimitation(models.Model):
    race_limitation_name = models.CharField(max_length=30)
    limitation_description = models.TextField()

    def __str__(self):
        return self.race_limitation_name

class RacialWay(models.Model):
    racial_way_name = models.CharField(max_length=30)
    rank_one = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"1"}, related_name="racial_rank_one")
    rank_two = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"2"}, related_name="racial_rank_two")
    rank_three = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"3"}, related_name="racial_rank_three")
    rank_four = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"4"}, related_name="racial_rank_four")
    rank_five = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"5"}, related_name="racial_rank_five")

    def __str__(self):
        return self.racial_way_name

class Race(models.Model):
    race_name = models.CharField(max_length=30)
    race_description = models.TextField()
    slug = models.SlugField(max_length=30, unique=True)
    prejudice = models.TextField()
    trait_strength = models.SmallIntegerField(default=0)
    trait_dexterity = models.SmallIntegerField(default=0)
    trait_constitution = models.SmallIntegerField(default=0)
    trait_intelligence = models.SmallIntegerField(default=0)
    trait_wisdom = models.SmallIntegerField(default=0)
    trait_charisma = models.SmallIntegerField(default=0)
    race_picture = models.ImageField(upload_to="images/races", blank=True)

    race_traits = models.ManyToManyField(RaceTrait, blank=True)
    race_limitations = models.ManyToManyField(RaceLimitation, blank=True)
    racial_way = models.ManyToManyField(RacialWay)

    def __str__(self):
        return self.race_name

class BasicWay(models.Model):
    way_name = models.CharField(max_length=50)
    way_capacity = models.TextField(blank=True)
    
    rank_one = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"1"}, related_name="basic_rank_one")
    rank_two = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"2"}, related_name="basic_rank_two")
    rank_three = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"3"}, related_name="basic_rank_three")
    rank_four = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"4"}, related_name="basic_rank_four")
    rank_five = models.ForeignKey(Rank, on_delete=models.CASCADE, limit_choices_to={'rank_level':"5"}, related_name="basic_rank_five")

    def __str__(self):
        return self.way_name

class Profile(models.Model):
    profile_name = models.CharField(max_length=30)
    profile_resume = models.TextField()
    profile_description = models.TextField()
    slug = models.SlugField(max_length=30, unique=True, default="profile1")
    hit_dice = models.PositiveSmallIntegerField(default=0)
    magic_modifier = models.CharField(max_length=3, blank=True)
    recommanded_traits = models.CharField(max_length=30, default="no-recommandation")
    sup_strength = models.BooleanField(default=False)
    sup_dexterity = models.BooleanField(default=False)
    sup_constitution = models.BooleanField(default=False)
    sup_intelligence = models.BooleanField(default=False)
    sup_wisdom = models.BooleanField(default=False)
    sup_charisma = models.BooleanField(default=False)
    weapons_armors_capacities = models.TextField(default="capacity")
    profile_picture = models.ImageField(upload_to="images/profiles", blank=True)
    weapons_start = models.ManyToManyField(Weapon, blank=True, through='ProfileWeapons')
    armor_start = models.ManyToManyField(Armor, blank=True, through='ProfileArmors')
    material_start = models.ManyToManyField(Material, blank=True, through='ProfileMaterials')
    special_material_start = models.CharField(max_length=50, blank=True)

    FAMILY_CHOICES = (
        ('VOY', 'Voyageur'),
        ('COM', 'Combattant'),
        ('LAN', 'Lanceur de sort'),
        ('NOF', 'Pas de famille'),
    )
    family = models.CharField(max_length=3, choices=FAMILY_CHOICES, default='NOF')

    basic_ways = models.ManyToManyField(BasicWay)

    def __str__(self):
        return self.profile_name

class ProfileEquipmentQuantity(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    
    class Meta:
        abstract=True

class ProfileWeapons(ProfileEquipmentQuantity):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    
class ProfileArmors(ProfileEquipmentQuantity):
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)

class ProfileMaterials(ProfileEquipmentQuantity):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    
class Perso(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField(default=1)
    strength = models.PositiveSmallIntegerField(default=0)
    dexterity = models.PositiveSmallIntegerField(default=0)
    constitution = models.PositiveSmallIntegerField(default=0)
    intelligence = models.PositiveSmallIntegerField(default=0)
    wisdom = models.PositiveSmallIntegerField(default=0)
    charisma = models.PositiveSmallIntegerField(default=0)
    age = models.PositiveSmallIntegerField(default=20)
    height = models.PositiveSmallIntegerField(default=80)
    weight = models.PositiveSmallIntegerField(default=20)
    slug = models.SlugField(max_length=105, unique=True)
    perso_picture = models.ImageField(upload_to="images/persos", blank=True)

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    profiles = models.ManyToManyField(Profile)

    def mod_strength_calc(self):
        """
        Return the modifier of Strength.
        """
        if strength <= 3 :
            mod_strength = -4
        elif strength <= 5 :
            mod_strength = -3
        elif strength <= 7 :
            mod_strength = -2
        elif strength <= 9 :
            mod_strength = -1
        elif strength <= 11 :
            mod_strength = 0
        elif strength <= 13 :
            mod_strength = 1
        elif strength <= 15 :
            mod_strength = 2
        elif strength <= 17 :
            mod_strength = 3
        elif strength <= 19 :
            mod_strength = 4
        else:
            mod_strength = 5
        
        return ('%s' % mod_strength)



    def _get_full_name(self):
        """
        Return the perso's full name.
        """
        return '%s %s' %(self.first_name, self.last_name)
    full_name = property(_get_full_name)

    def __str__(self):
        return self.full_name
