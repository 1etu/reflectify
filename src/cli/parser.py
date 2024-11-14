import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sync', action='store_true', help='Run in background sync mode')
    return parser

def parse_args():
    parser = create_parser()
    return parser.parse_args() 