from django.db import models 
from django.contrib.auth.models import User 
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pics")
    background = models.TextField(default="No background created yet.")

    classes = (
        ("", ""),
        ('Barbarian', 'Barbarian'),
        ('Bard', 'Bard'),
        ('Cleric', 'Cleric'),
        ('Druid', 'Druid'),
        ('Fighter', 'Fighter'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Ranger', 'Ranger'),
        ('Rogue', 'Rogue'),
        ('Sorcerer', 'Sorcerer'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard'),
    )

    races = (
        ("", ""),
        ('Dragonborn', 'Dragonborn'),
        ('Dwarf', 'Dwarf'),
        ('Elf', 'Elf'),
        ('Gnome', 'Gnome'),
        ('Half-elf', 'Half-Elf'),
        ('Halfling', 'Halfling'),
        ('Half-orc', 'Half-Orc'),
        ('Human', 'Human'),
        ('Tabaxi', 'Tabaxi'),
        ('Tiefling', 'Tiefling'),
    )
    charClass = models.CharField(max_length=10, choices=classes, default="")
    race = models.CharField(max_length=15, choices=races, default="")
    
    def __str__(self):
        return f'{self.user.username} Profile'