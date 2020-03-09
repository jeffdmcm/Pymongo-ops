import json
from pymongo import MongoClient
import pandas
import configparser



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def mongoConnect(env):

     # check that environment is valid
     validateEnv(env)

     # create connection to mongo
     config = configparser.ConfigParser()
     config.read('python/config.ini')
     url = config['url'][env]
     lib = config['libName'][env]
     db = MongoClient(url)[lib]
     # check that connection is valid
     validateDBConnect(db)
     
     return db

     


def validateDBConnect(db):
    colls = db.list_collection_names()
    count = len(colls)
    # if db finds some collections it is valid
    if count > 0:
        return 1
    else:
        return 0
 

def validateEnv(env):
    validEnvs = ['sandbox', 'qa-graphql', 'production']
    if env not in validEnvs:
        raise InvalidEnvironmentError(envError)
    if env == 'production':
        confirmation = input(bcolors.WARNING + "\nTo confirm, re-enter 'production':\n" + bcolors.ENDC)
        if confirmation == "production":
            pass
        else:
            print(bcolors.FAIL +
                  "'{confirmation}' != 'production \n\nAborting..." +
                  bcolors.ENDC)

    return env



def importJSON(input, collection, db):
    with open(input, 'r') as infile:
        data = json.load(infile)
        collection.insert_many(data)
    # add error handling
    # add print statement of number of elements added to collection

        
class InvalidEnvironmentError(Error):
    '''
    Raised when referencing an invalid environment
    Environment must be one of: 'sandbox', 'qa-graphql', 'production'
    '''
