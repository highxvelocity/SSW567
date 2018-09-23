"""
HW04a: Github Repo Metadata
Author: Chris Corrado
Date: 9/22/2018
"""
import json

import requests

BASE_URL = "https://api.github.com/"


class GitRepo(object):
    """
    The GitRepo object is representative of what we want to know about each repository
    """
    __slots__ = "repo", "commit_list"

    def __init__(self, repo, commit_list):
        self.repo = repo
        self.commit_list = commit_list

    def __str__(self):
        return "Repo: " + self.repo.get("name") + " Number of commits: " + str(len(self.commit_list))


def get_repos_for_user(github_id):
    request = requests.get(BASE_URL + "users/" + github_id + "/repos")
    if request.status_code == 200:
        return json.loads(request.text)
    else:
        return []


def get_commits_for_repo(repo):
    if repo == {}:
        return []
    request = requests.get(BASE_URL + "repos/" + repo.get("owner").get("login") + "/" + repo.get("name") + "/commits")
    if request.status_code == 200:
        return json.loads(request.text)
    else:
        return []


def get_git_repo_list(github_id):
    git_repo_list = []
    repos = get_repos_for_user(github_id)
    for repo in repos:
        git_repo_list.append(GitRepo(repo, get_commits_for_repo(repo)))
    print_repo_results(git_repo_list)
    return git_repo_list


def print_repo_results(git_repo_list):
    """
    Method to print {@link GitRepo} Objects
    :param git_repo_list: List containing GitRepo objects
    """
    for repo in git_repo_list:
        print(repo)
