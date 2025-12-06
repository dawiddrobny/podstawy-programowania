import json
import urllib.request

url = "http://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json"
file_name = "euro.json"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f"{'Date':<15} {'Buying Rate':<15} {'Selling Rate':<15}")
print("="*45)

for rate in data['rates']:
    print(f"{rate['effectiveDate']:<15} {rate['bid']:<15.4f} {rate['ask']:<15.4f}")