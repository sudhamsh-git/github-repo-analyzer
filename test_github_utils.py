# test_github_utils.py
import unittest
from unittest.mock import patch
from github_utils import fetch_repo_metadata, fetch_contributors, fetch_commits

class TestGithubUtils(unittest.TestCase):
    @patch('github_utils.requests.get')
    def test_fetch_repo_metadata_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'name': 'test-repo'}
        
        result = fetch_repo_metadata('test-owner', 'test-repo')
        self.assertEqual(result['name'], 'test-repo')
    
    @patch('github_utils.requests.get')
    def test_fetch_repo_metadata_error(self, mock_get):
        mock_get.return_value.raise_for_status.side_effect = Exception("API Error")
        
        result = fetch_repo_metadata('test-owner', 'test-repo')
        self.assertIn('error', result)
    
    @patch('github_utils.requests.get')
    def test_fetch_contributors_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'login': 'user1'}]
        
        result = fetch_contributors('test-owner', 'test-repo')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['login'], 'user1')
    
    @patch('github_utils.requests.get')
    def test_fetch_commits_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'commit': {'message': 'test commit'}}]
        
        result = fetch_commits('test-owner', 'test-repo')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['commit']['message'], 'test commit')

if __name__ == '__main__':
    unittest.main()
