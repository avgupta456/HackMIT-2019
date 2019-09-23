import os
import sys

import numpy as np

from helper import abbrev

def repNum(str):
    try:
        return float(str)
    except ValueError:
        try: return float(str[1:])
        except ValueError: return -1

def getItems(data):
    items = []
    prices = []

    lines = data.readlines()
    for line in lines:
        if(line[-4]==46):
            item = " ".join(str(line).split(" ")[0:-2]).strip().lstrip("'b \t")
            price = str(line).split(" ")[-1].strip().rstrip("\\'\"n ").lstrip('$USD ')

            items.append(item.lstrip("123456789 "))
            prices.append(float(price.lstrip("T$")))

    totals = []
    for i in range(len(items)):
        if ("total" in items[i].lower()):
            totals.append(prices[i])

    total = max(totals)

    newItems = []
    newPrices = []
    avoid = ["tax", "total", "phone", "price", "discount",
        "amount", "amex", "visa", "change", ":"]
    for i in range(len(items)):
        skip = False
        for word in avoid:
            if(word in items[i].lower()): skip = True

        if(prices[i]>total): skip = True

        if(items[i]==""): skip = True

        if(not skip):
            newItems.append(items[i])
            newPrices.append(prices[i])

    total = sum(newPrices)
    return [newItems, newPrices, total]
