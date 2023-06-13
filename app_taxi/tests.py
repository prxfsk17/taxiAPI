from django.test import TestCase
import unittest
from app_taxi.models import User

# Create your tests here.
class MyTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        print("setUp()")


    def tearDown(self) -> None:
        super().tearDown()
        print("tearDown()")
    def test_no_users(self):
        users = User.objects.all()

        assert len(users) == 3