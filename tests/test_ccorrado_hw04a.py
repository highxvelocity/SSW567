import json
import unittest
from unittest import TestCase

from hw04a.ccorrado_hw04a import get_repos_for_user, get_commits_for_repo, GitRepo


class GitRepoTests(TestCase):

    def test_online_data(self):
        repos = get_repos_for_user("CCorrado")
        commits = get_commits_for_repo(repos[0])
        self.assertTrue(repos != [])
        self.assertTrue(commits != [])

    def test_local_data(self):
        with open("../hw04a/sample_repo_data.json") as file:
            repos = json.load(file)
            self.assertTrue(repos != [])
            with open("../hw04a/sample_commit_data.json") as commit_file:
                commits = json.load(commit_file)
                self.assertTrue(repos[0].get("owner").get("node_id") == commits[0].get("author").get("node_id"))
                git_repo = GitRepo(repos[0], commits)
                print(git_repo)
                self.assertEqual("android-RepeatingAlarm", git_repo.repo.get('name'))
                self.assertEqual(23, len(git_repo.commit_list))


if __name__ == "__main__":
    unittest.main()
