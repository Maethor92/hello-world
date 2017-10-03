#!/usr/bin/env python

from flask import Flask, jsonify
import subprocess
import sys

from tasks import searching
import json

from os import listdir
from os.path import isfile, join

app = Flask(__name__)
@app.route('/app/api/v1.0/compute', methods=['GET'])

def program():
	mypath = '/home/ubuntu/Downloads/data/'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	total = {}
	temp = {}
	searchword = ['han', 'hon', 'hen', 'den', 'det', 'denna', 'denne']
	for i in searchword:
		total[i] = 0
		temp[i] = 0

	for element in onlyfiles:
		temp = searching.delay(element).get()
		for i in searchword:
			total[i] = total[i] + temp[i]
			temp[i] = 0
		print total


	return json.dumps(total)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True)
