import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone
from main import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(settings.PHONE, 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)
            for line in phone_reader:
                phone = Phone(
                    id=line[0],
                    name=line[1],
                    image=line[2],
                    price=int(line[3]),
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slugify(line[1])
                )
                phone.save()
                self.stdout.write(f'Запись {phone.name} в БД произведена')
