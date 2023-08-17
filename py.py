#!/usr/bin/python3
import sys
import requests
from lxml import html
import re

states = [('f2ab504a-503d-4216-b4e3-d6ee676d0f16', 'vczmclkril', [
    ('f6a92db1-1a67-4975-8381-ea95731fad6b', 'dzjmnmihny'), 
    ('8478c2d5-d9cf-4893-a381-a6307914a11f', 'khpiaeezfs'), 
    ('a4e63494-4232-4e09-bc9d-09720d767704', 'mroevsntnd'), 
    ('959faf21-c328-46b1-a04d-7e117093396b', 'phwhznewde'), 
    ('33903e35-c164-4c76-a004-9e3c1586bbe4', 'txyzbwdqqu')])]

NO_PROXY = {
    'no': 'pass',
}


## Request
page = requests.get('http://0.0.0.0:5000/states/f2ab504a-503d-4216-b4e3-d6ee676d0f16', proxies=NO_PROXY)
if int(page.status_code) != 200:
    print("Status fail: {}".format(page.status_code))
    sys.exit(1)

## Parsing
tree = html.fromstring(page.content)
if tree is None:
    print("Can't parse page")
    sys.exit(1)

## H1
h1_tags = tree.xpath('//body/h1/text()')
if h1_tags is None or len(h1_tags) == 0:
    print("H1 tag not found")
    sys.exit(1)

if not re.search(r".*State.*", h1_tags[0]):
    print("Title `State` doesn't found")
    sys.exit(1)

if states[0][1] not in h1_tags[0]:
    print("`State` name doesn't found")
    sys.exit(1)

## H3
h3_tags = tree.xpath('//body/h3/text()')
if h3_tags is None or len(h3_tags) == 0:
    print("H3 tag not found")
    sys.exit(1)

if not re.search(r".*Cities.*", h3_tags[0]):
    print("Title `Cities` doesn't found")
    sys.exit(1)

## LI city ID
li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/text()')]))
if li_tags is None or len(li_tags) != len(states[0][2]):
    print("Doesn't find {} LI tags (found {})".format(len(states[0][2]), len(li_tags)))
    sys.exit(1)

for li_tag in li_tags:
    is_found = False
    for city_tuple in states[0][2]:
        is_found = re.search(r".*{}.*".format(city_tuple[0]), li_tag)
        if is_found:
            break
    if not is_found:
        print("{} not found".format(li_tag))
        sys.exit(1)
            
## LI state name sorted
li_tags_b = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/b/text()')]))
if li_tags_b is None or len(li_tags_b) != len(states[0][2]):
    print("Doesn't find {} LI tags with B tag (found {})".format(len(states[0][2]), len(li_tags_b)))
    sys.exit(1)

idx = 0
for li_tag in li_tags_b:
    if not re.search(r".*{}.*".format(states[0][2][idx][1]), li_tag):
        print("{} not found or not sorted".format(li_tag))
        sys.exit(1)
    idx += 1

print("OK", end="")
