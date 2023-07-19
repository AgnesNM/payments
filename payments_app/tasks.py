from celery import shared_task

from time import sleep

#create a task

@shared_task
def sleeptime(total_time):

    sleep(total_time)

    return "yea"