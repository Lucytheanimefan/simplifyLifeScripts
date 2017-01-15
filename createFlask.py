import subprocess
import sys

pathRoot = "/Users/lucyzhang/github/"

def createFlask():
	print "Create a flask app? (y/n)"
	userInput = sys.stdin.readline().strip()
	if (userInput == 'y'):
		print "Name of project folder: "
		appName = sys.stdin.readline().strip()
		appRoot = pathRoot + appName
		print "Making a folder in "+appRoot
		subprocess.call(["mkdir",appRoot])
		print "Making internal folders and files"
		subprocess.call(["mkdir",appRoot+"/static"])
		subprocess.call(["mkdir",appRoot+"/static/css"])
		subprocess.call(["touch",appRoot+"/static/css/style.css"])
		subprocess.call(["mkdir",appRoot+"/static/js"])
		subprocess.call(["touch",appRoot+"/static/js/script.js"])
		subprocess.call(["mkdir",appRoot+"/static/img"])
		subprocess.call(["mkdir",appRoot+"/static/plugins"])
		subprocess.call(["mkdir",appRoot+"/templates"])
		subprocess.call(["touch",appRoot+"/templates/index.html"])
		#subprocess.call(["touch",appRoot+"/app.py"])
		f = open(appRoot+"/app.py", "w")
		subprocess.call(["echo", "from flask import Flask, render_template\napp = Flask(__name__)\nif __name__ == \"__main__\":\n	port = int(os.environ.get(\"PORT\", 5000))\n	app.run(host='0.0.0.0', port=port)"], stdout=f)
		#subprocess.call(["touch",appRoot+"/Procfile"])
		p=open(appRoot+"/Procfile","w")
		subprocess.call(["echo","web: python app.py"],stdout=p)
		subprocess.call(["cd",appRoot])
		print "Creating virtualenv"
		subprocess.call(["virtualenv", appRoot+"/venv"])
		subprocess.call(["touch", appRoot+"/requirements.txt"])
		print "Would you like to initialize your git repo here? (y/n)"
		gitrepo = sys.stdin.readline().strip()
		if (gitrepo=="y"):
			appRoot = appRoot+"/"
			print appRoot
			print "Please input the git repo URL:"
			remoteURL = sys.stdin.readline().strip()
			p1=subprocess.Popen(["git","init"],cwd=appRoot)
			p1.wait()
			p2=subprocess.Popen(["git","add","-A"],cwd=appRoot)
			p2.wait()
			p3=subprocess.Popen(["git","config","user.email","spothorse9.lucy@gmail.com"],cwd=appRoot)
			p3.wait()
			p4=subprocess.Popen(["git","commit","-am","Added files"],cwd=appRoot)
			p4.wait()
			p5=subprocess.Popen(["git","remote","add","origin",remoteURL],cwd=appRoot)
			p5.wait()
			p6=subprocess.Popen(["git","push","-u","origin","master"],cwd=appRoot)
			p6.wait()
			print("Pushed code to repo")
		elif (gitrepo=="n"):
			print "Done"
			return
	elif (userInput=="n"):
		print "Bye"


if __name__ == "__main__":
    createFlask()
