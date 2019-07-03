import pymongo
from descriptions import *

MongoClient = pymongo.MongoClient()
db = MongoClient['Atlas']
use_cases = db['Atlas_UseCases']
cybersecurity_threats = db['Atlas_cybersecurity_threats']
actors = db['Atlas_actors']
responding_organizations = db['Atlas_responding_organizations']
technologies = db['Atlas_technologies']
disciplines = db['Atlas_disciplines']
locations = db['Atlas_locations']
information_types = db['Atlas_information_types']
information_categories = db['Atlas_information_categories']
activities = db['Atlas_activities']

use_cases.delete_many({})
cybersecurity_threats.delete_many({})
actors.delete_many({})
responding_organizations.delete_many({})
technologies.delete_many({})
disciplines.delete_many({})
locations.delete_many({})
information_types.delete_many({})
information_categories.delete_many({})
activities.delete_many({})

cybersecurity_threats_ids = {}
information_categories_ids = {}
actors_ids = {}
responding_organizations_ids = {}
technologies_ids = {}
disciplines_ids = {}
locations_ids = {}
information_types_ids = {}
activities_ids = {}

actors.insert_many([
        {
            'name': 'patients',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'paramedics',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'law enforcement',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'suspects',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'civilians',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'victims',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'fire fighters',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'incident commander',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'cab driver',
            'description': '',
            'resource_links': []
        },
])

for i in actors.find({}):
    actors_ids[i['name']] = i['_id']

for i, j in actors_ids.items():
    print(i, j)

responding_organizations.insert_many([
        {
            'name': 'Local EMS',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'Local Police',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'Highway Patrol',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'EMS',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'Park Police',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'Fire Department',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'FEMA',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'Local Fire',
            'description': '',
            'resource_links': []
        }
])

for i in responding_organizations.find({}):
    responding_organizations_ids[i['name']] = i['_id']

disciplines.insert_many([
        {
            'name': 'EMS',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'Law Enforcement',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'Fire',
            'description': '',
            'resource_links': []
        }
])

for i in disciplines.find({}):
    disciplines_ids[i['name']] = i['_id']

locations.insert_many([
        {
            'name': 'highway',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'hospital',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'national park',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'urban area',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'building',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'sub-urban area',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'parks',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'road',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'metropolitan city',
            'description': '',
            'resource_links': []
        },
        {
            'name': 'subway',
            'description': '',
            'resource_links': []
        },
])

technologies.insert_many(
    [{
      "name": "smartphone",
      "description": "",
      "resource_links": [
        {
          "href": "https://www.nist.gov/communications-technology-laboratory/pscr/process-document-nist-list-certified-devices",
          "hyperlink_name": "Certified Devices",
          "description": "The Middle Class Tax Relief and Job Creation Act of 2012 (Act) defined responsibilities for the National Institute of Standards and Technology (NIST) in regards to the Nationwide Public Safety Broadband Network (NPSBN) and the First Responder Nextwork Authority (FN). AT&T was awarded the contract by FN to partner with FN and to build the NPSBN. One requirement of the Act is that the Director of NIST shall ensure the development of a list of certified devices that meet appropriate protocols and standards for access to, use of, or compatibility with the NPSBN that FN and AT&T build and maintain. This requirement is carried out by the Public Safety Communications Research Division (PSCR) of the NIST Communications Technology Laboratory. This document describes the process for creating and maintaining the list."
        }
      ]
    },
    {
      "name": "tablet",
      "description": "",
      "resource_links": []
    },
    {
      "name": "hotspot",
      "description": "",
      "resource_links": []
    },
    {
      "name": "LTE modem",
      "description": "",
      "resource_links": []
    },
    {
      "name": "smartwatch",
      "description": "",
      "resource_links": []
    },
    {
      "name": "fitness tracker",
      "description": "",
      "resource_links": []
    },
    {
      "name": "drone",
      "description": "",
      "resource_links": []
    },
    {
      "name": "body worn camera",
      "description": "",
      "resource_links": []
    },
    {
      "name": "smartglasses",
      "description": "",
      "resource_links": []
    },
    {
      "name": "bluetooth headset",
      "description": "",
      "resource_links": []
    },
    {
      "name": "wearable health monitoring sensor",
      "description": "",
      "resource_links": []
    },
      {
      "name": "hardware authentication device",
      "description": "",
      "resource_links": []
    },
    {
      "name": "LMR handsets",
      "description": "",
      "resource_links": []
    }]

)

