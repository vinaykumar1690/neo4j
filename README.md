neo4j
=====

Traversing and parsing relationships in a big (~250M relations) neo4j graph using py2neo.

## Starting the script

You can start the script `ParseRelation.py` on the Ubuntu server by running the command:
- `screen -L -d -m python ParseRelation.py`

GNU Screen attaches this process to a virtual process and you will notice the script will start running in the list of processes. The -L option will create a log document in the same directory which will keep a record all exception or error messages.

## How to check if the script is running

Running the following command should give you the number of sockets running on Screen.
- `screen -list`

You can get the process id of the process. Say it's 12345.

## How to stop the script

Assuming the process id is 12345, run the following commands:
- `kill -9 12345`
- `screen wipe`
