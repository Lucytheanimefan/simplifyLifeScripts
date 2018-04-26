from bs4 import BeautifulSoup
import requests

POST_URL = 'http://anonymouse.org/cgi-bin/anon-email.cgi'
#POST_BODY = {'to':None, 'subject':None, 'text':None}

def send(subject, message, receiver):
	POST_BODY = {'to':receiver, 'subject':subject, 'text':message}
	r = requests.post(POST_URL, data=POST_BODY)
	print(r.status_code, r.reason)


def go_crazy(subject, message, receiver, num=100): 
	if isinstance(subject, str) and isinstance(message, str) and isinstance(receiver, str):
		for i in range(num):
			send(subject, message, receiver)
	elif isinstance(subject, list) and isinstance(message, list): 
		for i in range(num):
			if i < len(subject):
				print(i)
				send(subject[i] + ' ' + str(i), message[i], receiver)
	else:
		print('Can\'t go crazy')

if __name__ == '__main__':
	go_crazy('List test', 'go crazy test', '<EMAIL HERE>', 10)