import json

# I. LIRE DES DONNÉES

with open("../data.json") as f:
    read_file = json.load(f)


# 1. Afficher dans la console le nombre d’utilisateurs.

print(f"nombre d'utilisateurs : {len(read_file['users'])}")

# 2. Afficher dans la console l’entreprise du second utilisateur.

print(f"la compagnie du 2eme utilisateur : {read_file['users'][1]['company']}")

# 3. Afficher dans la console le nom complet du troisième ami du second utilisateur.

print(f"nom complet du troisième ami du second utilisateur : {read_file['users'][1]['friends'][2]['name']}")

# 4. Afficher dans la console la couleur des yeux du premier utilisateur.

print(f"la couleur des yeux du premier utilisateur : {read_file['users'][0]['eyeColor']}")


# 5. Afficher dans la console l’adresse de chacun des utilisateurs.

for user in read_file["users"] : 
    for key,value in user.items():
        if key == 'address':
            print(f"adresse de {user['name']} : {value}")


# 6. Afficher dans la console le nombre d’utilisateurs dont le fruit favoris est la fraise.

strawberry_fan = 0

for user in read_file["users"] : 
    if user['favoriteFruit'] =='strawberry':
        strawberry_fan +=1

print(f"nombre d’utilisateurs dont le fruit favoris est la fraise : {strawberry_fan}")

# 7. Afficher le nombre de messages non lus de Brianna Huffman.

for user in read_file["users"] : 
    if user['name'] == 'Brianna Huffman':
        print(user['greeting'])


# 8. Calculer et afficher dans la console le pourcentage d’utilisateur masculin.
user_gender = len(read_file["users"])
male_gender = 0
for user in read_file["users"] :
    if user['gender'] == 'male':
        male_gender +=1

percent_male_user = round((male_gender/user_gender)*100)

print(f"le pourcentage d’utilisateur masculin: {percent_male_user} %")

# 9. Calculer et afficher la moyenne d’âge des utilisateurs féminins.
female_age = []
for user in read_file["users"] :
    if user['gender'] == 'female':
        female_age.append(user['age'])


result = 0
for i in (female_age):
    result += i
print(f"la moyenne d’âge des utilisateurs féminins : {round(result/len(female_age))} ans")

# 10. Calculer et afficher la somme des soldes de tous les utilisateurs.
total = 0.0

for user in read_file["users"] :
    if 'balance' in user.key():
        value_without_dollars = user['balance'].replace('$',"").replace(",","")
        new_value = value_without_dollars.replace(',','.')
        final_value = new_value.replace(".","",1)
        float_value = float(final_value)
        total += float_value
        
print(f"la somme des soldes de tous les utilisateurs : ${total}")


# 11. Afficher dans la console la ville où réside Zelma Sutton.
city_zelma =""
for user in read_file["users"] :
    if user['name'] == 'Zelma Sutton':
        city_zelma= user['address'] 
        print(f"la ville où réside Zelma Sutton : {city_zelma.split(',')[1]}")



# II. ÉCRIRE DES DONNÉES

# 1. Supprimer le second utilisateur.

del read_file["users"][1]


# 2. Ajouter un ami au troisième utilisateur.


new_friend  = { "id":3,"name":"John Doe"}
read_file["users"][2]["friends"].append(new_friend)


# 3. Mettre à jour le numéro de téléphone du quatrième utilisateur par “+1(954) 421-6824”.

for user in read_file['users'] :
    if user['index'] == 3:
        user['phone'] = '+1(954) 421-6824'



# 4. Ajouter une deuxième entreprise du nom de “SYLENT“ au premier utilisateur.
for user in read_file['users'] :
    if user['index'] == 0:
        user.update({"company": ["IMAGEFLOW","SYLENT"]})

# 5. Séparer pour chacun des utilisateurs le nom et le prénom, à l’aide des clefs suivantes
# firstName et lastName.
for user in read_file['users'] :
    name = user['name'].split(' ')
    del user['name']
    user['firstName'] = name[0]
    user['lastName'] = name[1]


# 6. Supprimer le tag “laborum“ du dernier utilisateur.
for user in read_file['users'] :
    if user['index'] == len(read_file['users'] ):
        user['tags'].remove('laborum')
    print(user['tags'])


# 7. Ajouter “+1“ à l’âge de tous les utilisateurs.
for user in read_file['users'] :
    print("avant modification : ")
    print(user['age'])
    user['age'] += 1
    print("apres modification : ")
    print(user['age'])