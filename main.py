import numpy as np 
import pandas as pd 
import bigjson
import matplotlib.pyplot as plt
import os


count  = 0
graph_str = ''

element_dict = {'id':[],
                  'title':[],
                  'doc_type':[],
                  'publisher':[],
                  'venue_name':[],
                  'venue_ID':[],
                  'references':[],
                  'fos':[],
                  'year':[],
                  'authors':[]}


def process_fos(fos):
    out = []
    for s_dict in fos:
        out.append(s_dict['name'])
        out.append(s_dict['w'])
    return out
    

def process_authors(authors):
    out = []
    for s_dict in authors:
        out.append(s_dict['id'])
    return out



with open('dblp.v12.json', 'rb') as f:
    j = bigjson.load(f)
    while count<100000:
        if count % 100 == 0:
            print(count)
        new_row = ''
        element = j[count]

        element_dict['id'].append(element['id'])
        new_row += str(element['id']) + ' '

        if 'references' in element.keys():
            element_dict['references'].append(list(element['references']))
            for ref in list(element['references']):
                new_row += str(ref) + ' '
        else:
            element_dict['references'].append(np.nan)

        element_dict['title'].append(element['title'])

        if element['publisher'] != "":
             element_dict['publisher'].append(element['publisher'])
        else:
             element_dict['publisher'].append(np.nan)

        if element['doc_type'] != "":
            element_dict['doc_type'].append(element['doc_type'])
        else:
            element_dict['doc_type'].append(np.nan)

        if 'venue' in element.keys():
            if 'raw' in element['venue'].keys():
                element_dict['venue_name'].append(element['venue']['raw'])
            else:
                element_dict['venue_name'].append(np.nan)
            if 'id' in element['venue'].keys():
                element_dict['venue_ID'].append(element['venue']['id'])
            else:
                element_dict['venue_ID'].append(np.nan)
        else:
            element_dict['venue_name'].append(np.nan)
            element_dict['venue_ID'].append(np.nan)

        if 'fos' in element.keys():
            element_dict['fos'].append(process_fos(element['fos']))
        else:
            element_dict['fos'].append(np.nan)

        if 'year' in element.keys():
            element_dict['year'].append(element['year'])
        else:
            element_dict['year'].append(np.nan)

        if 'authors' in element.keys():
            element_dict['authors'].append(process_authors(element['authors']))
        else:
            element_dict['authors'].append(np.nan)

        count = count + 1

        graph_str += new_row[:-1] + '\n'


data = pd.DataFrame.from_dict(element_dict)
print(data.head(10))

data.to_csv("citation_network_100k.csv", index=False)

with open('graph_adjlist_100k.txt', 'w') as f:
    f.write(graph_str)



