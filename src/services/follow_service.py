import time
from config.constants import RATE_LIMIT_DELAY

class FollowService:
    def __init__(self, api, logger):
        self.api = api
        self.logger = logger

    def follow_new_followers(self, followers, following):
        to_follow = set(followers) - set(following)
        
        for username in to_follow:
            if self.api.follow_user(username):
                self.logger.info(f"Successfully followed {username}")
            else:
                self.logger.error(f"Failed to follow {username}")
            time.sleep(RATE_LIMIT_DELAY)

    def unfollow_non_followers(self, followers, following):
        to_unfollow = set(following) - set(followers)
        
        for username in to_unfollow:
            if self.api.unfollow_user(username):
                self.logger.info(f"Successfully unfollowed {username}")
            else:
                self.logger.error(f"Failed to unfollow {username}")
            time.sleep(RATE_LIMIT_DELAY)
