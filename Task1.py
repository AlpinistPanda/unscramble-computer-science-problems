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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

#sets are unordered and it has unique elements (duplicates are not allowed)

text = set(i[0] for i in texts).union(set(i[1] for i in texts))
call = set(i[0] for i in calls).union(set(i[1] for i in calls))

# length of the union of text set and call set
len_union = len(text.union(call))


print(f"There are {len_union} different telephone numbers in the records.")
