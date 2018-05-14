import requests


POST_URL = 'http://anonymouse.org/cgi-bin/anon-email.cgi'
#POST_BODY = {'to':None, 'subject':None, 'text':None}

# Messages with same content can only be sent once, so make it different with 0 width space
def pad_zero_width(text, num):
	return text + num*'\u200b'


def send(subject, message, receiver):
	POST_BODY = {'to':receiver, 'subject':subject, 'text':message}
	r = requests.post(POST_URL, data=POST_BODY)
	print(r.status_code, r.reason)


def go_crazy(subject, message, receiver, num=100): 
	if isinstance(subject, str) and isinstance(message, str) and isinstance(receiver, str):
		for i in range(num):
			send(subject + ' ' + str(i), pad_zero_width(message, i), receiver)
	elif isinstance(subject, list) and isinstance(message, list): 
		for i in range(num):
			if i < len(subject):
				print(i)
				send(subject[i] + ' ' + str(i), pad_zero_width(message[i], i), receiver)
	else:
		print('Can\'t go crazy')

if __name__ == '__main__':
	go_crazy('Pad test weekend2', 'try again weekend2', 'lz107@duke.edu', 7)