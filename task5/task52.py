import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

sortjs = dict(sorted(sampleJson.items()))

with open('sort.json' , 'w') as json_file:
    json.dump(sortjs, json_file, indent=4)