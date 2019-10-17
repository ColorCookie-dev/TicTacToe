from django.db import models
from accounts.models import User

class Game(models.Model):

    def __new__(cls, *args, **kwargs):
        if (not kwargs.get('player1')) or kwargs['player1'].isidentifier():
            if (not kwargs.get('player2')) or kwargs['player2'].isidentifier():
                if (not kwargs.get('ended')) or kwargs['ended'] in range(6):
                    return super(Game, cls).__new__(cls)
        return None

    player1 = models.CharField(max_length=50, default='anonymous')
    player2 = models.CharField(max_length=50, default='computer')
    row = models.IntegerField(default=3)
    col = models.IntegerField(default=3)
    ended = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(ended__lte=5), name='ended_lte_5'),
            models.CheckConstraint(check=models.Q(row__gte=1), name='row_gte_1'),
            models.CheckConstraint(check=models.Q(col__gte=1), name='col_gte_1'),
        ]
