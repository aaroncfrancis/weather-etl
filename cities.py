from datapackage import Package
import pandas as pd

package = Package('https://datahub.io/core/world-cities/datapackage.json')

# print list of all resources:
print(package.resource_names)

for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        f = open('cities.csv', 'w')
        print(resource.read())