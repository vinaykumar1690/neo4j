#!/usr/bin/python

from py2neo import neo4j
from py2neo import exceptions
import time
import logging
import MasterRelations
import Utilities

CONNECTION_STR = "http://localhost:8001/db/data/"
#CONNECTION_STR = "http://localhost:7474/db/data/"

# Output file
output = open("relations.txt", 'a')

try:
    # Open connection
    graph_db = neo4j.GraphDatabaseService(CONNECTION_STR)

    '''users.txt is a file that has a list of all human nodes in the graph
    If the script stops running for any reason, just trim the already processed
    node ids from the top of the text file. Continue running with the remaining
    node ids.'''
    with open("users.txt") as infile:
        for line in infile:            
            nodeid = line.strip()
            validnode = True

            try:
                node = graph_db.node(nodeid)
            except Exception as node_error:
                print "Invalid node"
                print node_error
                validnode = False
                continue

            if validnode:
                validrelation = True
                try:
                    rels = list(graph_db.match(start_node=node, rel_type="CONNECTED", bidirectional=True))
                except Exception as relation_error:
                    print "Invalid relation"
                    print relation_error
                    validrelation = False
                    continue

                if validrelation:
                    for rel in rels:
                        end_node = rel.end_node
                        if end_node._id > node._id:
                            relation = MasterRelations.get_relation(node, end_node, graph_db)
                            output.write(str(node._id) + ', ' + str(end_node._id) + ", " + str(relation) + "\n")

except Exception as ex:
    print "Error!"
    print ex
finally:
    graph_db = None
    if output:
        output.close()
