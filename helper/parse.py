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
    totals = []
    print_next = False
    for item in data['Blocks']:
        if item['BlockType'] == 'LINE':
            if(print_next):
                totals.append(item['Text'])
                print_next = False
            if("total" in item['Text'].lower()):
                print_next = True

    newTotals = []
    for i in range(len(totals)): newTotals.append(repNum(totals[i]))
    total = max(newTotals)

    items = []
    prices = []
    prev = None
    for item in data['Blocks']:
        if item['BlockType'] == 'LINE':
            if(repNum(item['Text'])>0):
                items.append(prev)
                prices.append(repNum(item['Text']))
            elif(len(item['Text'])>3):
                prev = item['Text']

    newItems = []
    newPrices = []
    avoid = ["tax", "total", "phone", "price", "discount",
        "amount", "amex", "visa", "change", ":"]
    for i in range(len(items)):
        skip = False
        for word in avoid:
            if(word in items[i].lower()): skip = True

        if(prices[i]>total): skip = True

        if(not skip):
            newItems.append(abbrev.complete(items[i].lstrip('0123456789.-X ')))
            newPrices.append(prices[i])

    total = sum(newPrices)
    return [newItems, newPrices, total]
