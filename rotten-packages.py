import json
import requests
from tabulate import tabulate

with open ('package.json') as f:
    package = json.load(f)

    packageList = []
    print(f"request {len(package['dependencies'].keys())} packages, this may take a while.")
    for key, value in package['dependencies'].items():
        response = requests.get('https://registry.npmjs.org/'+key)
        data = response.json()
        packageList.append([key, data['time']['modified'], data.get('homepage','')])

    print(tabulate(packageList, headers=['Package', 'Last Modified', 'Homepage']))