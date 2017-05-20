# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 15:15:36 2017

@author: Victor
"""

import sqlite3

sqlite_file = 'freetown2.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM nodes;")
print c.fetchall()

c.execute("SELECT COUNT(*) FROM ways;")
print c.fetchall()
c.execute("SELECT COUNT(DISTINCT(a.uid)) FROM \
          (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) a;")
print c.fetchall()

c.execute("SELECT a.user, COUNT(*) as num \
           FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) a \
           GROUP BY a.user \
           ORDER BY num DESC \
           LIMIT 10;")

pprint.pprint(c.fetchall())

c.execute("SELECT COUNT(*) \
           FROM \
              (SELECT a.user, COUNT(*) as num \
               FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) a \
           GROUP BY a.user \
           HAVING num=1)  u;")

pprint.pprint(c.fetchall())
c.execute("SELECT value, COUNT(*) as num \
            FROM nodes_tags \
           WHERE key='amenity' \
           GROUP BY value \
           ORDER BY num DESC \
           LIMIT 20;")

pprint.pprint(c.fetchall())

c.execute("SELECT nodes_tags.value, COUNT(*) as num \
           FROM nodes_tags \
               JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value = 'restaurant') \
               i ON nodes_tags.id = i.id \
           WHERE nodes_tags.key = 'cuisine'\
           GROUP BY nodes_tags.value\
           ORDER BY num DESC;")

pprint.pprint(c.fetchall())

c.execute("SELECT nodes_tags.value, COUNT(*) as num \
           FROM nodes_tags \
             JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='place_of_worship') i \
             ON nodes_tags.id=i.id \
           WHERE nodes_tags.key='religion' \
           GROUP BY nodes_tags.value \
           ORDER BY num DESC \
           LIMIT 1;")

pprint.pprint(c.fetchall())