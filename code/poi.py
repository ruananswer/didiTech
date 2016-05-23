from collections import defaultdict
from utils import *
import hashlib

def process(poi_file):
	file_handle = open(poi_file, 'r')
	poi_dict = {}
	for line in file_handle:
		data_list = line.strip('\n').split('\t')
		poi_dict[data_list[0]] = {}
		for ii in range(1, len(data_list)):
			category, size = data_list[ii].split(':')
			size = int(size)
			md5 = CalcMD5(category)
			poi_dict[data_list[0]][md5] = size
	file_handle.close()
	return poi_dict

def merge_dict(poi_dict):
	poi_list = []
	for area_id in poi_dict:
		for md5 in poi_dict[area_id]:
			if md5 not in poi_list:
				poi_list.append(md5)
	return poi_list

def poi_write(poi_format_file, poi_dict, poi_list):
	file_handle = open(poi_format_file, 'w')
	for area_id in poi_dict:
		file_handle.write('%s\t'%area_id)
		for md5 in poi_list:
			if md5 not in poi_dict[area_id]:
				file_handle.write('0\t')
			else:
				file_handle.write('%d\t'%poi_dict[area_id][md5])
		file_handle.write('\n')
	file_handle.close()

if __name__ == '__main__':
	root_path = '/Users/didi/workspace/Python/Competition/season_1'
	poi_file = '%s/training_data/poi_data/poi_data'%root_path
	poi_format_file = '%s/format/training_data/poi_data/poi_data'%root_path
	poi_dict = process(poi_file)
	poi_list = merge_dict(poi_dict)
	print len(poi_list)
	poi_write(poi_format_file, poi_dict, poi_list)

