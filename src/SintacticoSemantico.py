# coding=utf-8
def semantico(lista):
    palabras = sintactico(lista)

    t = pronombre(palabras)
    r = pregunta(palabras[0])
    palabras[0] = palabras[0][0].upper()+palabras[0][1:]
    
    v = posVerb(palabras)
    if(palabras != ""):
        if(r[0]):
            palabras[0] = "¿"+palabras[0]
            if(t[0]):
                palabras[v] = fixVerb(t[1],palabras)
            else:
                palabras[1] = fixVerb("usted", palabras)
            palabras[len(palabras)-1] = palabras[len(palabras)-1]+"?"
            print str(palabras)
            return palabras
        elif(t[0]):
            if(t[0]):
                if(palabras[t[2]+1]!=""):
                    palabras[t[2]] = t[1]
                    palabras[v] = fixVerb(t[1], palabras)
                else:
                    print("no hay verbo")
                print str(palabras)
                return palabras
        else:
            print str(palabras)
            return palabras


def posVerb(palabras):
    verb = ["ser","estar","ir","venir","tener","hacer","decir","comer", "llamar", "cumplir", ""]
    n = -1
    for x in range(0,len(palabras)):
        for y in verb:
            if(palabras[x]==y):
                n = x
    return n
    

def pronombre(palabras):
    exc = ["yo", "usted", "ustedes", "nosotros", "ellos","él", "ella"]
    x = False
    y = ""
    n = 0
    for e in exc:
        for w in range(len(palabras)):
            if(e == palabras[w]):
                if(palabras[w+1]=="nombre"):
                    if(e=="yo"):
                        e = "mi"
                    elif(e=="usted"):
                        e = "su"
                    else:
                        e = "sus"
                x = True
                y = e
                n = w
                print(y)
    return [x,y,n]

def pregunta(palabra):
    preg = ["donde","cual","que","como","cuando","porque"]
    t = False
    w = ""
    for x in preg:
        if(x == palabra):
            t = True
            w = x
            print(x)
    return [t,w]

def fixVerb(pron, palabras):
    verb = ["ser","estar","ir","venir","tener","hacer","decir","llamar","cumplir", ""]
    conjY = ["soy", "estoy", "voy","vengo","tengo", "hago", "digo","llamo","cumplo"]
    conjEEU = ["es", "está", "va","viene","tiene", "hace", "dice","llama", "cumple"]
    conUs = ["son", "están", "van","vienen", "tienen", "hacen", "dicen","llaman", "cumplen"]
    conN = ["somos","estamos", "vamos","venimos", "tenemos", "hacemos", "decimos","llamamos", "cumplimos"]
    w = ""
    for x in palabras:
        for y in range(0,len(verb)):
            if(x == verb[y]):
                if(pron == "él" or pron == "ella" or pron == "usted" or pron == "mi" or pron == "su"):
                    w = conjEEU[y]
                elif(pron == "yo"):
                    w = conjY[y]
                elif(pron == "ustedes" or pron == "sus"):
                    w = conUs[y]
                else:
                    w = conN[y]
    return w

def sintactico(palabras):
    n = 0
    res = []
    for x in range(0,len(palabras)):
        w = ""
        if(palabras[x] == " "):
            for y in range(n,x):
                if(palabras[y]=="10" and palabras[y+1]!=" "):
                    s = int(10)+int(palabras[y+1])
                    k = str(s)
                    w += k
                elif(palabras[y-1]=="10"):
                    "suma"
                else:
                    if(palabras[y]!=w or w.isdigit()):
                        w += palabras[y]
            n = x +1
            res += [w]
            w = ""
    return res
