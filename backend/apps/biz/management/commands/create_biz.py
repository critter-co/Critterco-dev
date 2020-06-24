from biz.models import Biz
from django.core.management.base import BaseCommand
import factory
import random
from django.contrib.gis.geos import Point
from factory.fuzzy import BaseFuzzyAttribute


class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0))


class BizFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Biz

    title = factory.Faker("company")
    description = factory.Faker("bs")
    address = factory.Faker("address")
    city = factory.Faker("city")
    location = FuzzyPoint()


class Command(BaseCommand):
    help = "Creates dummy Posts to seed the database"

    def handle(self, *args, **options):
        bizs = Biz.objects.all()
        if not bizs:
            for i in range(1000):
                biz = BizFactory()
                biz.save()
            print("Created posts")
        else:
            print("Not creating posts")
