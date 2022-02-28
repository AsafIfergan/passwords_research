from utils import TxtFileParser
import argparse

parser = argparse.ArgumentParser(description="Parse files")
parser.add_argument("-f", "--file", help="Path to a file", required=True)
args = parser.parse_args()

parser = TxtFileParser(args.file)
parser.parse()
