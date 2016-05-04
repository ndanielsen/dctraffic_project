from django.test import TestCase
from django.contrib.gis.geos import Point

import factory.django, random
from factory.fuzzy import BaseFuzzyAttribute
from faker import Faker
import pytest

from .models import ParkingViolation

pytestmark = pytest.mark.django_db


fake = Faker()
fake.seed(4321)

class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0),
                     random.uniform(-90.0, 90.0))

# Factories for tests
class ParkingViolationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ParkingViolation
        django_get_or_create = (
             'location',
             'objectid',
             'rowid',
             'holiday',
             'violation_code',
             'violation_description',
             'address',
             'rp_plate_state',
             'body_style',
             'address_id',
             'streetsegid',
             'xcoord',
             'ycoord',
             'filename',
             'ticket_issue_datetime')
    location = FuzzyPoint()
    objectid = random.randint(1,2000)
    rowid = random.randint(1,2000)
    holiday = bool(random.getrandbits(1))
    violation_code = 'P001'
    violation_description = fake.text(max_nb_chars=200)
    address = fake.address()
    rp_plate_state = 'MD'
    body_style = 'TK'
    address_id = random.randint(1,2000)
    streetsegid = random.uniform(1, 9000)
    xcoord = random.randint(1,2000)
    ycoord = random.randint(1,2000)
    filename = fake.file_name(category=None, extension='csv')
    ticket_issue_datetime = '2011-07-06T16:09:00.000Z'

@pytest.mark.django_db
class ParkingViolationTest(TestCase):
    pytestmark = pytest.mark.django_db

    def setUp(self):
        self.violation = ParkingViolationFactory()

    def test_creation(self):
        self.assertTrue(isinstance(self.violation, ParkingViolation))

    def test_verbose_name_plural(self):
        self.assertEqual(str(ParkingViolation._meta.verbose_name_plural), "Parking Violations")

    def test_string_representation(self):
        self.assertEqual(str(self.violation), self.violation.ticket_issue_datetime)

    def test_create_violation(self):
        # Check we can find it
        all_violations = ParkingViolation.objects.all()
        self.assertEqual(len(all_violations), 1)
        only_violation = all_violations[0]
        self.assertEqual(only_violation, self.violation)
        # Check attributes
        self.assertEqual(only_violation.body_style, 'TK')
        self.assertEqual(only_violation.rp_plate_state, 'MD')
