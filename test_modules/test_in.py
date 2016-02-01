#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import os
import filecmp
import sys
sys.path.append("..")
from sql import SELECT
from common import fileop
from common import dbop

#              Test                                 #
#####################################################
#def setUp():
#    sql_pg()
#    sql_pt()
    
#def test_results():
#    r = compare_results()
#    assert(r == True)

SQL = SELECT.create_sql_select_all()
pgfile = dbop.sql_exe_pg('../peloton_test.conf', SQL, 'select.pg')
ptfile = dbop.sql_exe_pt('../peloton_test.conf', SQL, 'select.pt')
res = fileop.compare_results(pgfile, ptfile)

print "%s"%res
