import uuid
from django.db import models


class Game(models.Model):
    game_id = models.UUIDField(primary_key=True,
                               default=uuid.uuid4,
                               editable=False)
    width = models.IntegerField(blank=False,
                                null=False)
    height = models.IntegerField(blank=False,
                                 null=False)
    mines_count = models.IntegerField(blank=False,
                                      null=False)
    field = models.JSONField(blank=True,
                             null=True)
    completed = models.BooleanField(blank=True,
                                    default=False)
    field_with_mines = models.JSONField(blank=True,
                                        null=True,
                                        default=None)

    def save(self, *args, **kwargs):
        if not self.field:
            self.field = [[" " for i in range(int(self.width))]
                          for j in range(int(self.height))]
        super(Game, self).save(*args, **kwargs)
