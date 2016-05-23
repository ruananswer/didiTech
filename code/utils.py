import time
import hashlib
import os

def time2slice(timestamp):
	timeArray = time.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
	hour = timeArray.tm_hour
	minute = timeArray.tm_min
	slice = (hour * 60 + minute) / 10
	return slice

def CalcMD5(str):
	md5obj = hashlib.md5()
	md5obj.update(str)
	hash = md5obj.hexdigest()
	return hash

def fetch_file_list(file_path):
	file_list = []
	for root, dirs, files in os.walk(file_path):
		for curr_file in files:
			file_name = os.path.join(root, curr_file)
			file_list.append(curr_file)
	return file_list

