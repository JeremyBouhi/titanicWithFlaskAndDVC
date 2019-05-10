from unittest import TestCase
from unittest.mock import patch

from titanic_predictor.web.server import Server


class TestServer(TestCase):

    def test_route_returns_hello_world(self):
        # Given
        titanic_predictor_app = Server().bootstrap().test_client()

        # When
        fetched_data = titanic_predictor_app.get('/').data

        # Then
        self.assertEqual(b'Hello World', fetched_data)

#    def test_predict_route_returns_a_prediction(self):
        # Given
#        titanic_predictor_app = Server().bootstrap().test_client()

        # When
#        fetched_prediction = titanic_predictor_app.post('/predict').json.get('predictions')

        # Then
#        self.assertTrue(isinstance(fetched_prediction, float))

    @patch('titanic_predictor.web.server.compute_prediction')
    def test_predict_route_returns_expected_prediction(self, patch_compute_prediction):
        # Given
        titanic_predictor_app = Server().bootstrap().test_client()
        patch_compute_prediction.return_value = [17]

        # When
        fetched_prediction = titanic_predictor_app.post('/predict').json.get('predictions')

        # Then
        self.assertEqual(17, fetched_prediction)
