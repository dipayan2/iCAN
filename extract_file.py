import numpy as np 
import pandas as pd 
import bigjson
import os
import json 

element_dict = {
    "id":0,
    "authors": [],
    "year": 0,
    "n_citation": 0,
    "references": [],
    "venue_ID": 0
}

def process_authors(authors):
    out = []
    for s_dict in authors:
        out.append(s_dict['id'])
    return out

citaion_dict = {} #This one stores the dictionary of dictionaries in the list

## Reading the brobdingnagian file

with open('dblp.v12.json','rb') as f:
    result_data = bigjson.load(f)
    id_count = 0
    for element in result_data:
        #Adding the id of the paper
        data_dict = {} # set an empty dict to add to the big dict
        #Adding the id of the paper
        data_dict['id'] = element['id']

        #Adding the references
        data_dict['references'] = []
        if 'references' in element.keys():
            data_dict['references'].append(list(element['references']))

        else:
            data_dict['references'].append(np.nan)

        #Adding venue ID
        data_dict['venue_ID'] = np.nan
        if 'venue' in element.keys():
            if 'id' in element['venue'].keys():
                data_dict['venue_ID'] = element['venue']['id']
        
        #Adding the year of publishing
        data_dict['year'] = np.nan
        if 'year' in element.keys():
            data_dict['year']= element['year']

        #Adding the list of authors
        data_dict['authors'] = []
        if 'authors' in element.keys():
            data_dict['authors'].append(process_authors(element['authors']))
        else:
            data_dict['authors'].append(np.nan)
        
        #Adding number of citations
        data_dict['n_citation'] = 0
        if 'n_citation' in element.keys():
            data_dict['n_citation'] = element["n_citation"]
        
        #Adding data to big dump
        citaion_dict[id_count] = data_dict
        id_count  += 1
        if id_count%100000 == 0:
            print(f"Number of records processes {id_count}")

#Data processing completed
print("Data processed, and did not crash yet!!")
with open('citaion_stripped.json','w') as fp:
    json.dump(citaion_dict,fp)

print("Process complete..Exiting system")

 
        


        



