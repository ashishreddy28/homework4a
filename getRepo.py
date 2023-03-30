"""
Name:Bala Ashish Yeruva
Subject: SSW 567
HW 05a - Isolate External Dependencies
"""


import requests
import json


def getRepo(username):
    response = requests.get(
        "https://api.github.com/users/" + username + "/repos")

    response = response.json()
    fakeResponse = response
    #print(fakeResponse)

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
