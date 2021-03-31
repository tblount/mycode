#!/usr/bin/env python3

# create the list called vendors / farms
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across the list vendors
for x in farms:
    print(x)
print("\nOur loop has ended.")  # when the loop ends print this
