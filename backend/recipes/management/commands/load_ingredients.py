import json
import os
from django.core.management.base import BaseCommand
from recipes.models import Ingredient

FILE_PATH = os.path.join('data', 'ingredients.json')


class Command(BaseCommand):
    help = f'Load ingredients from {FILE_PATH}'

    def handle(self, *args, **kwargs):
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            ingredients = json.load(f)
        for item in ingredients:
            Ingredient.objects.get_or_create(
                name=item['name'],
                measurement_unit=item['measurement_unit']
            )
        self.stdout.write(self.style.SUCCESS(
            f'Loaded {len(ingredients)} ingredients'
        ))
