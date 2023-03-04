# import json 





# with open('skill_data.json', 'r') as file:
#     skill_data = json.load(file)




# print(skill_data)

def finddemon(demon):
    # Probably commands here to pull info from elephantsql database
    if response.ok:
        demon_dict = {}
        demon_dict['name'] = my_dict['name']
        demon_dict['Image'] = my_dict['Image']
        demon_dict['HP'] = my_dict['HP']
        demon_dict['Strength'] = my_dict['Strength']
        demon_dict['Defense'] = my_dict['Defense']
        demon_dict['Weak'] = my_dict['Weak']
        demon_dict['Null'] = my_dict['Null']
        demon_dict['Repel'] = my_dict['Repel']
        demon_dict['Lore'] = my_dict['Lore']
        return demon_dict
    else:
        raise Exception("The demon you're looking for does not exist.")
    
def get_skill_data(skillname):
    #Probably pull from DB to get skill name from the demon table

    if response.ok:
        skill_dict = {}
        skill_dict['name'] = my_dict2['name']
        skill_dict['Type'] = my_dict2['Type']
        skill_dict['Affinity'] = my_dict2['Affinity']
        skill_dict['Range'] = my_dict2['Range']
        skill_dict['Power'] = my_dict2['Power']
        return skill_dict
    else:
        raise Exception("Error getting skill data")


    
    