for i in locations.find({}):
    locations_ids[i['name']] = i['_id']


information_categories.insert_many([
    {
        'name': 'operations data',
        'description': '',
        'resource_links': []
    },
    {
        'name': 'sensor data',
        'description': '',
        'resource_links': []
    },
    {
        'name': 'publicly sourced data',
        'description': '',
        'resource_links': []
    },
    {
        'name': 'situational awareness data',
        'description': '',
        'resource_links': []
    },
    {
        'name': 'Unknown',
        'description': '',
        'resource_links': []
    },
    {
        "description": "A data type for a single or set of related actions, events, or process steps.",
        "name": "ActivityType",
        "resource_links": [
            {
                "description": "NIEM Type.",
                "href": "https://beta.movement.niem.gov/#/details?entityID=nc:ActivityType",
                "hyperlink_name": "NIEM Namespace: NIEM Core. - ActivityType"
            }
        ]
    },
    {
        "description": "A data type for a device.",
        "name": "DeviceType",
        "resource_links": [
            {
                "description": "NIEM Type.",
                "href": "https://beta.movement.niem.gov/#/details?entityID=nc:DeviceType",
                "hyperlink_name": "NIEM Namespace: NIEM Core. - DeviceType"
            }
        ]
    },
    {
        "description": "A data type for a human being.",
        "name": "PersonType",
        "resource_links": [
            {
                "description": "NIEM Type.",
                "href": "https://beta.movement.niem.gov/#/details?entityID=nc:PersonType",
                "hyperlink_name": "NIEM Namespace: NIEM Core. - PersonType"
            }
        ]
    },
    {
        "description": "A data type for a conveyance designed to carry an operator, passengers and/or cargo, over land.",
        "name": "VehicleType",
        "resource_links": [
            {
                "description": "NIEM Type.",
                "href": "https://beta.movement.niem.gov/#/details?entityID=nc:VehicleType",
                "hyperlink_name": "NIEM Namespace: NIEM Core. - VehicleType"
            }
        ]
    }
])


for i in information_categories.find({}):
    information_categories_ids[i['name']] = i['_id']


