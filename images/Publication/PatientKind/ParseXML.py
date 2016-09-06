import logging
import xml.etree.ElementTree as ET
import pickle
import json
import glob


def maybe_get_text(node):
    if node is None:
        return node
    else:
        return node.text
    
def parse_article(filename):
    tree = ET.parse(filename)
    root = tree.getroot()   
        
    articles = {}
    for article in root.findall('.//MedlineCitation'):
        pmid = maybe_get_text(article.find('.//PMID'))
        authors = []
        for author in article.findall('.//Author'):
            last_name = maybe_get_text(author.find('.//LastName'))
            fore_name = maybe_get_text(author.find('.//ForeName'))
            
            authors.append([fore_name, last_name])
            
        abstract = maybe_get_text(article.find('.//AbstractText'))
        title = maybe_get_text(article.find('.//ArticleTitle'))
        pub_time = maybe_get_text(article.find('.//DateCreated/Year'))
        #assert pmid not in articles, "Found duplicate PMID: {}".format(pmid)
        articles[pmid] = {
            'authors': authors,
            'abstract': abstract,
            'title': title,
            'pub_time': pub_time
        } 
    
    return articles

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

def batch(file_list):
    '''Given a list of file names, combine all files into a dictionary'''
    z = {} #z is the dictionary to be returned
    
    #this for loop is to assign names to the files
    for i in range(len(file_list)):
        if file_list[i] < 10:
            filename = 'medline16n000{}.json'.format(file_list[i])
        elif file_list[i] < 100:
            filename = 'medline16n00{}.json'.format(file_list[i])
        elif file_list[i] < 1000:
            filename = 'medline16n0{}.json'.format(file_list[i])
        else:
            filename = 'medline16n{!0d}.json'.format(file_list[i])
            
        logging.warn('Loading article: {}'.format(filename))
        
        #Open each file and merge them into one dictionary
        data = json.load(open(filename, 'r'))
        z = merge_two_dicts(z, data)

        
    return z
                
if __name__ == '__main__':
    
    filename = 'medline16n0001.xml'
    data = parse_article(filename)
    
    with open('medline16n0001.json', 'w') as file:
        json.dump(data, file)
    
    
    #author_info = pickle.load(open('author_info.p',  'rb'))
    
    #articles_to_extract = set()
    # get a set of all article ids from the author dictionary
    
    #gene_reviews_pub = {}
    
    #for name in author_info:
        #articles_to_extract.update(author_info[name]['Publications'])
    
    #for filename in glob.glob("medline*.json"):
        #logging.warn('Loading article: {}'.format(filename))
        #with open(filename) as input_file:
            #data = json.load(input_file)
        #for pmid in articles_to_extract:
            #if pmid in data.keys():
                #gene_reviews_pub[pmid] = data[pmid]
    
        # data is in 'data' and the file is closed
        # for each article
          # if it's in articles_to_extract, then save it in our extracted article dictionary
          
#---------------------------------------------------------------------------------------------------    
    
    
                    
    
                              
    
    
    
    #full_dict = {}
    #for i in range(1, 1076):
        #if i < 10:
            #filename = filename = 'medline16n000{}.xml'.format(i)
        #elif i < 100:
            #filename = 'medline16n00{}.xml'.format(i)
        #elif i < 1000:
            #filename = 'medline16n0{}.xml'.format(i)
        #else:
            #filename = 'medline16n{}.xml'.format(i)
            
        #logging.warn('Loading article: {}'.format(filename))
        #data = parse_article(filename)
        #if i < 10:
            #with open('medline16n000{}.json'.format(i), 'w') as fp:
                #json.dump(data, fp)            
        #elif i < 100:
            #with open('medline16n00{}.json'.format(i), 'w') as fp:
                #json.dump(data, fp)                     
        #elif i < 1000:
            #with open('medline16n0{}.json'.format(i), 'w') as fp:
                #json.dump(data, fp)                     
        #else:
            #with open('medline16n{}.json'.format(i), 'w') as fp:
                #json.dump(data, fp)     
                
        #if i < 10:
            #data = json.load(open('medline16n000{}.json'.format(i), 'r'))
        #elif i < 100:
            #data = json.load(open('medline16n00{}.json'.format(i), 'r'))
        #elif i < 1000:
            #data = json.load(open('medline16n0{}.json'.format(i), 'r'))
        #else:
            #data = json.load(open('medline16n{}.json'.format(i), 'r'))
        
        #full_dict = merge_two_dicts(full_dict, data)
        
            
    #z = {}
    #for i in range(1000, 1045):
        #a = json.load(open('data' + str(i) + '.json', 'r'))
        #z = {**z, **a}        
            
    #z = {}
    #for i in range(1000, 1045):
        #a = pickle.load(open('articles' + str(i) + '.p', 'rb'))
        #z = {**z, **a}

