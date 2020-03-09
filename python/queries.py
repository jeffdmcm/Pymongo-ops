from pymongo_helper import mongoConnect
from pymongo_helper import importJSON


qa_db = mongoConnect("qa")

measures  = qa_db['measures']

measures.count_documents({"incentive.state": "NY"})

measures.distinct("incentive.utility_company")

measures.count_documents({"incentive.utility_company": "MCE"})

measures.delete_many({"incentive.utility_company": "MCE"})



prd_db = mongoConnect('prd')
measures = prd_db['measures']

importJSON(input,measures) 
