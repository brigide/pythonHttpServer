import json


def readAllContactsFromFile():   
    with open("data/contacts.json", "r") as file:
        data = json.load(file)
        
        return data


def readSingleContactFromFile(desiredName):   
    with open("data/contacts.json", "r") as file:
        data = json.load(file)
        
        desiredPerson = None
        for person in data:
            if person['name'] == desiredName:
                desiredPerson = person
                break

        return person


def saveContactToFile(contact): 
    with open("data/contacts.json", "r") as file:
        data = json.load(file)
        data.append(contact)

    with open("data/contacts.json", "w") as file:
        dataString = json.dumps(data, indent = 4) 
        file.write(dataString)


def updateContactFromFile(contactPhone, newData): 
    with open("data/contacts.json", "r") as file:
        data = json.load(file)
    
    lenght = len(data)
    for i in range(lenght):
        if data[i]['phone'] == contactPhone:
            data[i] = newData

    with open("data/contacts.json", "w") as file:
        dataString = json.dumps(data, indent = 4) 
        file.write(dataString)


def deleteContactFromFile(contactPhone): 
    with open("data/contacts.json", "r") as file:
        data = json.load(file)
    
    lenght = len(data)
    for i in range(lenght):

        if data[i]['phone'] == contactPhone:
            data.pop(i)

    with open("data/contacts.json", "w") as file:
        dataString = json.dumps(data, indent = 4) 
        file.write(dataString)
