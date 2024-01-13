class variable:
    def __init__(self, numrange="R", upper=None, lower=None):
        self.numrange = numrange
        self.upper = upper
        self.lower = lower
        
class term:
    def __init__(self, term):
        self.term = term
    def simplify(self):
        new_term = []
        skip_iterating = []
        for count, nom in enumerate(self.term):
            if count in skip_iterating:
                continue
            for count2, nom2 in enumerate([self.term[count+1:-1] + self.term[-1]]):
                if nom[1:-1]+[nom[-1]] == nom2[1:-1]+[nom2[-1]]:
                    print(nom[0], nom2[0])
                    new_nom = [nom[0] + nom2[0]] + nom[1:-1]+ [nom[-1]]
                    new_term.append(new_nom)
                    skip_iterating.append(count)
                    skip_iterating.append(count2)
            if count in skip_iterating:
                continue
            new_term.append(nom)
        self.term = new_term
                            
                            
                            

            
x = variable()
y = variable()
term1 = term([[2,x], [3,x], [5,y], [6]])
term1.simplify()
print(term1.term)