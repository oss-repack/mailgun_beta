import os

from mailgun.client import Client


key = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]
html = """<body style="margin: 0; padding: 0;">
 <table border="1" cellpadding="0" cellspacing="0" width="100%">
  <tr>
   <td>
    Hello!
   </td>
  </tr>
 </table>
</body>"""
client = Client(auth=("api", key))


def post_message():
    # Messages
    # POST /<domain>/messages
    data = {
        "from": os.environ["MESSAGES_FROM"],
        "to": os.environ["MESSAGES_TO"],
        "cc": os.environ["MESSAGES_CC"],
        "subject": "Hello Vasyl Bodaj",
        "html": html,
        "o:tag": "Python test",
    }
    # "text": "Congratulations !!!!!, you just sent an email with Mailgun!  You are truly awesome!"}
    # TODO: Refactor this by using with context manager or pathlib.Path
    files = [
        (
            "attachment",
            ("test1.txt", open("../doc_tests/files/test1.txt", "rb").read()),
        ),
        (
            "attachment",
            ("test2.txt", open("../doc_tests/files/test2.txt", "rb").read()),
        ),
    ]

    req = client.messages.create(data=data, files=files, domain=domain)
    print(req.json())


def post_mime():
    # Mime messages
    # POST /<domain>/messages.mime
    mime_data = {
        "from": os.environ["MESSAGES_FROM"],
        "to": os.environ["MESSAGES_TO"],
        "cc": os.environ["MESSAGES_CC"],
        "subject": "Hello HELLO",
    }
    # TODO: Refactor this by using with context manager or pathlib.Path
    files = {"message": open("../doc_tests/files/test_mime.mime")}

    req = client.mimemessage.create(data=mime_data, files=files, domain=domain)
    print(req.json())


def post_no_tracking():
    # Message no tracking
    data = {
        "from": os.environ["MESSAGES_FROM"],
        "to": os.environ["MESSAGES_TO"],
        "cc": os.environ["MESSAGES_CC"],
        "subject": "Hello Vasyl Bodaj",
        "html": html,
        "o:tracking": False,
    }

    req = client.messages.create(data=data, domain=domain)
    print(req.json())


def post_scheduled():
    # Scheduled message
    data = {
        "from": os.environ["MESSAGES_FROM"],
        "to": os.environ["MESSAGES_TO"],
        "cc": os.environ["MESSAGES_CC"],
        "subject": "Hello Vasyl Bodaj",
        "html": html,
        "o:deliverytime": "Thu Jan 28 2021 14:00:03 EST",
    }

    req = client.messages.create(data=data, domain=domain)
    print(req.json())


def post_message_tags():
    # Message Tags
    data = {
        "from": os.environ["MESSAGES_FROM"],
        "to": os.environ["MESSAGES_TO"],
        "cc": os.environ["MESSAGES_CC"],
        "subject": "Hello Vasyl Bodaj",
        "html": html,
        "o:tag": ["September newsletter", "newsletters"],
    }

    req = client.messages.create(data=data, domain=domain)
    print(req.json())


def resend_message():
    data = {"to": ["spidlisn@gmail.com", "mailgun@2048.zeefarmer.com"]}

    params = {
        "from": os.environ["MESSAGES_FROM"],
        "to": os.environ["MESSAGES_TO"],
        "limit": 1,
    }
    req_ev = client.events.get(domain=domain, filters=params)
    print(req_ev.json())

    req = client.resendmessage.create(
        data=data,
        domain=domain,
        storage_url=req_ev.json()["items"][0]["storage"]["url"],
    )
    print(req.json())


if __name__ == "__main__":
    resend_message()
