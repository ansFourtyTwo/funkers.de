from django.test import TestCase
from django.urls import reverse


class IndexTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get(reverse('doublepower:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doublepower/home.html')
