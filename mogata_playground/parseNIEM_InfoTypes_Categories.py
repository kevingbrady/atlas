import pandas as pd
import pprint
import json
import os
import sys
from json import JSONEncoder, JSONDecoder

sys.path.append( os.path.abspath(os.path.join( os.path.join(os.path.dirname(__file__), os.path.pardir) ) ) )
sys.path.append(
    os.path.abspath(
        os.path.join(
                *[
                    os.path.join(os.path.dirname(__file__), os.path.pardir ),
                    "Atlas"
                ]
            ) ) )
sys.path.append(
    os.path.abspath(
        os.path.join(
                *[
                    os.path.join(os.path.dirname(__file__), os.path.pardir ),
                    "Atlas",
                    "static"
                ]
            ) ) )
from models import InformationCategories, InformationTypes

# Script Globals #######################################################################################################
NIEM_FILENAME = "./niem_data/database.xls"
INFORMATION_CATEGORIES_FILE = "./data/information_categories/information_categories.json"
INFORMATION_TYPES_FILE = "./data/information_types/information_types.json"

########################################################################################################################

# Script Classes #######################################################################################################
pp = pprint.PrettyPrinter(indent=4)

####

class s_InformationCategories(object):
    def __init__(self, name, description, resource_links):
        self.my_ic = InformationCategories()

        self.my_ic.name = name
        self.my_ic.description = description
        self.my_ic.resource_links = resource_links

    def __dict__(self):
        return{
            "name": self.my_ic.name,
            "description": self.my_ic.description,
            "resource_links": self.my_ic.resource_links
        }

####

class s_InformationTypes(object):
    def __init__(self, name, description, information_categories):
        self.my_it = InformationTypes()

        self.my_it.name = name
        self.my_it.description = description
        self.my_it.information_categories = information_categories

        self.my_it.security_resoning = ""
        self.my_it.triad_rating={
            "confidentiality": "-",
            "integrity": "-",
            "availability": "-"
        }
    def __str__(self):
        return (
            {
                "name": self.my_it.name,
                "description": self.my_it.description,
                "security_reasoning": self.my_it.security_resoning,
                "triad_rating": self.my_it.triad_rating,
                "information_categories": self.my_it.information_categories
            }
        )

    def __dict__(self):
        return (
            {
                "name": self.my_it.name,
                "description": self.my_it.description,
                "security_reasoning": self.my_it.security_resoning,
                "triad_rating": self.my_it.triad_rating,
                "information_categories": self.my_it.information_categories
            }
        )

####

class CategoryEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__()

########################################################################################################################
def main():
    namespaces = {}
    types_categories_names = set()
    types_categories = []
    types = []

    xl = pd.ExcelFile(NIEM_FILENAME)

    # load name spaces
    df_namepsaces = xl.parse("Namespaces", header=3)
    for i, r in df_namepsaces.iterrows():
        namespaces[ r["Prefix"] ] = r["Definition"]

    # Load types -> information_category

    # Load relationship -> information types
    df_relationships = xl.parse("Relationships", header=3)
    for i, r in df_relationships.iterrows():
        (namespace, category) = r[0].split(":")

        cur_category = s_InformationCategories(
            category,
            r["Type Definition"],
            [
                {
                    "href": "https://beta.movement.niem.gov/#/details?entityID={}".format(r[0]),
                    "hyperlink_name": "NIEM Namespace: {} - {}".format(namespaces[namespace], category),
                    "description": "NIEM Type."
                }
            ]
        )

        if not category in types_categories_names:
            types_categories_names.add(category)
            types_categories.append(cur_category)


        (tdomain, tname) = r[2].split(":")
        newinformationtype = s_InformationTypes(
            tname,
            r[3],
            [ cur_category.my_ic.name ]
        )

        types.append( newinformationtype )

    def set_default(obj):
        if isinstance(obj, set):
            return(list(obj))
        elif isinstance(obj, s_InformationCategories):
            return obj.__dict__()
        elif isinstance(obj, s_InformationTypes):
            return obj.__dict__()
        raise TypeError

    with open (INFORMATION_CATEGORIES_FILE, "w") as o:
        to_write = {
            "collection_name": "Atlas_information_categories",
            "documents": types_categories
        }
        json.dump(to_write, o, default=set_default, indent=4, sort_keys=True)

    with open( INFORMATION_TYPES_FILE, "w") as o:
        to_write = {
            "collection_name": "Atlas_information_types",
            "documents": types
        }
        json.dump(to_write, o, default=set_default, indent=4, sort_keys=True)

if __name__ == "__main__":
    main()