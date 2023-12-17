# success_tracker/tasks.py
from celery import shared_task
from django.core.management import call_command

@shared_task
def daily_evaluation():
    call_command('evaluate_daily')
