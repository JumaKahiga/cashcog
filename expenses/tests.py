import json

from django.test import Client, TestCase

from .fixtures import hello_world_query

# Create your tests here.
class TestHelloWorld(TestCase):

    @classmethod
    def setUpClass(cls):

        # We need to first run setUpClass function that we
        # inherited from TestCase.
        super(TestHelloWorld, cls).setUpClass()

        # Set up test client for all test classes
        # that will inherit from this class.
        cls.client = Client()

    @classmethod
    def query(cls, query: str = None):
        # Method to run all queries and mutations for tests.
        body = dict()
        body['query'] = query
        response = cls.client.post(
            '/api', json.dumps(body), content_type='application/json')
        json_response = json.loads(response.content.decode())
        return json_response

    def setUp(self):
        pass

    def test_hello_world_endpoint(self):
        response = self.query(hello_world_query)

        self.assertEqual('Hello World', response['data']['response']['message'])

