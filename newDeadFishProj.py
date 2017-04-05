import subprocess
import sys

appRoot = "/Users/lucyzhang/Github/deadfisheyed"
def createNewProj():
	print "Name of project:"
	project = sys.stdin.readline().strip()
	print "Making css folder"
	subprocess.call(["mkdir",appRoot+"/static/css/"+project])
	subprocess.call(["touch",appRoot+"/static/css/"+project+"/style.css"])
	print "Making js"
	subprocess.call(["mkdir",appRoot+"/static/js/"+project])
	subprocess.call(["touch",appRoot+"/static/js/"+project+"/script.js"])
	print "Making template"
	subprocess.call(["mkdir",appRoot+"/templates/"+project])
	subprocess.call(["touch",appRoot+"/templates/"+project+"/index.html"])
	print "Make img folder? (y/n)"
	userInput = sys.stdin.readline().strip()
	if (userInput == 'y'):
		subprocess.call(["mkdir",appRoot+"/static/img/"+project])
	else:
		print "done"
	print "done"

if __name__ == '__main__':
	createNewProj()
