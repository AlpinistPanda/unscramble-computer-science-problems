"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

lenTexts = len(texts)
lenCalls = len(calls)

def getTime(str):
    date, time = list(str.split(' '))
    return time

def getSeconds(str):
    hours, minutes, seconds = list(str.split(':'))
    return seconds

print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {getTime(texts[0][2])}" )
print(f"Last record of calls, {calls[lenCalls-1][0]} calls {calls[lenCalls-1][1]} at time {getTime(calls[lenCalls-1][2])} lasting {calls[lenCalls-1][3]} seconds.")
