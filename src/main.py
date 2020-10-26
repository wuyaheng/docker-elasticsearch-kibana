import argparse
import sys
import os
import requests
import json
from requests.auth import HTTPBasicAuth 
from sodapy import Socrata

parser = argparse.ArgumentParser(description='Process data')
parser.add_argument('--page_size', type=int, help='how many rows to get per page', required=True)
parser.add_argument('--num_pages', type=int, help='how many pages to get in total')
args = parser.parse_args(sys.argv[1:])


DATASET_ID = os.environ["DATASET_ID"]
APP_TOKEN = os.environ["APP_TOKEN"]
ES_HOST = os.environ["ES_HOST"]
ES_USERNAME = os.environ["ES_USERNAME"]
ES_PASSWORD = os.environ["ES_PASSWORD"]

	
	
if __name__ == "__main__":
	try:
		r = requests.put(f"{ES_HOST}/parkingdata",
			auth=HTTPBasicAuth(ES_USERNAME,ES_PASSWORD),
			json={
				"settings": {
				"number_of_shards": 1,
				"number_of_replicas": 1
				}, 
				"mappings": {"properties": {
					"plate": { "type": "keyword" },
					"state": { "type": "keyword" },
					"license_type": { "type": "keyword" },
					"summons_number": { "type": "keyword" },
					"issue_date": { "type": "date", "format": "mm/dd/yyyy" },
					"violation_time": {"type": "keyword"},
					"violation": { "type": "keyword" },
					"fine_amount": { "type": "float" },
					"penalty_amount": { "type": "float" },
					"interest_amount": { "type": "float" },
					"reduction_amount": { "type": "float" },
					"payment_amount": { "type": "float" },
					"amount_due": { "type": "float" },
					"precinct": { "type": "keyword" },
					"county": { "type": "keyword" },
					"issuing_agency": { "type": "keyword" }
					}
				}
			})
		
		print(r.status_code)
		r.raise_for_status()
	except Exception as e:
		print(e)
	
	
	for i in range(0, args.num_pages):
		violations = Socrata("data.cityofnewyork.us", APP_TOKEN).get(DATASET_ID, limit=args.page_size, offset=i*(args.page_size))
		for violation in violations:
			try:
				violation["plate"] = violation["plate"],
				violation["state"] = violation["state"],
				violation["license_type"] = violation["license_type"],
				violation["summons_number"] = violation["summons_number"],
				violation["issue_date"] = violation["issue_date"],
				violation["violation_time"] = violation["violation_time"],
				violation["violation"] = violation["violation"],
				violation["fine_amount"] = float(violation["fine_amount"]),
				violation["penalty_amount"] = float(violation["penalty_amount"]),
				violation["interest_amount"] = float(violation["interest_amount"]),
				violation["reduction_amount"] = float(violation["reduction_amount"]),
				violation["payment_amount"] = float(violation["payment_amount"]),
				violation["amount_due"] = float(violation["amount_due"]),
				violation["precinct"] = violation["precinct"],
				violation["county"] = violation["county"],
				violation["issuing_agency"] = violation["issuing_agency"] 
			
				r = requests.post(f"{ES_HOST}/parkingdata/_doc",auth=HTTPBasicAuth(ES_USERNAME,ES_PASSWORD),json=violation)
			except Exception as e:
				print(e)  
				continue


