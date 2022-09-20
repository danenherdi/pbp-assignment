from django.test import TestCase, Client

# Create your tests here.
class MyWatchlistTest(TestCase):
    def test_mywatchlist_html_response(self):
        response = Client().get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)
    
    def test_mywatchlist_xml_response(self):
        response = Client().get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)
    
    def test_mywatchlist_json_response(self):
        response = Client().get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)

# Referensi : https://docs.djangoproject.com/en/4.1/topics/testing/tools/