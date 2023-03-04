import json
import csv
# E:\CODE TEMPLE\FInal Project\SMT Flask backend\app\demon_data.json


# with open('app\demondata.json') as json_file:
#     data = json.load(json_file)

# demons = data["Demons"]

# data_file = open('data_file.csv', 'w')

# csv_writer = csv.writer(data_file)

# count=0

# for demon in demons:
#     if count == 0:
#         header = demon.keys()
#         csv_writer.writerow(header)
#         count += 1

#     csv_writer.writerow(demon.values())
    
# data_file.close()

with open('app\demondata.json') as f:
    demondata = json.load(f)

print(demondata)

with open('app\skillData.json') as d:
    skilldata = json.load(d)

print(skilldata)



