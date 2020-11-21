# import
import argparse
import unicodedata

# parser definition
parser = argparse.ArgumentParser(description='Genere une liste de login depuis un prenom et un nom')
# parser arg1
parser.add_argument('arg1', metavar='prenom', type=str,
                    help='Prenom')
# parser arg2
parser.add_argument('arg2', metavar='nom', type=str,
                    help='Nom de famille')
# parser
args = parser.parse_args()

# vars
name = [args.arg1, args.arg2]


def cleanArgv(listAgrv):
    listNom = []
    for nom in listAgrv:
        s = unicodedata.normalize('NFD', nom).encode('ascii', 'ignore')
        s = s.lower()
        listNom.append(s.decode("utf-8"))
    return listNom

def lettreFromNom(nom):
    listNom = []
    reverse = nom[::-1]
    for i in range(len(nom)):
        listNom.append(nom[0:i+1])
        listNom.append(reverse[0:i+1])
    return listNom

def mixNom(litPrenom, listNom):
    listDefinitive = []
    for prenom in litPrenom:
        for nom in listNom:
            listDefinitive.append(prenom + "." + nom)
            listDefinitive.append(prenom + "-" + nom)
            listDefinitive.append(prenom + "_" + nom)
            listDefinitive.append(prenom + nom)
            listDefinitive.append(nom + "." + prenom)
            listDefinitive.append(nom + "-" + prenom)
            listDefinitive.append(nom + "_" + prenom)
            listDefinitive.append(nom + prenom)
    return listDefinitive

if __name__ == '__main__':
    prenom, nom = cleanArgv(name)

    initPrenom = lettreFromNom(prenom)
    initNom = lettreFromNom(nom)

    toFile = mixNom(initPrenom, initNom)

    with open("./login.txt", 'w') as f:
        for login in toFile:
            f.write("{}\n".format(login))