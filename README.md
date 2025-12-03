# twtr

## Setup

1. Make a free account and project at [developer.x.com](https://developer.x.com) and get the following keys:

- Bearer Token
- Consumer Key
- Consumer Secret
- Access Token
- Access Token Secret

![](https://github.com/kiankyars/twtr/blob/main/keys.png?raw=true)

2. Add these lines to your `~/.zshrc` or `~/.bashrc`:
> December 2025 update: this is honestly bad practice, so I recommend putting your environment variables in a separate .env file and then exporting that. Nevertheless, you need to somehow expose these keys to the environment.
```sh
export TWEEPY_BEARER_TOKEN="<your_bearer_token>"
export TWEEPY_CONSUMER_KEY="<your_consumer_key>"
export TWEEPY_CONSUMER_SECRET="<your_consumer_secret>"
export TWEEPY_ACCESS_TOKEN="<your_access_token>"
export TWEEPY_ACCESS_TOKEN_SECRET="<your_access_token_secret>"
```
Then reload your config:
```sh
source ~/.zshrc
```
or
```sh
source ~/.bashrc
```

## Usage

Install from PyPI with uv:

```sh
uv tool install twtr
```

Then tweet from the CLI:

```sh
twtr "your tweet here"
```

## Development

Set up the development environment:

```sh
uv sync
```

Run the package locally for testing:

```sh
# Using the entry point script
uv run twtr "your tweet here"

# Or as a Python module
uv run python -m twtr.cli "your tweet here"
```

## Structure
```
.
├── LICENSE
├── README.md
├── keys.png
├── pyproject.toml
├── twtr
│   ├── __init__.py      # Public API (expose main functions/classes)
│   └── cli.py           # CLI entry point (separate from core logic)
└── uv.lock
```