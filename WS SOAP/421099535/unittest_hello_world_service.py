import unittest
from hello_world_service import HelloWorldService

class TestHelloWorldService(unittest.TestCase):
    def test_say_hello(self):
        service = HelloWorldService()
        response = service.say_hello(None,'World', 3)
        self.assertEqual(response, 'Hello, WorldWorldWorld')

if __name__ == '__main__':
    unittest.main()