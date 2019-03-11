

# d={'hou':'0','xu':'1','wang':'2','zhang':'3','li':'4'}
# print('hou:',d['hou'])
# print('xu:',d['xu'])
# print('wang:',d['wang'])
# print('zhang:',d['zhang'])
# print('li:',d['li'])

# for key, value in d.items(): 
#     print("\nKey: " + key) 
#     print(len(key)) 
#     print("Value: " + value) 

favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 } 
# for key,value in favorite_languages.items():
#     print('key:',key)
#     print('value',value)
'''
for name, language in favorite_languages.items(): 
    print(name.title() + "'s favorite language is " + 
    language.title() + ".") 
'''
# for name in favorite_languages.keys():
#     print(name.title())

    
friends=['phil','sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(name.title(),'喜欢的是',favorite_languages[name])
if 'erin' not in favorite_languages.keys():
    print("Erin is please take our poll")
    



