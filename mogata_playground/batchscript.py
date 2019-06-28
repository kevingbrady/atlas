import UpdateDatabaseStructures
import LoadData
import json
import pymongo

def main():
    # Set up db connection
    MongoClient = pymongo.MongoClient()
    db = MongoClient['Atlas']

    # Data Files
    technologies = "./data/technology/technologies.json"

    # Add Data
    with open( technologies, "r") as cur:
        jo = json.load(cur)
        LoadData.loadData(db, jo)

    # Update DB Structure
    UpdateDatabaseStructures.addReferenceLinks(db)

if __name__ == "__main__":
    main()