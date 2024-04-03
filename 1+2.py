import re

def estIPv4Valide(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return bool(pattern.match(ip))

def getNbSTA_cidr(cidr):
    return 2**(32 - cidr) - 2

def estMasqueValide(mask):
    parts = mask.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    binary_mask = ''.join([bin(int(x)).count('1') for x in parts])
    return binary_mask.count('1') == 32

def masque2cidr(mask):
    binary_mask = ''.join([bin(int(x)).count('1') for x in mask.split('.')])
    return binary_mask.count('1')

def cidr2masque(cidr):
    binary_mask = '1' * cidr + '0' * (32 - cidr)
    return '.'.join([str(int(binary_mask[i:i+8], 2)) for i in range(0, 32, 8)])

# Tests
print(estIPv4Valide("192.168.1.1"))
print(estIPv4Valide("256.0.0.1"))

print(getNbSTA_cidr(24))

print(estMasqueValide("255.255.255.0"))
print(estMasqueValide("255.255.255.128"))
print(estMasqueValide("255.255.255.255"))

print(masque2cidr("255.255.255.0"))

print(cidr2masque(24))

"""Fonction estIPv4Valide() :

Entrée attendue : Une chaîne de caractères représentant une adresse IPv4.
Sortie attendue : Un booléen indiquant si l'adresse IPv4 est valide ou non.
Fonction getNbSTA_cidr() :

Entrée attendue : Une valeur CIDR.
Sortie attendue : Le nombre d'hôtes potentiels dans le sous-réseau logique correspondant au CIDR.
Fonction estMasqueValide() :

Entrée attendue : Une chaîne de caractères représentant un masque de sous-réseau.
Sortie attendue : Un booléen indiquant si le masque de sous-réseau est valide ou non.
Fonction masque2cidr() :

Entrée attendue : Une chaîne de caractères représentant un masque de sous-réseau.
Sortie attendue : Une valeur CIDR correspondant au masque de sous-réseau fourni.
Fonction cidr2masque() :

Entrée attendue : Une valeur CIDR.
Sortie attendue : Une chaîne de caractères représentant le masque de sous-réseau correspondant au CIDR fourni."""




