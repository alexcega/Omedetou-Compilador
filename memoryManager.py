
#& Mapa de Memoria
class limites():
    def __init__(self,limiteInferior,limiteSuperior) -> None:
        self.li = 1 + limiteInferior
        self.ls = limiteSuperior
        self.cont = 0

#* cuantos valores hay por rango
total = 10
#~ Globales
rangoInt = limites(0,total)
rangoFloat = limites(rangoInt.ls, rangoInt.ls + total)
rangoBool = limites(rangoFloat.ls, rangoFloat.ls+ total)
rangoStirng = limites(rangoBool.ls, rangoBool.ls+ total)

# print(rangoInt.li, rangoStirng.ls)
desfase = rangoStirng.ls
#~ Temporales
rangoTempInt = limites(0 + desfase ,total + desfase)
rangoTempFloat = limites(rangoInt.ls + desfase, rangoInt.ls + total + desfase)
rangoTempBool = limites(rangoFloat.ls + desfase, rangoFloat.ls + total+ desfase)
rangoTempStirng = limites(rangoBool.ls + desfase, rangoBool.ls + total + desfase)

# print(rangoTempInt.li, rangoTempStirng.ls)
#~ Locales
rangoLocalInt = limites(0 + desfase*2  ,total + desfase)
rangoLocalFloat = limites(rangoTempInt.ls + desfase, rangoTempInt.ls + total + desfase)
rangoLocalBool = limites(rangoTempFloat.ls + desfase, rangoTempFloat.ls + total+ desfase)
rangoLocalStirng = limites(rangoTempBool.ls + desfase, rangoTempBool.ls + total + desfase)
# print(rangoLocalInt.li, rangoLocalStirng.ls)

#~ Constantes
rangoConstInt = limites(0 + desfase*3  ,total + desfase)
rangoConstFloat = limites(rangoLocalInt.ls + desfase, rangoLocalInt.ls + total + desfase)
rangoConstBool = limites(rangoLocalFloat.ls + desfase, rangoLocalFloat.ls + total+ desfase)
rangoConstStirng = limites(rangoLocalBool.ls + desfase, rangoLocalBool.ls + total + desfase)
# print(rangoConstInt.li, rangoConstStirng.ls)


#& Memoria
mainMemory = [ None for _ in range(rangoConstStirng.ls)]
# print(len(mainMemory))

def apartarMemoria(tipo ):
    miRango = None
    if tipo == 'int':
        miRango = rangoInt
    elif tipo == 'float':
        miRango = rangoFloat
    elif tipo == 'bool':
        miRango = rangoBool
    elif tipo == 'String':
        miRango = rangoStirng
    indice = miRango.li + miRango.cont
    miRango.cont += 1 
    checkCounter(miRango)
    mainMemory[indice] = -1
    return indice

def checkCounter(obj):
    if obj.cont > obj.ls :
        print('Error, memory limit exceeded')
        exit()

def apartarMemoriaTemporal(tipo):
    miRango = None
    if tipo == 'int':
        miRango = rangoTempInt
    elif tipo == 'float':
        miRango = rangoTempFloat
    elif tipo == 'bool':
        miRango = rangoTempBool
    elif tipo == 'String':
        miRango = rangoTempStirng
    indice = miRango.li + miRango.cont
    miRango.cont += 1 
    checkCounter(miRango)
    mainMemory[indice] = -1
    return indice

def apartarMemoriaLocal(tipo):
    miRango = None
    if tipo == 'int':
        miRango = rangoLocalInt
    elif tipo == 'float':
        miRango = rangoLocalFloat
    elif tipo == 'bool':
        miRango = rangoLocalBool
    elif tipo == 'String':
        miRango = rangoLocalStirng
    indice = miRango.li + miRango.cont
    miRango.cont += 1 
    checkCounter(miRango)
    mainMemory[indice] = -1
    return indice

def apartarMemoriaConst(tipo):
    miRango = None
    if tipo == 'int':
        miRango = rangoConstInt
    elif tipo == 'float':
        miRango = rangoConstFloat
    elif tipo == 'bool':
        miRango = rangoConstBool
    elif tipo == 'String':
        miRango = rangoConstStirng
    indice = miRango.li + miRango.cont
    miRango.cont += 1 
    checkCounter(miRango)
    mainMemory[indice] = -1
    return indice