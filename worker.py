import os
from celery import Celery

from strip import *

celery = Celery('tasks',broker=os.getenv('REDIS_URL', 'redis://localhost'))

# decorate celery task "after the fact"
clear = celery.task(name='clear')(clear)
brighteness = celery.task(name='brighteness')(brighteness)
colorWipe = celery.task(name='colorWipe')(colorWipe)
rainbow = celery.task(name='rainbow')(rainbow)
rainbowCycle = celery.task(name='rainbowCycle')(rainbowCycle)
solid = celery.task(name='solid')(solid)
theaterChase = celery.task(name='theaterChase')(theaterChase)
