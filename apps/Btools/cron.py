# -*- coding: utf-8 -*-

from apps.django_cron import cronScheduler, Job
from models import BookSet
from datetime import datetime

class CheckBS(Job):
    # run every 300 seconds (5 minutes)
    run_every = 300

    def job(self):
        fo = open('cron_test_file', "wb")
        fo.write('bobo time \n')
        fo.close()
        bsets = BookSet.odjects.all()
        for bset in bsets:
            if datetime.time() > bset.time  and bset.last_time_update.date() != datetime.date():
                bset.save()
               
cronScheduler.register(CheckBS)
