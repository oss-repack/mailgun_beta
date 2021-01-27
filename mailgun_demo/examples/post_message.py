import requests
import json

def send_simple_message():
	data = {"from": "Stepan Pidlisnyi <mailgun@2048.zeefarmer.com>",
			"to": "Vasyl Bodaj <diskovodik@gmail.com>",
			"subject": "Hello Vasyl Bodaj",
			"text": "Congratulations Vasyl Bodaj, you just sent an email with Mailgun!  You are truly awesome!"}
	req = requests.post(
		"https://api.mailgun.net/v3/2048.zeefarmer.com/messages",
		auth=("api", "key-578f9790b7d06fd46a104f8156ed6995"),
		data=data,
		params=None)
	print(req.json())



if __name__ == '__main__':
    send_simple_message()