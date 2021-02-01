import requests, json

def price(sym:str):
	s = json.loads(requests.get("http://flask-stock-prices-python.thepeeps191.repl.co/price?sym="+sym).text)
	return s

'''
Usage:
	print(price("symbol"))
'''

# Cenovus Energy
cve = price("cve")
print(cve['price'])

'''
{'detail': 'valid', 'symbol': 'CVE', 'price': '6.11'}
'''