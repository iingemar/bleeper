from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.

# Run 'python manage.py test'

from .models import Bleep


User = get_user_model()


class BleepTestModelCase(TestCase):
    def setUp(self):
        User.objects.create(username='test_user2000')

    def test_bleep_item(self):
        obj = Bleep.objects.create(
            user=User.objects.first(),
            content='Random content'
        )
        self.assertTrue(obj.content == 'Random content')
        self.assertTrue(obj.id == 1)
        self.assertEqual(obj.id, 1)
        absolute_url = reverse('bleeps:bleep_detail_view', kwargs={'pk' : 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_bleep_url(self):
        obj = Bleep.objects.create(
            user=User.objects.first(),
            content='Random content'
        )
        absolute_url = reverse('bleeps:bleep_detail_view', kwargs={'pk' : obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
