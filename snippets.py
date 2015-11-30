import psycopg2 
import logging

logging.basicConfig(filename='snippets.log',level=logging.DEBUG)
import argparse
import sys
import os


def connect_to_db():
    logging.debug("Connecting to PostgreSQL")
    connection = psycopg2.connect(database="snippets")
    logging.debug("Database connection established.")


def put(name, snippet):

    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")   
    return name, snippet
    
    

def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet...

    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
    
    
def main():
    
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    get_paser=subparsers.add_parser("get",help="Retrieve a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    get_paser.add_argument("name",help="The name of the snippet")

    arguments = parser.parse_args(sys.argv[1:])
    
    arguments = vars(arguments)
    command=arguments.pop("command")
    if command=="put":
        name,snippet=put(**arguments)
        print "Stored {!r} as {!r}".format(snippet,name)
    elif command=="get":
        snippet=get(**arguments)
        print "Retrieve snippet: {!r}".format(snippet)

if __name__ == '__main__':
    main()