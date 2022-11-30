from django.test import TestCase
from django.urls import reverse

class test_snack(TestCase):
    def test_status (self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
