import pandas as pd
import urllib.request
import urllib.error
import urllib.parse
import pprint
import urllib3
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from scipy import stats
#feed in text information, parse into format that can then be looked up as a zpid
section_index = 0
#0 - All School
#1 - Upper School
#2 - Middle School
#3 - Lower School
#4 - Class 4
#5 - Class 3
#6 - Class 2
#7 - Class 1
def choose_body(school_index):
    school_file = open('groups/all_school.txt', 'r')
    school_file.close()
    if(school_index == 0):
        school_file = open('groups/all_school.txt','r')
    elif(school_index == 1):
        school_file = open('groups/upper_school.txt','r')
    elif(school_index == 2):
        school_file = open('groups/middle_school.txt','r')
    elif(school_index == 3):
        school_file = open('groups/lower_school.txt','r')
    elif(school_index == 4):
        school_file = open('groups/class_4.txt', 'r')
    elif(school_index == 5):
        school_file = open('groups/class_3.txt', 'r')
    elif(school_index == 6):
        school_file = open('groups/class_2.txt', 'r')
    elif(school_index == 7):
        school_file = open('groups/class_1.txt', 'r')
    return(school_file)
def choose_value(school_index, read=False):
    value_file = open('groups/values.txt','r')
    value_file.close()
    if read:   
        if(school_index == 0):
            value_file = open('groups/values.txt','r')
        elif(school_index == 1):
            value_file = open('groups/upper_values.txt','r')
        elif(school_index == 2):
            value_file = open('groups/middle_values.txt','r')
        elif(school_index == 3):
            value_file = open('groups/lower_values.txt','r')
        elif(school_index == 4):
            value_file = open('groups/class_4_values.txt', 'r')
        elif(school_index == 5):
            value_file = open('groups/class_3_values.txt', 'r')
        elif(school_index == 6):
            value_file = open('groups/class_2_values.txt', 'r')
        elif(school_index == 7):
            value_file = open('groups/class_1_values.txt', 'r')
    else:
        if(school_index == 0):
            value_file = open('groups/values.txt','w')
        elif(school_index == 1):
            value_file = open('groups/upper_values.txt','w')
        elif(school_index == 2):
            value_file = open('groups/middle_values.txt','w')
        elif(school_index == 3):
            value_file = open('groups/lower_values.txt','w')
        elif(school_index == 4):
            value_file = open('groups/class_4_values.txt', 'w')
        elif(school_index == 5):
            value_file = open('groups/class_3_values.txt', 'w')
        elif(school_index == 6):
            value_file = open('groups/class_2_values.txt', 'w')
        elif(school_index == 7):
            value_file = open('groups/class_1_values.txt', 'w')
    return(value_file)
school_file = choose_body(section_index)
students = school_file.read()
school_file.close()
alone = students.split("\ny\n")

#print(alone[58])
#print(alone)
pull_data = False
address = []
for item in alone:
    lines = item.split("\n")
    for j in range(0,len(lines)):
        if(lines[j] != ''):
            if(lines[j][0].isdigit()):
                output = [lines[j],lines[j+1]]
                address.append(output)
#print(address)
#perform zillow lookup for each number/city combo in address

bvlax = open("groups/BHockey.txt",'r')
gsoccer = open("groups/VGSoccer.txt" , 'r')
bsoccer = open("groups/VBSoccer.txt", 'r')
glax = open("groups/VGLax.txt", 'r')
bbasketball = open("groups/BVBasketball.txt",'r')
ghockey = open("groups/VGHockey.txt", 'r')
gbasketball = open("groups/GVBasketball.txt", 'r')
bhockey = open("groups/BHockey.txt", 'r')

def searchByTeam(roster):
    roster_addresses = []
    team = roster.read()
    print(team.split('\n'))
    names = team.split("\n")
    team_addresses = []
    #print(names)
    for item in team.split('\n'):
        direct = list(filter(lambda x: item in x, alone))
        print(direct)
        team_addresses.extend(direct)
    #print(team_addresses)
    for item in team_addresses:
        #print(item)
        pass
    #print(team_addresses)          
    '''
    for item in team.split('\n'):
        print(item)
        if any(item in s for s in alone):
            team_addresses.append(s)
        for entry in alone:
            print(entry)
            if item in entry:
                #print(item + entry[1])
                team_addresses.append(entry)
    '''
    for item in team_addresses:
        lines = item.split("\n")
        #print(lines)
        for j in range(0,len(lines)):
            if(lines[j] != ''):
                if(lines[j][0].isdigit()):
                    output = [lines[j],lines[j+1]]
                    roster_addresses.append(output)
    
    return roster_addresses
