from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import sys

hostname=sys.argv[1]
username="cassandra"
password="cassandra"

nodes = []
nodes.append(hostname)
auth_provider = PlainTextAuthProvider(username=username, password=password)
try:
    cluster = Cluster(nodes,auth_provider=auth_provider)
    session = cluster.connect()
    
except:
    print "Connect Failed"

try :
    strCQL = "SELECT cluster_name FROM system.local"
    pStatement = session.prepare(strCQL)

    rows = session.execute(pStatement)

    for row in rows:
        print "\n"
        print hostname + " ==> " + row[0]
    

    strCQL2 = "SELECT keyspace_name FROM system_schema.keyspaces"
    pStatement2 = session.prepare(strCQL2)
    rows2 = session.execute(pStatement2)

    for row in rows2:
    
        print "-----------------> " + row[0] 
    session.shutdown()
except:
    pass
