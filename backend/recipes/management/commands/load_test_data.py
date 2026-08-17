from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from recipes.models import Tag, Ingredient, Recipe, RecipeIngredient

User = get_user_model()


class Command(BaseCommand):
    help = 'Load test data'

    def handle(self, *args, **kwargs):
        tags = [
            {'name': 'Завтрак', 'slug': 'breakfast'},
            {'name': 'Обед', 'slug': 'lunch'},
            {'name': 'Ужин', 'slug': 'dinner'},
        ]
        for tag in tags:
            Tag.objects.get_or_create(**tag)

        user1, _ = User.objects.get_or_create(
            email='user1@example.com',
            username='user1',
            first_name='Иван',
            last_name='Иванов'
        )
        user1.set_password('user12345')
        user1.save()

        user2, _ = User.objects.get_or_create(
            email='user2@example.com',
            username='user2',
            first_name='Петр',
            last_name='Петров'
        )
        user2.set_password('user12345')
        user2.save()

        ingredients_data = [
            {'name': 'Картофель', 'measurement_unit': 'г', 'amount': 500},
            {'name': 'Молоко', 'measurement_unit': 'мл', 'amount': 200},
        ]

        recipe = Recipe.objects.create(
            author=user1,
            name='Картофельное пюре',
            text='Простой рецепт пюре.',
            cooking_time=30,
        )
        recipe.tags.set([Tag.objects.get(slug='lunch')])
        for ing in ingredients_data:
            ingredient, _ = Ingredient.objects.get_or_create(
                name=ing['name'],
                measurement_unit=ing['measurement_unit']
            )
            RecipeIngredient.objects.create(
                recipe=recipe,
                ingredient=ingredient,
                amount=ing['amount']
            )

        self.stdout.write(self.style.SUCCESS('Test data loaded'))
