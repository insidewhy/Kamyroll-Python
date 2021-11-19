import sys
import requests
from . import extractor
from . import utils


class crunchyroll:
    def __init__(self, config):
        self.config = config

    def login(self, username, password):
        session = utils.get_session(self.config)

        data = {
            "username": username,
            "password": password,
            "grant_type": "password",
            "scope": "offline_access",
        }

        session.headers.update(utils.get_authorization(self.config, False))
        r = session.post(
            "https://beta-api.crunchyroll.com/auth/v1/token", data=data
        ).json()

        if utils.get_error(r):
            sys.exit(1)

        access_token = r.get("access_token")
        refresh_token = r.get("refresh_token")
        token_type = r.get("token_type")
        authorization = {"Authorization": "{} {}".format(token_type, access_token)}
        account_id = r.get("account_id")

        headers = utils.get_headers(self.config)
        headers.update(authorization)
        session.headers = headers

        r = session.get("https://beta-api.crunchyroll.com/accounts/v1/me").json()
        if utils.get_error(r):
            sys.exit(1)

        external_id = r.get("external_id")

        r = session.get(
            "https://beta-api.crunchyroll.com/accounts/v1/me/profile"
        ).json()
        if utils.get_error(r):
            sys.exit(1)

        email = r.get("email")
        username = r.get("username")

        r = session.get("https://beta-api.crunchyroll.com/index/v2").json()
        if utils.get_error(r):
            sys.exit(1)

        cms = r.get("cms")
        bucket = cms.get("bucket")
        policy = cms.get("policy")
        signature = cms.get("signature")
        key_pair_id = cms.get("key_pair_id")
        expires = cms.get("expires")

        json_token = self.config.get("configuration").get("token")
        json_token["refresh_token"] = refresh_token
        json_token["bucket"] = bucket
        json_token["policy"] = policy
        json_token["signature"] = signature
        json_token["key_pair_id"] = key_pair_id
        json_token["expires"] = expires
        self.config.get("configuration")["token"] = json_token

        json_account = self.config.get("configuration").get("account")
        json_account["account_id"] = account_id
        json_account["external_id"] = external_id
        json_account["email"] = email
        json_account["password"] = password
        json_account["username"] = username
        self.config.get("configuration")["account"] = json_account

        utils.print_msg("[debug] Connected account: [{}]".format(email), 0)
        utils.save_config(self.config)

    def search(self, query):
        authorization = utils.get_authorization(self.config, True)
        self.config = utils.get_config()
        headers = utils.get_headers(self.config)
        headers.update(authorization)

        session = utils.get_session(self.config)
        session.headers = headers

        params = {"q": str(query), "n": "6", "locale": utils.get_locale(self.config)}

        r = session.get(
            "https://beta-api.crunchyroll.com/content/v1/search", params=params
        ).json()
        if utils.get_error(r):
            sys.exit(1)

        items = r.get("items")
        for item in items:
            extractor.search(item, self.config)

    def season(self, series_id):
        (policy, signature, key_pair_id) = utils.get_token(self.config)
        self.config = utils.get_config()

        params = {
            "series_id": series_id,
            "Policy": policy,
            "Signature": signature,
            "Key-Pair-Id": key_pair_id,
            "locale": utils.get_locale(self.config),
        }

        endpoint = "https://beta-api.crunchyroll.com/cms/v2{}/seasons".format(
            self.config.get("configuration").get("token").get("bucket")
        )
        r = requests.get(endpoint, params=params).json()

        if utils.get_error(r):
            sys.exit(1)

        extractor.season(r, series_id)

    def episode(self, season_id):
        (policy, signature, key_pair_id) = utils.get_token(self.config)
        self.config = utils.get_config()

        params = {
            "season_id": season_id,
            "Policy": policy,
            "Signature": signature,
            "Key-Pair-Id": key_pair_id,
            "locale": utils.get_locale(self.config),
        }

        endpoint = "https://beta-api.crunchyroll.com/cms/v2{}/episodes".format(
            self.config.get("configuration").get("token").get("bucket")
        )
        r = requests.get(endpoint, params=params).json()
        if utils.get_error(r):
            sys.exit(1)

        extractor.episode(r, season_id, self.config)

    def movie(self, movie_id):
        (policy, signature, key_pair_id) = utils.get_token(self.config)
        self.config = utils.get_config()

        params = {
            "movie_listing_id": movie_id,
            "Policy": policy,
            "Signature": signature,
            "Key-Pair-Id": key_pair_id,
            "locale": utils.get_locale(self.config),
        }

        endpoint = "https://beta-api.crunchyroll.com/cms/v2{}/movies".format(
            self.config.get("configuration").get("token").get("bucket")
        )
        r = requests.get(endpoint, params=params).json()

        if utils.get_error(r):
            sys.exit(1)

        extractor.movie(r, movie_id, self.config)
