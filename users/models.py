from django.db import models 
from django.contrib.auth.models import User 
from PIL import Image 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pics")
    background = models.TextField(default="No background created yet.")

    classes = (
        ('Barbarian', 'BARBARIAN'),
        ('Bard', 'BARD'),
        ('Cleric', 'CLERIC'),
        ('Druid', 'DRUID'),
        ('Fighter', 'FIGHTER'),
        ('Monk', 'MONK'),
        ('Paladin', 'PALADIN'),
        ('Ranger', 'RANGER'),
        ('Rogue', 'ROGUE'),
        ('Sorcerer', 'SORCERER'),
        ('Warlock', 'WARLOCK'),
        ('Wizard', 'WIZARD'),
    )

    races = (
        ('Dragonborn', 'DRAGONBORN'),
        ('Dwarf', 'DWARF'),
        ('Elf', 'ELF'),
        ('Gnome', 'GNOME'),
        ('Half-elf', 'HALF-ELF'),
        ('Halfling', 'HALFLING'),
        ('Half-orc', 'HALF-ORC'),
        ('Human', 'HUMAN'),
        ('Tiefling', 'TIEFLING'),
    )
    charClass = models.CharField(max_length=10, choices=classes, default="")
    race = models.CharField(max_length=15, choices=races, default="")
    
    def __str__(self):
        return f'{self.user.username} Profile'