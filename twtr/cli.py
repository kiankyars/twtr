import sys
from twtr import tweet

def main():
    if len(sys.argv) < 2:
        print('Usage: twtr "your tweet"')
        sys.exit(1)
    try:
        tweet(sys.argv[1])
    except RuntimeError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()