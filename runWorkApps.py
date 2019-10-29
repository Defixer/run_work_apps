#!/usr/local/bin/python
import subprocess, signal
import time
import os

x_lite = '/Applications/X-Lite.app'
simple_note = '/Applications/Simplenote.app'
sublime = '/Applications/Sublime Text.app'
slack = '/Applications/Slack.app'
google_chat = '/Applications/Chat.app'
viber = '/Applications/Viber.app'
google_chrome = '/Applications/Google Chrome.app'
desktime = '/Applications/DeskTime.app'
apps = [desktime, x_lite, simple_note,sublime, slack, google_chat, viber, google_chrome]

qBittorrent = 'qbittorrent'
brave_browser = 'Brave Browser'

def run(apps):
	for app in apps:
		subprocess.Popen(["open", app])
#Close a running external app
def terminate(app):
	#Get all running processes
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)

	#Transform result into string
	out, err = p.communicate()

	#Traverse through all running process by line
	for line in out.splitlines():
		#Search for app by name for each running process
		if app.encode() in line:
			#Get PID of matching app
			pid = int(line.split(None, 1)[0])
			#Terminate app by PID
			os.kill(pid, signal.SIGKILL)

def press_any_key():
	input("Press any key...")

def myMain():
	terminate(qBittorrent)
	terminate(brave_browser)
	run(apps)

myMain()