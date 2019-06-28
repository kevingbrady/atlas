import pymongo

def addReferenceLinks(db):
    ####################################################################################################################
    # Update Use Case Attributes to have reference_links:
    # [
    #   {
    #       "href": "",
    #       "hyperlink_name": "",
    #       "description": ""
    #   },
    # ]
    for c in ("Atlas_technologies",):
        db[c].update_many(
            {"resource_links": { "$exists": False} },
            { '$set': {"resource_links": []}},
            False
        )
    ####################################################################################################################

def main():
    # Set up db connection
    MongoClient = pymongo.MongoClient()
    db = MongoClient['Atlas']
    addReferenceLinks(db)

if __name__ == "__main__":
    main()