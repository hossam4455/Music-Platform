from django.db.models.signals import pre_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Album, Song






@receiver(pre_delete, sender=Song)
def song_delete(sender, instance, **kwargs):
    flag = 0

    @receiver(pre_delete, sender=Album)
    def album_delete_check(**kwargs2):
        nonlocal flag
        flag = 1

    @receiver(post_delete, sender=Song)
    def song_delete_check(**kwargs3):
        nonlocal flag
        if flag == 0 and kwargs3['instance'].album.song_set.count() < 1:
            instance.save()
