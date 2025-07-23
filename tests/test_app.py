import unittest
from app import create_app
import json
class URLShortenerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_shorten_url(self):
        response = self.app.post('/shorten', json={'url': 'https://example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("short_url", response.get_json())

    def test_redirect(self):
        post_res = self.app.post('/shorten', json={'url': 'https://google.com'})
        short_code = post_res.get_json()["short_url"].split("/")[-1]
        get_res = self.app.get(f"/{short_code}", follow_redirects=False)
        self.assertEqual(get_res.status_code, 302)
        self.assertIn("Location", get_res.headers)

    def test_missing_url(self):
        response = self.app.post('/shorten', json={})
        self.assertEqual(response.status_code, 400)

    def test_invalid_code(self):
        response = self.app.get('/invalid123')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
