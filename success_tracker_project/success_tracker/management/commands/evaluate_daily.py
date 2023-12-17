# success_tracker/management/commands/evaluate_daily.py
from django.core.management.base import BaseCommand
from success_tracker.models import Task, DailyEvaluation

class Command(BaseCommand):
    help = 'Perform daily evaluation and assign marks'

    def handle(self, *args, **options):
        # Your daily evaluation logic here
        tasks_completed = Task.objects.filter(completed=True).count()

        # Assuming you have a DailyEvaluation model to store marks
        DailyEvaluation.objects.create(marks=tasks_completed)

        self.stdout.write(self.style.SUCCESS('Daily evaluation completed. Marks assigned.'))
