import requests
from config.config import GITHUB_TOKEN

class GitHubAPI:
    def __init__(self):
        self.headers = {
            'Authorization': f'token {GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = 'https://api.github.com'

    def get_followers(self, username):
        response = requests.get(
            f'{self.base_url}/users/{username}/followers',
            headers=self.headers
        )
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, list):
            raise ValueError("Unexpected API response format")
        return [user.get('login') for user in data if isinstance(user, dict)]

    def get_following(self, username):
        response = requests.get(
            f'{self.base_url}/users/{username}/following',
            headers=self.headers
        )
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, list):
            raise ValueError("Unexpected API response format")
        return [user.get('login') for user in data if isinstance(user, dict)]

    def follow_user(self, username):
        response = requests.put(
            f'{self.base_url}/user/following/{username}',
            headers=self.headers
        )
        return response.status_code == 204

    def unfollow_user(self, username):
        response = requests.delete(
            f'{self.base_url}/user/following/{username}',
            headers=self.headers
        )
        return response.status_code == 204