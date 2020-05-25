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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_numbers = set(number[0] for number in calls)
incoming_numbers = set(number[1] for number in calls)
only_outgoing = outgoing_numbers.difference(incoming_numbers)
text_numbers = set(number[0] for number in texts)
text_numbers = set(number[1] for number in texts)

telemarketers_set = set()
telemarketers_set = only_outgoing.difference(text_numbers)
print("These numbers could be telemarketers:")
print("\n".join(sorted(telemarketers_set)))
