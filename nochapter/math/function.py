class quadratischeFunktion:
    """Klasse zur Erstellung, zum Umgang und zur Formulierung quadratischer Funktionen"""
    def __init__(self, name = "f", **inputs):
        """Vervollständigt aus gegebenen Informationen die restlichen"""
        self.name = name
        self.informationen = {"sp": None, "a": None, "b": None, "c": None, "d": None, "e": None}
        #Trägt gegebene Informationen in das Dictionary ein
        punkte = []
        #Füllt Parameter ein
        for information in inputs:
            if information in self.informationen:
                self.informationen[information] = inputs[information]
                if isinstance(self.informationen[information], int):
                    self.informationen[information] = float(self.informationen[information])
        #Füllt Punkte ein
        if "p1" in inputs:
            punkte.append(inputs["p1"])
        if "p2" in inputs:
            punkte.append(inputs["p2"])
        if "p3" in inputs:
            punkte.append(inputs["p3"])
        if "sp" in inputs:
            punkte.append(inputs["sp"])
        #Füllt Werte zur allgemeinen Form au
        if self.informationen["sp"] != None:
            self.informationen["d"] = self.informationen["sp"][0]
            self.informationen["e"] = self.informationen["sp"][1]
        if self.informationen["d"] != None and self.informationen["e"] != None and len(punkte) >= 1 and self.informationen["a"] == None:
            self.informationen["a"] = (punkte[0][1] - self.informationen["e"]) / (punkte[0][0]**2 + -2 * self.informationen["d"] * punkte[0][0] + self.informationen["d"]**2)
        if self.informationen["a"] != None and self.informationen["d"] != None:
            self.informationen["b"] = 2 * self.informationen["a"] * -1 * self.informationen["d"]
            if self.informationen["e"] != None:
                self.informationen["c"] = self.informationen["a"] * self.informationen["d"]**2 + self.informationen["e"]
        if len(punkte) == 3:
            #Dankeschön Dima für die allgemeinen Lösungen der Gleichungssysteme. Dein Leiden wird niemals vergessen.
            self.informationen["a"] = ((punkte[2][1]-punkte[1][1])/(punkte[2][0]-punkte[1][0])-(punkte[0][1]-punkte[1][1])/(punkte[0][0]-punkte[1][0]))/(punkte[2][0]-punkte[0][0])
            self.informationen["b"] = (punkte[2][1]-punkte[1][1])/(punkte[2][0]-punkte[1][0])-((punkte[2][0]+punkte[1][0])/(punkte[2][0]-punkte[0][0]))*((punkte[2][1]-punkte[1][1])/(punkte[2][0]-punkte[1][0])-(punkte[0][1]-punkte[1][1])/(punkte[0][0]-punkte[1][0]))
            self.informationen["c"] = punkte[0][1]+(punkte[1][1]*punkte[0][0]-punkte[0][1]*punkte[0][0])/(punkte[0][0]-punkte[1][0])+punkte[0][0]*punkte[1][0]*(punkte[2][1]*(punkte[0][0]-punkte[1][0])+punkte[1][1]*(punkte[2][0]-punkte[0][0])+punkte[0][1]*(punkte[1][0]-punkte[2][0]))/((punkte[0][0]-punkte[1][0])*(punkte[2][0]-punkte[1][0])*(punkte[2][0]-punkte[0][0]))
        #Füllt von der allgemeinen Form aus alle anderen Werte
        if self.informationen["a"] != None and self.informationen["b"] != None:
            try:
                self.informationen["d"] = -1 * self.informationen["b"] / (2 * self.informationen["a"])
                if self.informationen["c"] != None:
                    self.informationen["e"] = self.informationen["c"] - (self.informationen["b"]**2)/(4*self.informationen["a"])
            except ZeroDivisionError:
                pass
        if self.informationen["d"] != None and self.informationen["e"] != None:
            self.informationen["sp"] = (self.informationen["d"], self.informationen["e"])
    def __str__(self):
        """Formatiert und gibt die allgemeine Form der quadratischen Funktion ax²+bx+c aus"""
        try:
            parameter = []
            parameter.append(self.informationen["a"])#sammelt parameter
            parameter.append(self.informationen["b"])
            parameter.append(self.informationen["c"])
            for p in range(0, 3):
                parameter[p] = round(parameter[p], 3)#rundet parameter auf 3 nachkommastellen
                if parameter[p].is_integer():
                    parameter[p] = int(parameter[p])#formatiert parameter wenn möglich in zahl um
                parameter[p] = str(parameter[p])
                if float(parameter[p]) >= 0 and p != 0:
                    parameter[p] = "+" + parameter[p]#fügt zur formatierung ein + vor nichtnegative Zahlen ein
            return f"{self.name}(x)={parameter[0]}x²{parameter[1]}x{parameter[2]}"
        except TypeError:
            return "None"
    def scheitelpunkt(self):
        """Formatiert und gibt den Scheitelpunkt der quadratischen Funktion aus"""
        try:
            sp = list(self.informationen["sp"])
            for p in range(0, 2):
                sp[p] = round(sp[p], 3)
                if sp[p].is_integer():
                    sp[p] = int(sp[p])
            return f"S({sp[0]}|{sp[1]})"
        except TypeError:#falls es keinen scheitelpunkt gibt (z.b. lineare funktion), gibt er dir keinen scheitelpunkt aus
            pass
    def scheitelpunktform(self):
        """Formatiert und gibt die Scheitelpunktform  der quadratischen Funktion a(x-d)²+e aus"""
        try:
            parameter = []
            parameter.append(self.informationen["a"])
            parameter.append(self.informationen["d"])
            parameter.append(self.informationen["e"])
            parameter[1] *= -1
            for p in range(0, 3):
                parameter[p] = round(parameter[p], 3)
                if parameter[p].is_integer():
                    parameter[p] = int(parameter[p])
                parameter[p] = str(parameter[p])
                if float(parameter[p]) >= 0 and p != 0:
                    parameter[p] = "+" + parameter[p]
            return f"{self.name}(x)={parameter[0]}(x{parameter[1]})²{parameter[2]}"
        except TypeError:
            pass

#beispiel
f = quadratischeFunktion(sp=(),a=1)#mögliche parameter sind p1, p2, p3 und sp als tupel (punkte/scheitelpunkt) sowie a, b, c, d und e als int/float (parameter)
print("Die allgemeine Funktionsgleichung ist",f)
print("Der Scheitelpunkt ist",f.scheitelpunkt())
print("Die Scheitelpunktform ist", f.scheitelpunktform())
