# Testing python_repos_visual.py
import unittest
import requests

class ApiTestCase(unittest.TestCase):
    """Testing GitHub API Requests"""

    def setUp(self):
        url = ('https://api.github.com/search/repositories?'
               'q=language:python&sort=stars')
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers=headers)
        self.response_dict = r.json()
        self.status_code = r.status_code

    def test_status_code(self):
        """Testing the response with a code 200"""
        self.assertEqual(self.status_code, 200)
    
    def test_numbers_of_repositories(self):
        """Testing the return of 30 repositories"""
        items = self.response_dict['items']
        self.assertEqual(len(items), 30)

    def test_total_count_exceeds_threshold(self):
        """Checks that the total number of repositories"""
        """exceeds a million."""
        total = self.response_dict['total_count']
        self.assertGreater(total, 1000000)

if __name__ == "__main__":
    unittest.main()
