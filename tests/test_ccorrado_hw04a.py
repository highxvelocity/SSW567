import json
import unittest
from unittest import TestCase

from hw04a.ccorrado_hw04a import get_repos_for_user, get_commits_for_repo, GitRepo


class GitRepoTests(TestCase):

    def test_online_data(self):
        """
        This unit test will make 2 network requests
        1. Get Repos for User "CCorrado"
        2. Get Commits for the first Repository in the list\
        Assert that neither list is empty.
        """
        repos = get_repos_for_user("CCorrado")
        commits = get_commits_for_repo(repos[0])
        self.assertTrue(repos != [])
        self.assertTrue(commits != [])

    def test_local_data(self):
        """
        This test is more of an integration test.
        It is meant to assert that the repository data and commit data are compatible with the GitRepo model class.
        Assert that the repo data file is not empty.
        Assert that the owner of the first repo matches the author of the first commit on the first repo.
        Assert that the name is equal to the name of the first repo in the sample file.
        Assert that the length of the commit list is 23.
        """
        with open("./hw04a/sample_repo_data.json") as file:
            repos = json.load(file)
            self.assertTrue(repos != [])
            with open("./hw04a/sample_commit_data.json") as commit_file:
                commits = json.load(commit_file)
                self.assertTrue(repos[0].get("owner").get("node_id") == commits[0].get("author").get("node_id"))
                git_repo = GitRepo(repos[0], commits)
                print(git_repo)
                self.assertEqual("android-RepeatingAlarm", git_repo.repo.get('name'))
                self.assertEqual(23, len(git_repo.commit_list))


if __name__ == "__main__":
    unittest.main()
