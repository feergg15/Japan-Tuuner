from django.core.management.base import BaseCommand, CommandError
from japanapp.models import Coche 

import csv


class Command(BaseCommand):
    
    help = "Para poblar la tabla de coches desde un fichero csv"

    def add_arguments(self, parser):
        parser.add_argument("fichero.csv", type=str , help="/home/fernando/Escritorio/TRABAJOS_2ASIR/IAW/csv/escape.csv")

    def handle(self, *args, **options):

        csv_filepathname = options['fichero.csv']


        with open(csv_filepathname) as csvfile:
            dataReader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in dataReader:
                escape = Escape()
                escape.año = row[0]
                escape.marca = row[1]
                escape.modelo = row[2]
                escape.estilo = row[3]
                escape.save()

            self.stdout.write(
                self.style.SUCCESS('Ha sido poblado con exito "%s"' % row)
            )