import json
import random #penerus dari ARPANET,lebih praktis
#kode
e = {
    "code" : 1000,
    "status" : False
}
d = {
    "device1" : "name",
    "device2" : "name",
    "device3" : "name"
}
a = {
    "name" : "name",
    "password" : "password",
    "GateAwayFile" : ""
}
def setMode(name, password):
    a["name"] = name
    a["password"] = password
    with open("ModeSetting.json", "w") as f:
        json.dump(a, f)
    with open("Devices.json", "w") as file:
        json.dump(d, file)
def gateaway(FileGateaway):
    if ".json" in FileGateaway:
        with open(FileGateaway, "r") as f:
            b = json.load(f) #ini untuk set gate away untuk data
    elif ".txt" in FileGateaway:
        with open(FileGateaway, "r") as f:
                b = f.read() #txt untuk hal not rumit kekbicara antar file
    a["GateAwayFile"] = FileGateaway
    with open("ModeSetting.json", "w") as f:
        json.dump(a, f)
#klo di atas udah,tinggal yg bawah
def connect(nameWifi, password, NameDevices):
    with open("Devices.json", "r") as f:
        D = json.load(f)
    if D["device1"] != "name":
        if D["device2"] != "name":
            if D["device3"] != "name":
                print("CONNECTIONS FULL!")
            else:
                D["device3"] = NameDevices
                with open("Devices.json","w") as f:
                    json.dump(D, f)
        else:
            D["device2"] = NameDevices
            with open("Devices.json", "w") as f:
                json.dump(D, f)
    else:
        D["device1"] = NameDevices
        with open("Devices.json", "w") as f:
            json.dump(D, f)
def pair(name, device, targetpair): #ini berarti memasangkan 1 file ke file lain untuk ambil data,tanpa ini,kita hanya menerima data dari gateaway
    with open("ModeSetting.json", "r") as f, open("Devices.json", "r") as file:
        a = json.load(f)
        b = json.load(file)
    #bagian periksa
    if name == a["name"]:
        print("pairing in progress")
        #PROSES dibalik layar yang MALAS
        if device == b["device1"] or device == b["device2"] or device == b["device3"]:
            if targetpair == b["device1"] or targetpair == b["device2"] or targetpair == b["device3"]:
                print("pair progress = 25%")#ini loading
                e["status"] = True
                e["code"] = random.randint(1001, 9999)
                with open("status.json", "w") as f:
                    json.dump(e, f) #untuk simpen
                return f'success!please run command runPair {e["code"]}'
def runpair(code, data):
    with open("status.json", "r") as f:
        pairprog = json.load(f)
    if code == pairprog["code"]:
        with open("data.txt", "w") as file:
            file.write(data)
def readData(code):
    with open("data.txt", "r") as f:
        data = f.read()
    return data
def runGate():
    with open("ModeSetting.json", "r") as f:
        data = json.load(f)
    if ".txt" in data["GateAwayFile"]:
        with open(data["GateAwayFile"], "r") as file:
            dataS = file.read()
        return dataS
    elif ".json" in data["GateAwayFile"]:
         #MENGIRIM DATA
        with open(data["GateAwayFile"], "r") as file:
            dataS = json.load(file)
        return dataS
    else:
        return "UNKNOWN FORMAT"
