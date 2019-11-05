from django.test import TestCase

# Create your tests here.

class DummyTest(TestCase):

    def test_one_plus_one(self):
        self.assertEqual(1+1, 2)
        self.assertNotEqual(1+1, 3)
    
    def test_two_plus_two(self):
        self.assertEqual(2+2, 4)
        self.assertNotEqual(2+2, 3)