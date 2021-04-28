#!/usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


choose_farm = input('pick a farm [NE Farm, W Farm, SE Farm] ')
farmKey=""

for data in farms:
    for key,value in data.items():
        #print (key, "->", value)
        if (key=="name"):
            farmKey =value
        elif farmKey==choose_farm and key=="agriculture":
                #print(value)
                for agridata in value:
                    #print(agridata,"test.....")
                    if(agridata not in ('carrots','celery')):
                        print( agridata)
