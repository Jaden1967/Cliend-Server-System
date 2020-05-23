import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),9999))

def checkName(infoName):
    flag = False
    if (len(infoName) != 0):
        if (bool(infoName.isspace()) is False):
            flag = True
    return flag

def checkAge(infoAge):
    if (len(infoAge) != 0):
        if (bool(infoAge.isspace()) is False):
            return infoAge.isdigit()
    else:
        return True



while True:
    numberSelection = \
        input("Python DB Menu \n"
              " 1. Find customer\n"
              " 2. Add customer\n"
              " 3. Delete customer\n"
              " 4. Update customer age\n"
              " 5. Update customer address\n"
              " 6. Update customer phone\n"
              " 7. Print report\n"
              " 8. Exit\n"
              "Select")

    if numberSelection == "1":
        missionType = "find"
        s.send(bytes(str(missionType),"utf-8"))
        print("Please Enter A Customer Name:")
        customerName = input()
        s.send(bytes(customerName,"utf-8"))
        customerInfo = s.recv(1024)
        print(customerInfo.decode("utf-8"))

    elif numberSelection == "2":
         print("Please Enter Customer Information:")
         customerInfo = ""
         infoName = input("Name")
         if(checkName(infoName)):
            customerInfo = customerInfo + infoName + "|"
         else:
            print("Name cannot be blank!")
            continue
         infoAge = input("Age")
         if (checkAge(infoAge)):
            customerInfo = customerInfo + infoAge + "|"
         else:
            print("Age should be an integer")
            continue
         infoAddress = input("Address")
         customerInfo = customerInfo + infoAddress + "|"
         infoNumber = input("Phone Number")
         customerInfo = customerInfo + infoNumber
         missionType = "add"
         s.send(bytes(str(missionType), "utf-8"))
         # print(customerInfo)
         s.send(bytes(customerInfo, "utf-8"))
         ifSucess = s.recv(1024)
         print(ifSucess.decode("utf-8"))

    elif numberSelection == "3":
        missionType = "delete"
        s.send(bytes(str(missionType), "utf-8"))
        print("Please Enter A Customer Name:")
        customerName = input()
        s.send(bytes(customerName, "utf-8"))
        ifSuccessMessage = s.recv(1024)
        print(ifSuccessMessage.decode("utf-8"))

    elif numberSelection == "4":
        missionType = "find"
        s.send(bytes(str(missionType), "utf-8"))
        print("Please Enter A Customer Name:")
        customerName = input()
        s.send(bytes(customerName, "utf-8"))
        customerInfo = s.recv(1024).decode("utf-8")
        print(customerInfo)
        if (customerInfo == "Customer not found!"):
            continue
        else:
            newAge = input("Please Enter an Age information")
            if (checkAge(newAge)):
                customerInfo = customerName+ "|" + newAge
                missionType = "updateAge"
                s.send(bytes(str(missionType), "utf-8"))
                s.send(bytes(customerInfo, "utf-8"))
                print(s.recv(1024).decode("utf-8"))
            else:
                print("Age should be an integer")
                continue

    elif numberSelection == "5":
        missionType = "find"
        s.send(bytes(str(missionType), "utf-8"))
        print("Please Enter A Customer Name:")
        customerName = input()
        s.send(bytes(customerName, "utf-8"))
        customerInfo = s.recv(1024).decode("uft-8")
        print(customerInfo)
        if(customerInfo == "Customer not found!"):
            continue
        else:
            newAddress = input("Please Enter an Address information")
            customerInfo = customerName+ "|" + newAddress
            missionType = "updateAddress"
            s.send(bytes(str(missionType), "utf-8"))
            s.send(bytes(customerInfo, "utf-8"))
            print(s.recv(1024).decode("utf-8"))

    elif numberSelection == "6":
        missionType = "find"
        s.send(bytes(str(missionType), "utf-8"))
        print("Please Enter A Customer Name:")
        customerName = input()
        s.send(bytes(customerName, "utf-8"))
        customerInfo = s.recv(1024).decode("utf-8")
        print(customerInfo)
        if (customerInfo == "Customer not found!"):
            continue
        else:
            newNumber = input("Please Enter an phone number information")
            customerInfo = customerName + "|" + newNumber
            missionType = "updateNumber"
            s.send(bytes(str(missionType), "utf-8"))
            s.send(bytes(customerInfo, "utf-8"))
            print(s.recv(1024).decode("utf-8"))

    elif numberSelection == "7":
        missionType = "report"
        sendMessage = "printReport"
        s.send(bytes(str(missionType), "utf-8"))
        s.send(bytes(sendMessage, "utf-8"))
        print(s.recv(1024).decode("utf-8"))

    elif numberSelection == "8":
        print("GOODBYE")
        break
    else:
        print("invalid input,please try again")

s.close()