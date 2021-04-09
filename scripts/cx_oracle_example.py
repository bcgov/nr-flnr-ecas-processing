# cx_oracle_example.py

# created by mdouville 20210414
# list the role name from a table in an oracle database
# python test.py arg1 arg2 arg3
# python cx_oracle_example.py <server> <database> <username> <password>
# python cx_oracle_example.py bcgw.bcgov idwprod1 mrdouvil 

import cx_Oracle
import sys
import argparse


# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", help="the server where the database resides", dest='host', action='store')
parser.add_argument("-d", "--database", help="the database to connect to",dest='database', action='store')
parser.add_argument("-u", "--username", help="the username to connect to the database",dest='user', action='store')
parser.add_argument("-p", "--password", help="the password of the user", dest='pwd', action='store')

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


results = parser.parse_args()

connection = results.user+'/'+results.pwd+"@"+results.host+'/'+results.database
connectionprint = results.user+"@"+results.host+'/'+results.database
print (connectionprint)

try:
    con = cx_Oracle.connect(connection)
    cur = con.cursor()
    cur.execute('select MAP_TILE_DISPLAY_NAME from WHSE_BASEMAPPING.BCGS_2500_GRID where OBJECTID=64688')
    

    for result in cur:
        role_name = str(result[0])
        print(role_name)

    cur.close()
    con.close()

except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
except ValueError as e:
    print(e)
except:
    print ("Unexpected error:", sys.exc_info()[0])
    raise

