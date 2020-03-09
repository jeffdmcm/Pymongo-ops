from pymongo_helper import mongoConnect
import json
import pandas as pd
import dplython

def measuresSchemaJSON(csv_path, db):

    db = mongoConnect('qa')

    # data shell of measures schema
    data_dict  = {'source':None, 'category':None, 'project_category':None,
                  'project_application':None, 'fuel':None, 'name':None,
                  'displayName':None, 'description':None,
                  'incentive':{'input_label':None, 'input_description':None,
                               'state':None, 'utility_company':None,
                               'rebate_code':None, 'product_code':None,
                               'program_link':None, 'bonuses_available':None,
                               'bonus_comment':None, 'source_link':None,
                               'expiration':None, 'existing_requirements':None,
                               'design_requirements':None, 'incentive_type':None,
                               'unit_rate':None, 'input_units':None}}

    raw_data = pd.read_csv(csv_path)
    data = raw_data.fillna("None")
    result = data.apply(compileData, axis = 1, main_dict = data_dict).tolist()
    
    out_path = "../data/json/mce-projects.json"
    with open(out_path, "w+", encoding = 'utf8') as outfile:
        outfile.write(json.dumps(result,indent=4))
    print('Wrote to {out_path}')
    
                      
      
    

def compileData(row, main_dict):
    # skip if no displayname
    if row.get('displayName') == None:
        return None
    curr_dict = main_dict
    # loop dict headers to pull data
    for key in curr_dict:
        # loop inside if nested dict
        if type(curr_dict[key]) == dict:
            for i_key in curr_dict[key]:
                curr_dict[key][i_key] = row.get(i_key)
        else:
            curr_dict[key] = row.get(key)
    return(curr_dict.copy())

    
