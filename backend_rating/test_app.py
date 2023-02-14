import unittest
from app import app
import model as md

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_prediction(self):
        # Succeed in predicting for a test example : score must be better or equal from the previous model
        response = self.app.post('/', json=md.test_predict["params"])
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(response.json["rating"], md.test_predict["result"])

        # Must at least have one anime information --> return 500
        response = self.app.post('/')
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()