"""
Name: Ashish Reddy Yeruva
Cwid:20012794
Subject: SSW - 567 WC
HW 04a Homework 04a
"""

import requests
import json


def getRepo(username):
    response = requests.get(
        "https://api.github.com/users/" + username + "/repos")

    response = response.json()

    if len(response) == 0:
        print("No Repos Found")
        return False

    for repo in response:
        repoResponse = requests.get(repo['commits_url'].split("{")[0])
        repoResponse = repoResponse.json()
        print("Name of Repo: " +
              repo['name'] + " \n Number of commits: " + str(len(repoResponse)))

    return True


if __name__ == "__main__":
    userInput = input("Enter Github Username: ")
    getRepo(userInput)
