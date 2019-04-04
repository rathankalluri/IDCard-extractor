import io
import re
from . import config
import json

def get_dob(raw_text):
    #print (re.findall('\d{2}[/.-]\d{2}[/.-]\d{4}',raw_text))
    return re.findall('\d{2}[/.-]\d{2}[/.-]\d{4}',raw_text)

def get_ID(key, raw_text, default=0):
    if default:
        #print (re.findall(key,raw_text))
        return re.findall(key,raw_text) 
    else:   
        #print (config.patterns.get(key))
        #print (re.findall(config.patterns.get(key),raw_text))
        return re.findall(config.patterns.get(key),raw_text)

def get_issueDate(key, raw_text):
    #print (re.findall('\d{2}[/.-]\d{2}[/.-]\d{4}',raw_text))
    return re.findall('\d{2}[/.-]\d{2}[/.-]\d{4}',raw_text)

def get_name(raw_text,index, key):
    raw_list = raw_text.splitlines()
    try:
        if key == "PASSPORT":
            indices = [i for i, k in enumerate(raw_list) if 'name' in k.lower()]
            name = ''
            for n in indices:
                name = name+raw_list[n+1]+' '
            nm = name
        else:
            nm = raw_list[index]
    except Exception:
        nm = ''
    return nm

def get_list(key):
    return config.id_list.get(key)

def get_data(key,raw_text):
    lst = get_list(key)
    
    DOB,ID,IssueDate,Name = '','','',''
    #print (lst)

    if "DOB" in lst:
        DOB = get_dob(raw_text)
    if "ID" in lst:
        ID = get_ID(key, raw_text,0)
    if "Name" in lst:
        Name = get_name(raw_text, lst[0], key)
    if "Issued On" in lst:
        IssueDate = get_issueDate(key, raw_text)
    if key == "PASSPORT":
        resp = {'DOB': DOB[0], 'ID': ID,'Name':Name, 'IssueDate':DOB[1]}
    else:
        resp = {'DOB': DOB, 'ID': ID,'Name':Name, 'IssueDate':IssueDate}
    return resp

def get_raw_data(raw_text):
    
    DOB,ID,IssueDate,Name = '','','',''

    DOB = get_dob(raw_text)
    r = re.compile('(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]{8,16})')
    ID = get_ID(r, raw_text,1)

    resp = {'DOB': DOB, 'ID': ID}
    return resp


# [START vision_text_detection]

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_text_detection]

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')
    #print(texts[0].description)
    raw_text = texts[0].description 
    for (key, value) in list(config.patterns.items()):
        if re.search(value, raw_text):
            print('{} card found'.format(key))
            data = get_data(key, raw_text)
            if data:
            	data['Type'] = key
            break
    else:
        #print ("Could not identify ID type, this is what we found :")
        data = get_raw_data(raw_text)
        if data:
        	data['Type'] = 'None Found'

    return (data)