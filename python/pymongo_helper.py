import json
import os
from pymongo import MongoClient
import pandas
import configparser
import exceptions



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
     try:
         # check that environment is valid
         validateEnv(env)
         # create connection to mongo
         config = configparser.ConfigParser()
         config.read('config.ini')
         url = config['url'][env]
         lib = config['libName'][env]
         db = MongoClient(url)[lib]
         # check that connection is valid
         validateDBConnect(db)
         return db
     except:
         pass

     


def validateDBConnect(db):
    try:
        colls = db.list_collection_names()
        # if db finds some collections it is valid
        if len(colls) < 1:
            raise InvalidDBError
    except InvalidDBError:
         print("DB connection not valid. Check parameters")
   
 

def validateEnv(env):
    validEnvs = ['sandbox', 'qa', 'prd','entBackup']
    try:
        if env not in validEnvs:
            raise InvalidEnvironmentError
        if env == 'prd':
            confirmation = input(bcolors.WARNING +
                                 "\nTo confirm, re-enter 'prd':\n" + bcolors.ENDC)
            if confirmation == "prd":
                pass
            else:
                print(bcolors.FAIL +
                      "'{confirmation}' != 'prd \n\nAborting..." +
                      bcolors.ENDC)

                return env
    except InvalidEnvironmentError:
        print("Invalid Environment. Must be 'qa' or 'prd'")




def importJSON(input, collection):
    try:
        with open(input, 'r') as infile:
            data = json.load(infile)
            collection.insert_many(data)
            count = len(data)
            print(str(count) + ' documents inserted into ' + str(collection.name))
    except:
        print('There was an error inserting ' + str(input))
   
