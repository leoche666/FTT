'''
FTT settings for project.
'''
import os
resource=os.path.abspath(r"../cases")
#encoding
LANGUAGE_CODE = 'utf-8'

#multi-thread
THREAD={'ISTHREAD':False,
        'LIMIT_THREAD':10,}

#for multi-thread,it can be empty if the key of 'ISTHREAD' is 'False' 
WORKDIRCTORY=r""


#testdb database
DATABASES = {
    'start-up': False,
    'engine': 'mysql',
    'settings': {
        'name': 'testdb',
        'user':'tester',
        'passwd':'xxx',
        'db':'testdb',
        'host':'xxx',
        'port':'3306',
        'encode':'utf8',
                },
             }

xml_path=os.path.join(resource,"website.xml")
log_path=os.path.join(resource,"log.txt")
html_path=os.path.join(resource,"report.html")
option="v:1"

OPTIONS={'xml':xml_path,'opt':option,'log':log_path,'html':html_path,
         }