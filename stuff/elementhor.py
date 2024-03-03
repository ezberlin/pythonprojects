print("Willkommen bei Elementhor, dem Tool für Angeber, die Wörter in Elemente verschlüsseln wollen!")
w = input("Gib dein Wort ein: ") #worteingabe
w = w.lower()
e = ["h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca", "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "y", "zr", "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "i", "xe", "cs", "ba", "la", "ce", "pr", "nd", "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg", "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl", "mc", "lv", "ts", "og"]
#elemente
c = 0 #counter
m = [] #marker
o = [] #output
while c+1 < len(w):
    try:
        if w[c] + w[c+1] in e:
            if w[c] in e:
                m.append(len(o))
            o.append(w[c] + w[c+1])
            c = c + 2
        elif w[c] in e:
            o.append(w[c])
            c = c + 1
        elif len(m) > 0:
            while len(o) < m[-1]:
                
            
                
                
                
    except IndexError:
        print("Index Error")
            
        
        