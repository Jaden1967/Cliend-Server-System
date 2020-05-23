import socket

# lord database
# As a dictionary in memory, Name is key combine with (age, address, phone number) as value
file = open('data.txt', 'r')
Lines = file.readlines()
Dic = {}
for item in Lines:
    temp = item.split('|')
    if(len(temp[0]) != 0):
        if(bool(temp[0].isspace()) is False):
            Dic[temp[0]] = temp[1], temp[2], temp[3]


# build the connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen()



def mission(missionType,reciveMessage):
    errorMessage = ""
    if missionType == "find":
        errorMessage = "Customer not found!"
        customerInfo = Dic.get(reciveMessage,errorMessage)
        return customerInfo

    elif missionType == "add":
        ifSucessMessage = ""
        temp = reciveMessage.split('|')
        if temp[0] in Dic:
            ifSucessMessage = "Customer already exists!"
        else:
            Dic[temp[0]] = temp[1], temp[2], temp[3]
            ifSucessMessage = "The customer has been added!"
        return ifSucessMessage

    elif missionType == "delete":
        ifSucessMessage = ""
        if reciveMessage in Dic:
            Dic.pop(reciveMessage)
            ifSucessMessage = "The customer has been deleted!"
        else:
            ifSucessMessage = "Customer does not exist!"
        return ifSucessMessage

    elif missionType == "updateAge":
        nameAge = reciveMessage.split('|')
        temp = Dic.get(nameAge[0])
        Dic[nameAge[0]]= nameAge[1],temp[1],temp[2]
        return "Age update is successful!"
    elif missionType == "updateAddress":
        nameAddress = reciveMessage.split('|')
        temp = Dic.get(nameAddress[0])
        Dic[nameAddress[0]]= temp[0],nameAddress[1],temp[2]
        return "Address update is successful!"
    elif missionType == "updateNumber":
        nameNumber = reciveMessage.split('|')
        temp = Dic.get(nameNumber[0])
        Dic[nameNumber[0]]= temp[0],temp[1],nameNumber[1]
        return "Number update is successful!"
    elif missionType == "report":
        returnMessage = ""
        for name in sorted(Dic.keys()):
            returnMessage = returnMessage + str(name) + str(Dic[name]) + "\n"
        return returnMessage
    else:
        return "terminate"

while True:
    clientsocket, address = s.accept()
    print(f"Connection from{address} has been established")
    # clientsocket.send(bytes("Welcome to the server!","utf-8"))
    missionType = clientsocket.recv(1024).decode("utf-8")
    print(missionType)
    reciveMessage = clientsocket.recv(1024).decode("utf-8")
    print(reciveMessage)
    returnMessage = mission(missionType, reciveMessage)
    print(returnMessage)
    if (returnMessage=="terminate"):
        break
    clientsocket.send(bytes(str(returnMessage), "utf-8"))


