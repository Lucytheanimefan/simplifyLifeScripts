import subprocess
import sqlite3
import sys
import nltk

# contact_info: phone number (ie. +19999999999) or apple id
def retrieve_texts(contact_info):
    con = sqlite3.connect("/Users/lucyzhang/Library/Messages/chat.db")
    results = con.execute("select is_from_me,text from message where handle_id=("+
        "select handle_id from chat_handle_join where chat_id=("+
        "select ROWID from chat where guid='iMessage;-;" + contact_info + "')"+
        ")")
    for result in results:
        # Your index is 1, the other person's index is 0
        sender_index, message = result
        tokens = nltk.word_tokenize(message)
        print(tokens)
        if sender_index is 0:
            # do something with your own texts
            continue
        else:# do something with other person's texts
            continue


if __name__ == '__main__':
    retrieve_texts(sys.argv[1])