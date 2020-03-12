from django.db import models


# Background Classes for ENums
class OutCome(models.IntegerChoices):
    XWin = 1,
    OWin = 2,
    Draw = -1
    ND = 0 # Not Determined

class PlayerChoice(models.IntegerChoices):
    X = 0
    O = 1

# ==== Real Models for storing data
class Game(models.Model):
    game_id = models.CharField(max_length=15, unique=True)
    tiles = models.PositiveSmallIntegerField()
    outcome = models.IntegerField(choices=OutCome.choices, default=OutCome.ND)
    turn = models.IntegerField(choices=PlayerChoice.choices, default=PlayerChoice.X)
    start_DT = models.DateTimeField(auto_now=True)

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.IntegerField(choices=PlayerChoice.choices)
    move = models.PositiveIntegerField()
    time = models.TimeField(auto_now=True)