bvlaxhouse = searchByTeam(bvlax)
gsoccerhouse = searchByTeam(gsoccer)
bsoccerhouse = searchByTeam(bsoccer)
glaxhouse = searchByTeam(glax)
bbasketballhouse = searchByTeam(bbasketball)
ghockeyhouse = searchByTeam(ghockey)
gbasketballhouse = searchByTeam(gbasketball)
bhockeyhouse = searchByTeam(bhockey)
teamhouses = [bvlaxhouse,gsoccerhouse,bsoccerhouse,glaxhouse,bbasketballhouse,ghockeyhouse,gbasketballhouse,bhockeyhouse]
print(len(searchByTeam(bvlax)))

zillow_data = "X1-ZWz18slaw8c3kb_ako3m"
request = "http://www.zillow.com/webservice/GetSearchResults.htm?"
values = []
def lookup(zillow_data, address, cityzip):
    f = {'zws-id' : zillow_data, 'address':address,'citystatezip':cityzip}
    sample = request + urllib.parse.urlencode(f)
    #print(sample)
    with urllib.request.urlopen(sample) as response:
        #pprint.pprint(response.read())
        reply = response.read()
        decoded_reply = reply.decode('ascii')
        #print(decoded_reply)
        #print(reply)
        #p = etree.fromstring(response)
        #values = xp.xpath('//amount/text()')
        str1 = '<amount currency=\"USD\">'
        str2 = '</amount>'
        start = decoded_reply.find(str1)
        start += len(str1)
        end = decoded_reply.find(str2)
        #print(start, end)
        if(start != -1 and end != -1 and start != end):
            return(int(decoded_reply[start:end]))

value_file = choose_value(section_index, True)
contents = value_file.read()
new_values = contents.split("\n")
if contents == '':
    pull_data = True
    value_file.close()
if(pull_data == False):
    for item in new_values:
        if item != 'None' and item != '':
            values.append(int(item))
    #print(values)
    #print(np.mean(values))
    #print(np.std(values))
    #print(np.min(values))
    #print(np.max(values))
    #print(np.median(values))
    ##plt.show()
else:
    value_file = choose_value(section_index)
    for pair in address:
        price = lookup(zillow_data,pair[0],pair[1])
        values.append(price)
        value_file.write(str(price)+ "\n")
    value_file.close()

for i in range(8):
    value_file = choose_value(section_index, True)
    contents = value_file.read()
    new_values = contents.split("\n")
    temp = []
    for item in new_values:
        if item != 'None' and item != '':
            temp.append(int(item))
    #plt.boxplot(temp)
#plt.tight_layout()
temporary = []
print(len(bvlaxhouse))
'''
for item in bvlaxhouse:
    print("item 0 : " + item[0])
    print("item 1 : " + item[1])
    term = lookup(zillow_data, item[0],item[1])
    if term is not None:
        temporary.append(int(term))
    #print(term)
'''
team_values = []
written = False
if(written == False):
    for team in teamhouses:
        entry = []
        for item in team:
            term = lookup(zillow_data, item[0], item[1])
            if term is not None:
                entry.append(int(term))
        team_values.append(entry)
    team_value_file = open("groups/team_values.txt", 'w')
    for item in team_values:
        for index in item:
            team_value_file.write(str(item) + ', ')
        team_value_file.write('\n')
    team_value_file.close()
else:
    team_value_file = open("groups/team_values.txt", 'r')
    #print(team_value_file.read())
    
    '''bleh = team_value_file.read().split('\n')
    for item in bleh:
        garbage = item[1:len(item)-1].split(',')
        temp_entry = []
        for item in garbage:
            temp_entry.append(item)
        team_values.append(temp_entry)
    '''
    print(team_value_file.read())
    team_value_file.close()

'''
print("Mean house values: " + str(np.mean(temporary)))
print("Standard Deviation: " + str(np.std(temporary)))
print("Sample Size: " + str(len(temporary)))
'''

print(team_values)
#print(np.mean(values))
'''
fig = plt.figure(1, figsize=(9,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(team_values)
fig.savefig('fig1.png', bbbox_inches='tight')
'''
percentiles = []
for item in team_values:
    p = stats.percentileofscore(values, np.mean(item))
    percentiles.append(p)
print(percentiles)
print(stats.percentileofscore(values,2298384))
team_values.append(values)
mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)
ax.boxplot(team_values)
ax.set_xticklabels(['BVLax', 'GVSoccer', 'BVSoccer', 'GVLax', 'BVBall', 'GVHockey', 'GVBall','BVHockey', 'Upper School'])


print("Mean " + str(np.mean(values)))
print("SD " + str(np.std(values)))
print("N: " + str(len(values)))
plt.show()
