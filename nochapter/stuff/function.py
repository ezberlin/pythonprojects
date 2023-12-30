class quadratischeFunktion:
    """Klasse zum Umgang mit quadratischen Funktionen"""
    def __init__(self, name = "f", **informationen):
        self.name = name
        self.informationen = {"sp": None, "a": None, "b": None, "c": None, "d": None, "e": None}
        punkte = []
        for information in informationen:
            if information in self.informationen:
                self.informationen[information] = informationen[information]
            if isinstance(self.informationen[information], int):
                self.informationen[information] = float(self.informationen[information])
        if "p1" in informationen:
            punkte.append(informationen["p1"])
        if "p2" in informationen:
            punkte.append(informationen["p2"])
        if "p3" in informationen:
            punkte.append(informationen["p3"])
        
        if self.informationen["sp"] != None:
            self.informationen["d"] = -1 * self.informationen["sp"][0]
            self.informationen["e"] = self.informationen["sp"][1]
        if self.informationen["d"] != None and self.informationen["e"] != None and len(punkte) >= 1:
            self.informationen["a"] = (punkte[0][1] - self.informationen["e"]) / (punkte[0][0]**2 + 2 * self.informationen["d"] * punkte[0][0] + self.informationen["d"]**2)
        if self.informationen["a"] != None and self.informationen["d"] != None:
            self.informationen["b"] = 2 * self.informationen["a"] * self.informationen["d"]
            if self.informationen["e"] != None:
                self.informationen["c"] = self.informationen["a"] * self.informationen["d"]**2 + self.informationen["e"]
        if len(punkte) == 3:
            self.informationen["a"] = ((punkte[2][1]-punkte[1][1])/(punkte[2][0]-punkte[1][0])-(punkte[0][1]-punkte[1][1])/(punkte[0][0]-punkte[1][0]))/(punkte[2][0]-punkte[0][0])
            self.informationen["b"] = (punkte[2][1]-punkte[1][1])/(punkte[2][0]-punkte[1][0])-((punkte[2][0]+punkte[1][0])/(punkte[2][0]-punkte[0][0]))*((punkte[2][1]-punkte[1][1])/(punkte[2][0]-punkte[1][0])-(punkte[0][1]-punkte[1][1])/(punkte[0][0]-punkte[1][0]))
            self.informationen["c"] = punkte[0][1]+(punkte[1][1]*punkte[0][0]-punkte[0][1]*punkte[0][0])/(punkte[0][0]-punkte[1][0])+punkte[0][0]*punkte[1][0]*(punkte[2][1]*(punkte[0][0]-punkte[1][0])+punkte[1][1]*(punkte[2][0]-punkte[0][0])+punkte[0][1]*(punkte[1][0]-punkte[2][0]))/((punkte[0][0]-punkte[1][0])*(punkte[2][0]-punkte[1][0])*(punkte[2][0]-punkte[0][0]))
        
        if self.informationen["a"] != None and self.informationen["b"] != None:
            self.informationen["d"] = self.informationen["b"] / (2 * self.informationen["a"])
            if self.informationen["c"] != None:
                self.informationen["e"] = self.informationen["c"] - (self.informationen["b"]**2)/(4*self.informationen["a"])
        if self.informationen["d"] != None and self.informationen["e"] != None:
            self.informationen["sp"] = (-1 * self.informationen["d"], self.informationen["e"])
    def __str__(self):
        parameter = []
        parameter.append(self.informationen["a"])
        parameter.append(self.informationen["b"])
        parameter.append(self.informationen["c"])
        for p in range(0, 3):
            if parameter[p].is_integer():
                parameter[p] = int(parameter[p])
            parameter[p] = str(parameter[p])
            if float(parameter[p]) > 0 and p != 0:
                parameter[p] = "+" + parameter[p]
        return f"{self.name}(x)={parameter[0]}x²{parameter[1]}x{parameter[2]}"
    def scheitelpunkt(self):
        sp = list(self.informationen["sp"])
        for p in range(0, 2):
            if sp[p].is_integer():
                sp[p] = int(sp[p])
        return f"({sp[0]}|{sp[1]})"
 
f = quadratischeFunktion(sp=(5,0), a=1)#mögliche parameter sind p1, p2, p3 und sp als tupel (punkte/scheitelpunkt) sowie a, b, c, d und e als int/float (parameter)
print(f)
print(f.scheitelpunkt())
