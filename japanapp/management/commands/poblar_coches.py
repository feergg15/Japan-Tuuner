from django.core.management.base import BaseCommand, CommandError
from japanapp.models import Coche 

import csv



class Command(BaseCommand):
    
    help = "Para poblar la tabla de coches desde un fichero csv"

    def add_arguments(self, parser):
        parser.add_argument("fichero.csv", type=str , help=" ")

    def handle(self, *args, **options):

        csv_filepathname = options['fichero.csv']


        with open(csv_filepathname) as csvfile:
            dataReader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in dataReader:
                coche = Coche()
                coche.año = row[0]
                coche.marca = row[1]
                coche.modelo = row[2]
                coche.estilo = row[3]
                coche.save()

            self.stdout.write(
                self.style.SUCCESS('Ha sido poblado con exito "%s"' % row)
            )