information_types.insert_many([
    {
        'name': 'active authentication',
        'description': "Something from a authenticator",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'body camera data',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'comms',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'completed incident command system (ICS) forms/plans',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'crime scene geographic information system (GIS) intel location',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'critical static locations (shelters|ccps|EVAC|LZ)',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'medium',
            'availability': 'medium'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'deployable assets',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'Emergency Response',
        'description': "",
        'triad_rating': {
            'confidentiality': 'low',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'evac routes and plans',
        'description': "",
        'triad_rating': {
            'confidentiality': 'low',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'facial recognition',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'medium'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'first responder assets',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'functional roles',
        'description': "",
        'triad_rating': {
            'confidentiality': 'medium',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'ICS (incident command system) forms/plans',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'images + media from ng911',
        'description': "",
        'triad_rating': {
            'confidentiality': 'low',
            'integrity': 'medium',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'incident action plan',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'Info from multiple CAD LE Location',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'medium',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'law enforcement intel',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'license and plate reader',
        'description': "",
        'triad_rating': {
            'confidentiality': 'medium',
            'integrity': 'high',
            'availability': 'low'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'license plate recognition (LPR)',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        'name': 'managing security',
        'description': "",
        'triad_rating': {
            'confidentiality': 'high',
            'integrity': 'high',
            'availability': 'high'
        },
        'security_reasoning': '',
        'information_categories': [information_categories_ids.get('operations data')]
    },
    {
        "description": "An augmentation point for ActivityType.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityAugmentationPoint",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A kind of activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityCategoryText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A person or organization to contact for additional information about an activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityContactEntity",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A date of an activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityDate",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of an activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A result or outcome of an activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityDisposition",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification that references an activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A name of an activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityName",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A reason for an activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityReasonText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A status of an activity.",
        "information_categories": [
            information_categories_ids.get('ActivityType')
        ],
        "name": "ActivityStatus",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An augmentation point for nc:DeviceType.",
        "information_categories": [
            information_categories_ids.get('DeviceType')
        ],
        "name": "DeviceAugmentationPoint",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a kind of communication device.",
        "information_categories": [
            information_categories_ids.get('DeviceType')
        ],
        "name": "DeviceCategoryAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification number of a device specified as an electronic serial number assigned to every GSM and UMTS cellular phone by the specific manufacturer.",
        "information_categories": [
            information_categories_ids.get('DeviceType')
        ],
        "name": "DeviceESNIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An Internet Protocol (IP) address or Uniform Resource Locator (URL) of a device that uniquely identifies a specific site on the Internet or another network.",
        "information_categories": [
            information_categories_ids.get('DeviceType')
        ],
        "name": "DeviceElectronicAddress",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification number of a device specified as an International Mobile Equipment Identity assigned to every mobile phone by the manufacturer.",
        "information_categories": [
            information_categories_ids.get('DeviceType')
        ],
        "name": "DeviceIMEIIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A piece of contact information stored on a device.",
        "information_categories": [
            information_categories_ids.get('DeviceType')
        ],
        "name": "DeviceStoredContactInformation",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A means of contacting a person at work.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "EmploymentContactInformation",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A manner of pronunciation; a way of pronouncing words that may indicate the place of origin or social background of the speaker.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonAccentText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A general description of the age of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonAgeDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A measurement of the age of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonAgeMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An augmentation point for PersonType.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonAugmentationPoint",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A date a person was born.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonBirthDate",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A location where a person was born.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonBirthLocation",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a blood group and RH factor of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonBloodTypeAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for the availability of an X-ray for a specific body part for a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonBodyXRaysAvailableAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a person's physique or body shape.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonBuildAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A capacity or ability of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonCapability",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "True if a person is circumcised; false otherwise.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonCircumcisionIndicator",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a country that assigns rights, duties, and privileges to a person because of the birth or naturalization of the person in that country.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonCitizenshipAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An appearance or condition of the skin of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonComplexionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A date a person died or was declared legally dead.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonDeathDate",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A number of people dependent upon a person as their primary means of support.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonDependentQuantity",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A photograph or image of a person in a digital format.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonDigitalImage",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An image of a handwritten signature of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonDigitizedSignatureImage",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of something a person wears to conceal or mislead others as to the true appearance or identity of that person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonDisguiseDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A highest level of education a person has obtained.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonEducationLevelText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A means of contacting someone in the event of an emergency.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonEmergencyContactInformation",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a cultural lineage of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonEthnicityAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a color of the eyes of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonEyeColorAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a kind of glasses or other eyewear.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonEyewearAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a kind of facial hair.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonFacialHairAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of the way a person looks and is presented overall.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonGeneralAppearanceDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An overall appearance of the hair of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHairAppearanceText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A kind of hair of a person, such as wavy or straight.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHairCategoryText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a color of the hair of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHairColorAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a length of hair of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHairLengthAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a style or cut of hair worn by a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHairStyleAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A hand with which a person is more adept using.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHandednessText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of the height of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHeightDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A measurement of the height of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHeightMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A means of contacting a person at home.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHomeContactInformation",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A human resources or employment identification assigned to a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonHumanResourceIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A form of physical harm or damage sustained by a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonInjury",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of adornments a person wears.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonJewelryDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "True if a person understands and speaks English; false otherwise.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonLanguageEnglishIndicator",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A disorder of a person which can cause difficulties in learning something.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonLearningDisabilityText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification that references a license certification or registration of a person for some purpose.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonLicenseIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "True if a person is alive; false if a person is dead.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonLivingIndicator",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A state of health for a person, on-going or present.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonMedicalCondition",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of the overall health of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonMedicalDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "True if a medical history file is known to exist for a person; false otherwise.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonMedicalFileIndicator",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A medication and dosage required for a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonMedicationRequiredText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A mental condition of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonMentalStateText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A service of a person in a military.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonMilitarySummary",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of a state of feeling of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonMoodDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A combination of names and/or titles by which a person is known.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonName",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification that references a person within a country but is not based on fingerprint.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonNationalIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a country of a person's citizenship or a country in which a person is deemed a national.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonNationalityAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "True if a person has given consent to be used as an organ donor upon death; false otherwise.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonOrganDonatorIndicator",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for an organ a person is willing to donate upon death.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonOrganDonorAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification with a kind that is not explicitly defined in the standard that refers to a person within a certain domain.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonOtherIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification of a passport issued to a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonPassportIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A physical disability of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonPhysicalDisabilityText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A prominent or easily identifiable aspect of  a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonPhysicalFeature",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A capacity of a person for a language with which that person has the strongest familiarity.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonPrimaryLanguage",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a classification of a person based on factors such as geographical locations and genetics.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonRaceAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a religion to which a person subscribes or believes; a categorization of spiritual beliefs.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonReligionAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a manner of residence a person has in a city, town, community, or other area..",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonResidentAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A unique identification reference to a living person; assigned by the United States Social Security Administration.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonSSNIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A capacity of a person for a language with which that person is not completely fluent.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonSecondaryLanguage",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a formal authorization granting a person access to classified or restricted information.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonSecurityClearanceAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a gender or sex of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonSexAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A target gender of the sexual interest of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonSexualOrientationText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a color or tone of the skin of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonSkinToneAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of a pattern of speech with which a person speaks.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonSpeechDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification of a person based on a state-issued ID card.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonStateIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An identification used to refer to a specific person within the tax system of a country.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonTaxIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "True if a person is a citizen of the United States; false otherwise.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonUSCitizenIndicator",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a legal status of a union between two people.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonUnionStatusAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A prescription a person needs for corrective lenses or contacts.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonVisionPrescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A description of the weight of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonWeightDescriptionText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A measurement of the weight of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonWeightMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An X-Ray image of a person or part of a person.",
        "information_categories": [
            information_categories_ids.get('PersonType')
        ],
        "name": "PersonXRayImage",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An augmentation point for VehicleType.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleAugmentationPoint",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A count of common axles of rotation of one or more wheels of a vehicle, whether power driven or freely rotating.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleAxleQuantity",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "True if a vehicle is a commercial motor vehicle; false otherwise.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleCMVIndicator",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A color of the interior of a vehicle.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleColorInteriorText",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "An observed, estimated, or measured weight of the conveyance.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleCurrentWeightMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A number of doors on a vehicle.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleDoorQuantity",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A sum of values specified by the manufacturer(s) for a truck tractor or trailer for the units that make up a combination.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleGrossLadenSumWeightMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A value specified by the manufacturer for a single unit truck, truck tractor, or trailer.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleGrossLadenUnitWeightMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A unique identification for a specific vehicle.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleIdentification",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A manufacturer's suggested retail price of a vehicle; a price at which a manufacturer recommends a vehicle be sold.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleMSRPAmount",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a manufacturer of a vehicle.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleMakeAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A maximum load weight intended for the vehicle to transport, assigned at the point of manufacture.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleMaximumLoadWeightMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a specific design or class of vehicle made by a manufacturer.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleModelAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A reading of a vehicle odometer to the nearest mile or kilometer.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleOdometerReadingMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A total number of people a vehicle is designed to safely transport.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehiclePassengerSafeQuantity",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A total number of seats available in a vehicle.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleSeatingQuantity",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A data concept for a kind of transmission unit in a vehicle.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleTransmissionCategoryAbstract",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    },
    {
        "description": "A weight of a vehicle fully equipped for service, not including the weight of the payload.",
        "information_categories": [
            information_categories_ids.get('VehicleType')
        ],
        "name": "VehicleUnladenWeightMeasure",
        "security_reasoning": "",
        "triad_rating": {
            "availability": "-",
            "confidentiality": "-",
            "integrity": "-"
        }
    }

])

for i in information_types.find({}):
    information_types_ids[i['name']] = i['_id']


use_cases.insert_many([

    {
        'name':  'Personal Injury Collision with hazards',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_1,
        'actors': [actors_ids[x] for x in ['patients', 'paramedics', 'law enforcement']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local EMS', 'Local Police', 'Highway Patrol']],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['EMS', 'Fire', 'Law Enforcement']],
        'locations': [locations_ids[x] for x in ['highway']],
        'information_types': [],
        'activities': [],
        'concept_links': {
            'actors': [actors_ids[x] for x in ['law enforcement']],
            'disciplines': [disciplines_ids[x] for x in ['Law Enforcement']],
            'responding_organizations': [responding_organizations_ids[x] for x in ['Local Police']],
            'information_types': [information_types_ids[x] for x in ['law enforcement intel', 'body camera data']]
            }
    },

    {
        'name': 'Medical emergency',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_2,
        'actors': [actors_ids[x] for x in ['patients', 'paramedics']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['EMS']],
        'technologies': [],
        'disciplines': [disciplines_ids[x]for x in ['EMS']],
        'locations': [locations_ids[x] for x in ['hospital']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Search in a national park',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_3,
        'actors': [actors_ids[x] for x in ['suspects', 'law enforcement']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local Police', 'Park Police']],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['Law Enforcement', 'EMS']],
        'locations': [locations_ids[x] for x in ['national park']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Rioting in an urban area',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_4,
        'actors': [actors_ids[x] for x in ['civilians', 'suspects', 'law enforcement', 'paramedics']],
        'responding_organizations': [],
        'technologies': [],
        'disciplines': [],
        'locations': [locations_ids[x] for x in ['urban area']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Undercover officer',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_5,
        'actors': [actors_ids[x] for x in ['suspects', 'law enforcement']],
        'responding_organizations': [],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['Law Enforcement']],
        'locations': [locations_ids[x] for x in ['urban area']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Structure fire',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_6,
        'actors': [actors_ids[x] for x in ['victims', 'fire fighters']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Fire Department']],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['Fire']],
        'locations': [locations_ids[x] for x in ['building']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Wild fire',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_7,
        'actors': [actors_ids[x] for x in ['civilians', 'fire fighters', 'law enforcement', 'paramedics']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local EMS', 'Fire Department', 'Local Police']],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['Fire']],
        'locations': [locations_ids[x] for x in ['sub-urban area', 'parks']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Hurricane',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_8,
        'actors': [actors_ids[x] for x in ['civilians', 'fire fighters', 'law enforcement', 'paramedics']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local EMS', 'Fire Department', 'Local Police', 'FEMA']],
        'technologies': [],
        'disciplines': [],
        'locations': [],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Active shooter',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_9,
        'actors': [actors_ids[x] for x in ['civilians', 'paramedics', 'law enforcement']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local EMS', 'Local Police']],
        'technologies': [],
        'disciplines': [],
        'locations': [locations_ids[x] for x in ['urban area']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Police officer vehicle stop',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_10,
        'actors': [actors_ids[x] for x in ['suspects', 'law enforcement']],
        'responding_organizations': [],
        'technologies': [],
        'disciplines': [],
        'locations': [locations_ids[x] for x in ['road']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Apartment Building Fire',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_11,
        'actors': [actors_ids[x] for x in ['cab driver', 'incident commander', 'fire fighters', 'paramedics', 'civilians']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local EMS', 'Local Fire']],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['Fire', 'EMS']],
        'locations': [locations_ids[x] for x in ['building', 'metropolitan city']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Structure Fire -Future Technology Scenario',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_12,
        'actors': [actors_ids[x] for x in ['fire fighters']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local Fire']],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['Fire']],
        'locations': [locations_ids[x] for x in ['building', 'metropolitan city']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'Subway Fire',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_13,
        'actors': [actors_ids[x] for x in ['civilians', 'fire fighters', 'victims']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local Fire']],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['Fire']],
        'locations': [locations_ids[x] for x in ['subway', 'metropolitan city']],
        'information_types': [],
        'activities': []
    },

    {
        'name': 'WUI Fire',
        "source": "",
        'cybersecurity_threats': [],
        'description': desc_14,
        'actors': [actors_ids[x] for x in ['civilians', 'fire fighters']],
        'responding_organizations': [responding_organizations_ids[x] for x in ['Local Fire']],
        'technologies': [],
        'disciplines': [disciplines_ids[x] for x in ['Fire']],
        'locations': [],
        'information_types': [],
        'activities': []
    }
])
