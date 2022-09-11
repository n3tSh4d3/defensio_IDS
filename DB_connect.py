#!/usr/bin/env python3
# Module Imports
import sys
import time
from datetime import datetime
import arachni
import mariadb
import nmap


class database_connect:

    def database_connection(self, utente, password, ip_db, port_server, db):

        try:
            conn = mariadb.connect(
                user=utente,
                password=password,
                host=ip_db,
                database=db,
                port=port_server
            )
            return conn
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)