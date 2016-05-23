from utils import *
from collections import defaultdict

def process(read_file):
	file_handle =open(read_file, 'r')
	traffic_dict = {}
	for line in file_handle:
		curr_list = line.strip('\n').split('\t')
		area_id = curr_list[0]
		if area_id not in traffic_dict:
			traffic_dict[area_id] = {}
		timestamp = curr_list[-1][0:-1]
		slice = time2slice(timestamp)
		traffic_dict[area_id][slice] = defaultdict(list)
		for ii in range(1, len(curr_list) - 1):
			idx, size = curr_list[ii].split(':')
			traffic_dict[area_id][slice][idx] = size
	file_handle.close()
	return traffic_dict

def write_traffic(write_file, traffic_dict):
	file_handle = open(write_file, 'w')
	for area_id in traffic_dict:
		file_handle.write('%s\n'%area_id)
		for slice in traffic_dict[area_id]:
			file_handle.write('\t%d\n'%slice)
			for idx in traffic_dict[area_id][slice]:
				file_handle.write('\t\t%s:%s\n'%(idx, traffic_dict[area_id][slice][idx]))
	file_handle.close()
			
if __name__ == '__main__':
	root_path = '/Users/didi/Desktop/Competition/season_1'
	traffic_path = '%s/training_data/traffic_data'%root_path
	traffic_write_path = '%s/format/training_data/traffic_data'%root_path
	file_list = fetch_file_list(traffic_path)
	for file_name in file_list:
		read_file = os.path.join(traffic_path, file_name)
		write_file = os.path.join(traffic_write_path, file_name)
		traffic_dict = process(read_file)
		write_traffic(write_file, traffic_dict)

