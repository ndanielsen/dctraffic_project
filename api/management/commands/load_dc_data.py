from collections import namedtuple
import csv, os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point

from api.models import ParkingViolation

class Command(BaseCommand):

    def __init__(self):
        self.parking_file = os.path.join(settings.BASE_DIR, 'api/fixtures/parking_violations_sample.csv')
        super(Command, self).__init__()

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('parking')


    def handle(self, *args, **options):
        # ...
        if options['parking']:
            Parking = namedtuple('Parking', 'x, y, objectid, rowid, holiday, violation_code, \
                                violation_description, location, rp_plate_state, body_style, \
                                address_id, streetsegid, xcoord, ycoord, filename, \
                                ticket_issue_datetime')


            for violation in map(Parking._make, csv.reader(open(self.parking_file, "rb"), delimiter='\t'))[1:]:

                obj = ParkingViolation(
                        location = Point((float(violation.x), float(violation.y))),
                        objectid = violation.objectid,
                        rowid = violation.rowid,
                        holiday = violation.holiday,
                        violation_code = violation.violation_code,
                        violation_description = violation.violation_description,
                        address = violation.location,
                        rp_plate_state = violation.rp_plate_state,
                        body_style = violation.body_style,
                        address_id = violation.address_id,
                        streetsegid = violation.streetsegid,
                        xcoord = violation.xcoord,
                        ycoord = violation.ycoord,
                        filename = violation.filename,
                        ticket_issue_datetime = violation.ticket_issue_datetime,
                        )
                obj.save()

            self.stdout.write(self.style.SUCCESS('All Loaded'))
