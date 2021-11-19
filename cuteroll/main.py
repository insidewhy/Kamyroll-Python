import argparse
import sys
from colorama import init
import termcolor
from . import api
from . import downloader
from . import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--login", "-l", type=str, help="Login with ID")
    parser.add_argument(
        "--connect", "-c", action="store_true", help="Login with configured ID"
    )
    parser.add_argument(
        "--bypass",
        "-b",
        action="store_true",
        help="Generate premium access to the catalog",
    )
    parser.add_argument("--search", type=str, help="Search a series, films, episode")
    parser.add_argument("--season", "-s", type=str, help="Show seasons of a series")
    parser.add_argument("--episode", "-e", type=str, help="Show episodes of a season")
    parser.add_argument("--movie", "-m", type=str, help="Show movies from a movie list")
    parser.add_argument(
        "--download", "-d", type=str, help="Download an episode or movie"
    )
    parser.add_argument(
        "--url", "-u", type=str, help="Show m3u8 url of episode or movie"
    )
    parser.add_argument("--playlist", "-p", type=str, help="Download episode list")
    args = parser.parse_args()

    try:
        config = utils.get_config()
    except LookupError as e:
        parser.print_help()
        termcolor.cprint(e, "red")
        sys.exit(0)

    cr_api = api.crunchyroll(config)

    if args.login:
        (username, password) = utils.get_login_form(args.login)
        cr_api.login(username, password, False)
    elif args.connect:
        username = config.get("configuration").get("account").get("email")
        password = config.get("configuration").get("account").get("password")
        if username is None or password is None:
            utils.print_msg("ERROR: No login is configured.", 1)
            sys.exit(0)
        cr_api.login(username, password, False)
    elif args.bypass:
        (username, password) = utils.get_bypass()
        cr_api.login(username, password, True)
    elif args.search:
        cr_api.search(args.search)
    elif args.season:
        cr_api.season(args.season)
    elif args.episode:
        cr_api.episode(args.episode)
    elif args.movie:
        cr_api.movie(args.movie)
    elif args.download:
        cr_dl = downloader.crunchyroll(config)
        if args.playlist:
            cr_dl.download_season(args.download, args.playlist)
        else:
            cr_dl.download(args.download)
    elif args.url:
        cr_dl = downloader.crunchyroll(config)
        cr_dl.url(args.url)
    else:
        parser.print_help()


if __name__ == "__main__":
    init()
    main()
