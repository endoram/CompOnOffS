from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=['GET'])
def mainFunk():
	print("Something")
	data = request.args.get("action")
	
	if (data == "turnOff"):
		subprocess.call(["gnome-session-quit", "--power-off", "--no-prompt", "--force"])
		return("Turnning off")

	if(data == "logOut"):
		subprocess.call(["gnome-session-quit", "--no-prompt", "--force"])
		return("Logging off")
		

	return("Unknown command")


if (__name__ == '__main__'):
	app.run(debug=True, host="192.168.1.138")
