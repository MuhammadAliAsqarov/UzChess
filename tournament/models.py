from django.db import models
from authentication.models import User


class Player(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    rating = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(Player, related_name='tournaments')

    def __str__(self):
        return self.name


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='matches', on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player, related_name='matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='matches_as_player2', on_delete=models.CASCADE)
    round_number = models.IntegerField()
    player1_score = models.FloatField(default=0)
    player2_score = models.FloatField(default=0)

    def __str__(self):
        return f"{self.player1} vs {self.player2} (Round {self.round_number})"
