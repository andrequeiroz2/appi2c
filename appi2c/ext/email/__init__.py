import requests


def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox40c6f90185c24c5da693f89817668e62.mailgun.org/messages",
		auth=("api", "6923648de44ad32d07d197de8037a091-cb3791c4-5ec658df"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox40c6f90185c24c5da693f89817668e62.mailgun.org>",
			"to": "Andre Queiroz <andrequeiroz.com@gmail.com>",
			"subject": "Hello Andre Queiroz",
			"text": "Congratulations Andre Queiroz, you just sent an email with Mailgun!  You are truly awesome!"})