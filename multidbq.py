import json
import sqlite3
import argparse
import sys
from os import listdir
from os import walk


def main():
	parser = argparse.ArgumentParser(description='Multi-DB Sqlite Query Tool')

	parser.set_defaults(default=lambda x: parser.print_help())
	parser.add_argument('query', help='Query to execute in multiple DBs')
	parser.add_argument('-d', '--root-dir', default='./', help='Root directory to find DB files in')
	parser.add_argument('-c', '--config', default='config.json', help='Specifies which config file to use')
	parser.add_argument('-pf', '--print-found-dbs', default=False, help='If True, prints all DB files found')
	parser.add_argument('-l', '--limit', nargs=1, default=0, help='If True, prints all DB files found')

	args = parser.parse_args()

	config = load_config(args.config)

	dbs_found = find_dbs(args.root_dir, config['default_db_name'])

	if(args.print_found_dbs):
		print('DBs found: ', str(dbs_found))

	count = 0
	limit = 0

	if(args.limit != 0):
		try:
			limit = int(args.limit[0])

		except ValueError as err:
			print('The limit argument must be an integer:', str(err))
			sys.exit(1)


	for db in dbs_found:
		if(limit > 0 and count >= limit):
			break

		print('')
		print('----------------------------------------------------------------------------------------------------')
		
		print('Connecting to: ', str(db))
		cursor = sql_init(db)
		result = execute_query(args.query, cursor)

		print('Result: ')
		print(str(result))
		cursor.close()
		count += 1
		print('----------------------------------------------------------------------------------------------------')
		print('')

def load_config(file):
	with open(file) as config_file:    
		config = json.load(config_file)
	
	return config

def find_dbs(root_db_dir, default_db_name):
	db_files = []

	for (dirpath, dirnames, filenames) in walk(root_db_dir):
		#print("walk: ", str(dirpath), str(dirnames), str(filenames))

		for filename in filenames:
			if filename == default_db_name:
				db_files.append(str(dirpath) + '/' + filename)

	return db_files

def sql_init(db_path):
	conn = sqlite3.connect(db_path)
	cursor = conn.cursor()
	return cursor

def execute_query(query, cursor):
	cursor.execute(query)
	result_set = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]

	return result_set


if __name__ == "__main__": main()