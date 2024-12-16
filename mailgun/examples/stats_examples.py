import os

from mailgun.client import Client


key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]

client = Client(auth=("api", key))


def get_stats_total():
    params = {"event": ["accepted", "delivered", "failed"],
              "duration": "1m"}

    req = client.stats_total.get(filters=params, domain=domain)
    print(req.json())


if __name__ == "__main__":
    get_stats_total()
