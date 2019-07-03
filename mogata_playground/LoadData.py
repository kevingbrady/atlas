import pymongo
import json
import argparse
import pymongo
import os
import sys


def loadData(db, jobj):

    # load data ########################################################################################################
    collection_name = jobj['collection_name']
    collection_documents = jobj['documents']

    # Insert Data ######################################################################################################
    collection = db[collection_name]

    collection.insert_many(collection_documents)

def loadLinked( db, jobj, link_attribute, to_collection):
    collection_name = jobj['collection_name']
    collection_documents = jobj['documents']
    collection = db[collection_name]

    for doc in collection_documents:
        new_link_array = []
        for la in ( doc[ link_attribute ]):
            for doc in db[to_collection].find({"name": la['name']}):
                new_link_array.append(doc['_id'])

        doc[ link_attribute ] = new_link_array
        print(doc)
        collection.insert_one(doc)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="data_file", type=str, required=True)
    link_group = parser.add_argument_group('link')
    link_group.add_argument("-l", "--link", dest="linked", type=bool, required=False)
    link_group.add_argument("-a" "--attribute", dest="link_attribute", type=str, required=False)
    link_group.add_argument("-t", "--table", dest="to_table", type=str, required=False)


    args = parser.parse_args()

    # Check for file existence
    if not os.path.isfile( args.data_file ):
        print( "Couldn't find data file {}".format( args.data_file))
        sys.exit(-1)

    with open( args.data_file, 'r') as jdata:
        MongoClient = pymongo.MongoClient()
        jobj = json.load(jdata)
        db = MongoClient['Atlas']
        if( args.linked ):
            loadLinked(db, jobj, args.link_attribute, args.to_table)
        else:
            loadData(db, jobj)

if __name__ == "__main__":
    main()