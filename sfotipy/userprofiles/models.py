from django.db import models

# Create your models here.

# from django.core.cache import cache
# from django.db.models.signals import post_save
# from django.contrib.sessions.models import Session
# from django.dispatch import receiver

# @receiver(post_save)
# def clear_cache(sender, **kwargs):
# 	if sender != Session:
# 		cache._cache.flush_all()



from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
 
from django.contrib.sessions.models import Session
@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()