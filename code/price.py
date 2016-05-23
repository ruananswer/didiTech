from utils import *
from collections import defaultdict

def process(process_file):
	file_handle = open(process_file, 'r')
	start_price_dict = {}
	dest_price_dict = {}
	for line in file_handle:
		data_list = line.strip('\n').split('\t')
		start_area_id = data_list[3]
		dest_area_id = data_list[4]
		price = float(data_list[5])
		slice = time2slice(data_list[6])
		if start_area_id not in start_price_dict:
			start_price_dict[start_area_id] = {}
		if dest_area_id not in dest_price_dict:
			dest_price_dict[dest_area_id] = {}
		if slice not in start_price_dict[start_area_id]:
			start_price_dict[start_area_id][slice] = price
		else:
			start_price_dict[start_area_id][slice] += price
		if slice not in dest_price_dict[dest_area_id]:
			dest_price_dict[dest_area_id][slice] = price
		else:
			dest_price_dict[dest_area_id][slice] += price
	file_handle.close()
	return start_price_dict, dest_price_dict

def write_dict(price_file, hot_list, start_price_dict, dest_price_dict):
	file_handle = open(price_file, 'w')
	count = 0
	for area_id in start_price_dict:
		if area_id not in hot_list:
			count += 1
			continue
		file_handle.write('%s\n'%area_id)
		for slice in start_price_dict[area_id]:
			start_price = start_price_dict[area_id][slice]
			if area_id in dest_price_dict:
				if slice in dest_price_dict[area_id]:
					dest_price = dest_price_dict[area_id][slice]
			else:
				dest_price = 0
			file_handle.write('\t%d:%d	%d\n'%(slice, start_price, dest_price))
	file_handle.close()


def get_list(hot_file):
	file_handle = open(hot_file, 'r')
	hot_list = []
	for line in file_handle:
		data_list = line.strip('\n').split('\t')
		hot_list.append(data_list[0])
	file_handle.close()
	return hot_list
		

if __name__ == '__main__':
	root_path = '/Users/didi/Desktop/Competition/season_1'
	order_path = '%s/training_data/order_data'%root_path
	price_path = '%s/format/training_data/price_data'%root_path
	hot_file = '%s/training_data/cluster_map/cluster_map'%root_path
	order_file_list = fetch_file_list(order_path)
	hot_list = get_list(hot_file)
	for file_name in order_file_list:
		order_file = os.path.join(order_path, file_name)
		price_file = os.path.join(price_path, file_name)
		start_price_dict, dest_price_dict = process(order_file)
		write_dict(price_file, hot_list, start_price_dict, dest_price_dict)

