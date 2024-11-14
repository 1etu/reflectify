from api.github_api import GitHubAPI
from config.config import GITHUB_USERNAME
from utils.logger import setup_logger
from utils.file_handler import FileHandler
from services.follow_service import FollowService
from cli.parser import parse_args
from config.constants import (
    SYNC_INTERVAL,
    RETRY_DELAY,
    FOLLOWERS_FILE,
    FOLLOWING_FILE,
    FOLLOWED_BACK_FILE
)
import time
import threading

class Reflectify:
    def __init__(self):
        self.api = GitHubAPI()
        self.logger = setup_logger()
        self.file_handler = FileHandler()
        self.follow_service = FollowService(self.api, self.logger)
        self.is_syncing = False
        self.sync_thread = None

    def start_sync(self):
        self.is_syncing = True
        self.sync_thread = threading.Thread(target=self._sync_loop)
        self.sync_thread.daemon = True
        self.sync_thread.start()

    def stop_sync(self):
        self.is_syncing = False
        if self.sync_thread:
            self.sync_thread.join()

    def _sync_loop(self):
        while self.is_syncing:
            try:
                followers, following, followed_back = self.update_files()
                self.follow_service.follow_new_followers(followers, following)
                self.follow_service.unfollow_non_followers(followers, following)
                time.sleep(SYNC_INTERVAL)
            except Exception as e:
                self.logger.error(f"Sync error: {str(e)}")
                time.sleep(RETRY_DELAY)

    def update_files(self):
        self.logger.start_loading("Fetching profile data...")
        followers = self.api.get_followers(GITHUB_USERNAME)
        following = self.api.get_following(GITHUB_USERNAME)
        self.logger.stop_loading()
        
        followed_back = list(set(followers) & set(following))
        
        self.file_handler.write_list_to_file(FOLLOWERS_FILE, followers)
        self.file_handler.write_list_to_file(FOLLOWING_FILE, following)
        self.file_handler.write_list_to_file(FOLLOWED_BACK_FILE, followed_back)

        self.logger.info(f"Found {len(followers)} followers")
        self.logger.info(f"Following {len(following)} users")
        self.logger.info(f"Mutual follows: {len(followed_back)}")

        return followers, following, followed_back

    def run(self, sync_mode=False):
        try:
            if sync_mode:
                self.start_sync()
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    self.stop_sync()
            else:
                followers, following, followed_back = self.update_files()
                self.follow_service.follow_new_followers(followers, following)
                self.follow_service.unfollow_non_followers(followers, following)
                self.update_files()
                
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    args = parse_args()
    bot = Reflectify()
    bot.run(sync_mode=args.sync)