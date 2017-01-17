
patron_busqueda = "AF#GiI!b6Kf9Lr/Ns;OyP QxR*3+WZaT=cYde_D0Egh:Vj.HklmXnSñCopqtJvwz1-2M45Ñ78B";
patron_encripta = "cD5i:E7F*JmL_ÑOPQ+S10TX.3Y=!Z4abG dKfgh8jkl#nN;Hño/pVW-qrAsMtCvIwRxyz2B6e9";


def EncriptarCadena(cadena):
    result=""
    for idx  in range (0,len(cadena)):
        result += EncriptarCaracter(cadena[idx:idx+1],len(cadena),idx)
    return result


def EncriptarCaracter(caracter, variable, a_indice):
    #if (patron_busqueda.index(caracter) != -1):
    try:
        indice = (patron_busqueda.index(caracter)+variable+a_indice)%(len(patron_busqueda))
        return patron_encripta[indice:indice+1]
    except:
        return caracter

def DesEncriptarCadena(cadena):
    result =""
    for idx in range(0, len(cadena)):
        result += DesEncriptarCaracter(cadena[idx:idx+1],len(cadena),idx)
    return result

def DesEncriptarCaracter (caracter, variable, a_indice):
    try:
        if(patron_encripta.index(caracter)-variable-a_indice > 0):
            indice = (patron_encripta.index(caracter) - variable - a_indice)% len(patron_encripta)
        else:
            indice = len(patron_busqueda)+ ((patron_encripta.index(caracter) - variable - a_indice)% len(patron_encripta))

        indice = indice%len(patron_encripta)
        return patron_busqueda[indice:indice+1]
    except:
        return caracter
