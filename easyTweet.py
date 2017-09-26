#!/usr/bin/env python3
import json
import re

searchword = ['han', 'hon', 'hen', 'penis']

total = {}
for i in searchword:
    total[i] = 0
print(total)

with open('/home/ubuntu/hello-world/data/0c7526e6-ce8c-4e59-884c-5a15bbca5eb3', 'r') as f:
    for line in f:
        line = line.strip()
        if not line == "":
            tweet = json.loads(line)
            if tweet['text'].split()[0] == 'RT':
                continue
            text = (tweet['text'])

            # count occurence and save in total
            for word in searchword:
                count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word.upper()), text.upper()))
                total[word] = total[word] + count
                count = 0
print(total)
