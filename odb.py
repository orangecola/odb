import json, urllib3
from datetime import datetime, timedelta

def odb(event, context):
	http = urllib3.PoolManager()
	now = datetime.now()
	now += timedelta(hours=8)
	print(now)
	raw_html = http.request('GET', 'https://api.experience.odb.org/devotionals/v2?site_id=1&status=publish&country=SG&on=' + str(now.month) + '-' + str(now.day) + '-' + str(now.year))
	req = json.loads(raw_html.data)
	return {
		"statusCode": 302,
		"headers": {
			"Location": req[0]["bible_in_a_year_url"]
		},
		"body": json.dumps(dict())
	}

if __name__ == '__main__':
	print(odb([], []))