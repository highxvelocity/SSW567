import json
import unittest
from unittest import TestCase
from unittest.mock import patch

from hw04a.ccorrado_hw04a import GitRepo, print_repo_results


class GitRepoTests(TestCase, object):

    @classmethod
    def setUpClass(cls):
        cls.mock_get_repo_patch = patch('hw04a.ccorrado_hw04a.get_repos_for_user')
        cls.mock_get_repo = cls.mock_get_repo_patch.start()

        with open("./hw04a/sample_repo_data.json") as file:
            cls.mock_get_repo.return_value = json.load(file)

        cls.mock_get_commits_patch = patch('hw04a.ccorrado_hw04a.get_commits_for_repo')
        cls.mock_get_commits = cls.mock_get_commits_patch.start()

        with open("./hw04a/sample_commit_data.json") as commit_file:
            cls.mock_get_commits.return_value = json.load(commit_file)

    @classmethod
    def tearDownClass(cls):
        cls.mock_get_commits_patch.stop()
        cls.mock_get_repo_patch.stop()

    def test_online_data(self):
        """
        This unit test will make 4 network requests
        Modification, Methods that depend on the network will be mocked.

        1. Get Repos for User "CCorrado"
        2. Get Commits for the first Repository in the list
        Assert that neither list is empty.
        """
        repos = self.mock_get_repo("CCorrado")
        self.assertTrue(repos != [])

        git_repos = []
        git_repo = GitRepo(repos[0], self.mock_get_commits(repos[0]))
        git_repos.append(git_repo)
        self.assertTrue(git_repo.repo != [])
        self.assertTrue(git_repo.commit_list != [])

        print_repo_results(git_repos)

    def test_local_data(self):
        """
        This test is more of an integration test.
        It is meant to assert that the repository data and commit data are compatible with the GitRepo model class.
        Assert that the repo data file is not empty.
        Assert that the owner of the first repo matches the author of the first commit on the first repo.
        Assert that the name is equal to the name of the first repo in the sample file.
        Assert that the length of the commit list is 23.
        """
        repos = self.mock_get_repo("CCorrado")
        self.assertTrue(repos != [])

        commits = self.mock_get_commits(repos[0])
        self.assertTrue(repos[0].get("owner").get("node_id") == commits[0].get("author").get("node_id"))

        git_repo = GitRepo(repos[0], commits)
        print(git_repo)

        self.assertEqual("android-RepeatingAlarm", git_repo.repo.get('name'))
        self.assertEqual(23, len(git_repo.commit_list))


if __name__ == "__main__":
    unittest.main()
