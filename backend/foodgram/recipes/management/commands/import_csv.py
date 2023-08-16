import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = "Импортирует данные из CSV-файла в модель Ingredient"

    def handle(self, *args, **options):
        data_path = settings.BASE_DIR
        with open(
            f"{data_path}/data/ingredients.csv", "r", encoding="utf-8"
        ) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name, measurement_unit = row
                Ingredient.objects.create(
                    name=name, measurement_unit=measurement_unit
                )
        self.stdout.write(self.style.SUCCESS("Все данные загружены"))
