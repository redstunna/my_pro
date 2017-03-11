import os
import sys
import requests
import datetime
from pymongo import MongoClient



#----test mongodb-------
'''
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

sys.exit()
'''
def fill_post(vac):
    out_dict = {}
    out_dict["id"] = vac["id"]
    out_dict["url"] = vac["alternate_url"]
    out_dict["name"] = vac["name"]
    out_dict["created_at"] = vac["created_at"]
    out_dict["employer"] = vac["employer"]["name"]
    #-------check salary-------
    if (vac["salary"]!=None):
        out_dict["salary"] = vac["salary"]
    else:
        out_dict["salary"] = None
    #--------------------------
    #out_dict["city"] =  vac["address"]["city"]
    if (("address" in vac)and(vac["address"]!=None)):
        out_dict["city"] = vac["address"]["city"]
    else:
        out_dict["city"] = None
    '''
    if ("city" in vac["address"]):
        out_dict["city"] = vac["address"]["city"]
    else:
        out_dict["city"] = None
    '''
    #--------------------------
    if ("experience" in vac):
        out_dict["experience"] = vac["experience"]
    else:
        out_dict["experience"] = None
    #--------------------------
    if ("key_skills" in vac):
        out_dict["key_skills"] = vac["key_skills"]
    else:
        out_dict["key_skills"] = None

    out_dict["snippet"] = vac["snippet"]

    return out_dict

def check_id(id, posts):
    label = posts.find_one({"id":id})
    #print(id)
    #print(label)
    #sys.exit()
    if (label == None):
        return True
    else:
        return False

    #out_dict[""]

#------set db connections-----
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
posts = db.posts
#post_id = posts.insert_one(post).inserted_id

'''
idd = "19704034"
label = check_id(idd, posts)
print(label)
'''
#print(posts.find_one({"id":"19740614"}))


#-----get vacancies--------
sett_vac = {"text":"python программист",
            "per_page":100}
url = "https://api.hh.ru/vacancies/"
req = requests.get(url, params=sett_vac)


num_pages = req.json()["pages"]
found = req.json()["found"]
print("num_pages = ", num_pages)
print("found = ", found)
#for i in range(0,num_pages):
for i in range(0,num_pages):
    sett_vac = {"text": "python программист",
                "per_page": 100,
                "page":i}

    req = requests.get(url, params=sett_vac)

    if (req.status_code != 200):
        print("error with request for page ", i)

    vac_lst = req.json()["items"]

    for vac in vac_lst:
        vac_id = vac["id"]
        id_label = check_id(vac_id, posts)
        if (id_label):
            post_dict = fill_post(vac)
            try:
                post_id = posts.insert_one(post_dict).inserted_id
            except:
                print("Error with post")
        #--------deb-----
        #else:
        #    print("It was inserted")

    print("page ",i,"done")


print("done")
print(posts.count())
sys.exit()
print(req.json())

for key in req.json():
    print(key)
#collection.find({"id":"19740614"})
#for doc in collection.find({"id":"19740614"}):
#    print(doc)

sys.exit()

#-----get vacancies--------
sett_vac = {"text":"python программист"}
url = "https://api.hh.ru/vacancies/"
req = requests.get(url, params=sett_vac)

print(req.status_code)

vac_list = req.json()["items"]
vac = vac_list[0]
post = fill_post(vac)
post_id = posts.insert_one(post).inserted_id
print("first post done")
vac = vac_list[1]
post = fill_post(vac)
post_id = posts.insert_one(post).inserted_id
print("second post done")


sys.exit()

class Vacancy:
    url = None
    id = None
    name = None
    salary_to = None
    slary_from = None
    salary_curr = None
    company_name = None
    town = None
    country = None
    exper = None
    key_skills = None

#def fill_vac

sett_vac = {"text":"python программист"}
url = "https://api.hh.ru/vacancies/"
req = requests.get(url, params=sett_vac)

print(req.status_code)
print(req.json()['found'])

#print(req.json())
#for key in req.json():
#    print(key)

#sys.exit()


#------see-names------
lst = req.json()

vac = lst["items"]
print(type(vac))
for nm in lst:
    print(nm)

print(lst)
sys.exit()

lst = req.json()['pages']
lst = req.json()['items'][0]["name"]
#print(req.json()['items'][0])
#sys.exit()

vac_list = req.json()['items']
for vac in vac_list:
    print(vac["name"])

#print("-------page = ",req.json()['page'])

#------page 2-----
sett_vac = {"text":"python программист", "page":2}
url = "https://api.hh.ru/vacancies/"
req = requests.get(url, params=sett_vac)
print(req.status_code)
print(req.json()['found'])

vac_list = req.json()['items']
for vac in vac_list:
    print(vac["name"])

#print("-------page = ",req.json()['page'])
#print(lst)
sys.exit()
sett_head = None
acces_token = "TL87NUSABSOL5K22QBKBMVSJOF5B3I3F5GJ3C6L9FPATQ6N6L8TCNMTI8U4T1JGH"