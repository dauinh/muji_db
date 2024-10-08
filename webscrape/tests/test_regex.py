# tests/test_regex.py
import re

list = [
    "https://www.muji.us/collections/tableware",
    "https://www.muji.us/collections/bedding",
    "https://www.muji.us/collections/storage-organizers",
    "https://www.muji.us/collections/aroma-fragrances",
    "https://www.muji.us/collections/pen-pencils",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
    "https://www.muji.us/collections/#",
]
results = []
for l in list:
    x = re.search(".*/collections/[\w-]*$", l)
    if x:
        results.append(l)
print(results)
