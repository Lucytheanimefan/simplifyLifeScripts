import subprocess
import sqlite3

def retrieve_texts(contact_info):
	con = sqlite3.connect("/Users/lucyzhang/Library/Messages/chat.db")
	results = con.execute("select is_from_me,text from message where handle_id=("+
		"select handle_id from chat_handle_join where chat_id=("+
		"select ROWID from chat where guid='iMessage;-;" + contact_info + "')"+
		")")
	for result in results:
		print(result)

	# subprocess.run("sqlite3 ~/Library/Messages/chat.db \""+
	# "select is_from_me,text from message where handle_id=("+
	# "select handle_id from chat_handle_join where chat_id=("+
	# "select ROWID from chat where guid='iMessage;-;" + contact_info + "')"+
	# ")\" | sed 's/1\|/me: /g;s/0\|/budy: /g' > MessageBackup.txt", stdout=subprocess.PIPE)


if __name__ == '__main__':
	retrieve_texts("spothorse9.lucy@gmail.com")