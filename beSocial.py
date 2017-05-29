import subprocess
import applescript


def get_relevant_contacts():
	return




def run():
	applescript.AppleScript('tell application "Messages" \n'+
    'send "Testing" to buddy "chenkaijie0653@126.com" of service "E:spothorse9.lucy@gmail.com"\n'+
	'end tell').run()

if __name__ == '__main__':
	run()