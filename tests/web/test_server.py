from unittest import TestCase

from titanic_predictor.web.server import Server


class TestServer(TestCase):

    def test_route_returns_hello_world(self):
        # Given
        titanic_predictor_app = Server().bootstrap().test_client()

        # When
        fetched_data = titanic_predictor_app.get('/').data

        # Then
        self.assertEqual(b'Hello World', fetched_data)
