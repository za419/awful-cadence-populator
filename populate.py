#!/usr/bin/python

import pg8000
import sys
import os
from configparser import ConfigParser

config = ConfigParser(interpolation=None)
config.read(os.path.realpath(sys.argv[1]))
config = config['DEFAULT']

dir = os.path.realpath(sys.argv[2])

db = pg8000.connect(user=config['db_username'], host=config['db_host'],
                    port=int(config['db_port']), database=config['db_name'],
                    password=config['db_password'], ssl=config.getboolean('db_encrypt'),
                    timeout=ariaSearch.timeout)
cursor = db.cursor()

for r, d, files in os.walk(dir):
    for file in files:
        lfile = file.lower()
        if lfile.endswith((".mp3", ".m4a", ".flac", ".ogg")):
            part = file.rpartition(".")[0]
            cursor.execute("INSERT INTO "+config['db_table']+" ("+', '.join([config['db_column_title'], config['db_column_artist'], config['db_column_path']])+") VALUES %s, %s, %s", part, part, file)
            db.commit()
            print("Populated with file {0}.", file)
