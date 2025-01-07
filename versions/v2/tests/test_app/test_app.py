#!/usr/bin/python3
"""
test_app : to test app module
"""
import unittest
import sys
import os
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../web_flask')))


from web_flask.app import app

class TestAppRunning(unittest.TestCase):
    def setUp(self):
        """Setup for the tests."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_app_can_run(self):
        """Test if the app can run without any issues."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        """Teardown after tests are run."""
        pass

if __name__ == '__main__':
    unittest.main()
