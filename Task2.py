"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def updateDict(item, dict):
    if item[0] in dict:
        dict[item[0]] += int(item[3])
    elif item[0] not in dict:
        dict[item[0]] = int(item[3])
    if item[1] in dict:
        dict[item[1]] += int(item[3])
    elif item[1] not in dict:
        dict[item[1]] = int(item[3])
    return dict

records = {}
for i in calls:
    records = updateDict(i, records)

key = max(records, key=lambda x: records[x])
print(f"{str(key)} spent the longest time, {str(records.get(key))} seconds, on the phone during September 2016.")
