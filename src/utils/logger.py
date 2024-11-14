import logging
import threading
import time
import sys
from colorama import Fore, Style, init

init()

class Animation:
    def __init__(self):
        self.is_running = False
        self.thread = None
        self.frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.current_msg = ""

    def animate(self):
        i = 0
        while self.is_running:
            sys.stdout.write(f"\r{Fore.LIGHTMAGENTA_EX}{self.frames[i]} {self.current_msg}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
            i = (i + 1) % len(self.frames)

    def start(self, message):
        self.current_msg = message
        self.is_running = True
        self.thread = threading.Thread(target=self.animate)
        self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write("\r" + " " * (len(self.current_msg) + 2) + "\r")
        sys.stdout.flush()


class Formatter(logging.Formatter):
    COLORS = {
        'INFO': Fore.WHITE,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'DEBUG': Fore.LIGHTMAGENTA_EX,
        'SUCCESS': Fore.LIGHTMAGENTA_EX
    }

    SYMBOLS = {
        'INFO': '○',
        'WARNING': '△',
        'ERROR': '✕',
        'DEBUG': '◆',
        'SUCCESS': '◈'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loading_animation = Animation()

    def format(self, record):
        if not hasattr(record, 'color'):
            record.color = self.COLORS.get(record.levelname, '')
        
        if self.loading_animation.is_running and self.loading_animation.thread and self.loading_animation.thread.is_alive():
            self.loading_animation.stop()

        timestamp = self.formatTime(record, '%H:%M:%S')
        
        prefix = f"{Fore.LIGHTMAGENTA_EX}[{timestamp}]{Style.RESET_ALL}"
        
        symbol = self.SYMBOLS.get(record.levelname, '')
        
        formatted_msg = f"{prefix} {record.color}{symbol} {record.msg}{Style.RESET_ALL}"
        record.msg = formatted_msg
        
        return super().format(record)


def setup_logger():
    logger = logging.getLogger('Git')
    logger.setLevel(logging.INFO)

    formatter = Formatter('%(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    def start_loading(self, message):
        self.handlers[0].formatter.loading_animation.start(message)
    
    def stop_loading(self):
        self.handlers[0].formatter.loading_animation.stop()

    logger.start_loading = start_loading.__get__(logger)
    logger.stop_loading = stop_loading.__get__(logger)
    
    return logger