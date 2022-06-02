
#& Mapa de Memoria
class limites():
    def __init__(self,limiteInferior,limiteSuperior) -> None:
        self.li = 1 + limiteInferior
        self.ls = limiteSuperior
        self.cont = 0

#* cuantos valores hay por rango
total = 10
#~ Globales
rangoInt = limites(0,total) #*10
rangoFloat = limites(rangoInt.ls, rangoInt.ls + total) #*20
rangoBool = limites(rangoFloat.ls, rangoFloat.ls+ total)#*30
rangoStirng = limites(rangoBool.ls, rangoBool.ls+ total)#*40

desfase = rangoStirng.ls #*40
#~ Temporales
rangoTempInt = limites(0 + desfase ,total + desfase) #*50
rangoTempFloat = limites(rangoInt.ls + desfase, rangoInt.ls + total + desfase) #*60
rangoTempBool = limites(rangoFloat.ls + desfase, rangoFloat.ls + total+ desfase)#*70
rangoTempStirng = limites(rangoBool.ls + desfase, rangoBool.ls + total + desfase)#*80
#~ Locales
rangoLocalInt = limites(0 + desfase*2  ,total + desfase*2)#*90
rangoLocalFloat = limites(rangoTempInt.ls + desfase, rangoTempInt.ls + total + desfase)#*100
rangoLocalBool = limites(rangoTempFloat.ls + desfase, rangoTempFloat.ls + total+ desfase)#*110
rangoLocalStirng = limites(rangoTempBool.ls + desfase, rangoTempBool.ls + total + desfase)#*120

#~ Constantes
rangoConstInt = limites(0 + desfase*3  ,total + desfase*3)#*130
rangoConstFloat = limites(rangoLocalInt.ls + desfase, rangoLocalInt.ls + total + desfase)#*140
rangoConstBool = limites(rangoLocalFloat.ls + desfase, rangoLocalFloat.ls + total+ desfase)#*150
rangoConstStirng = limites(rangoLocalBool.ls + desfase, rangoLocalBool.ls + total + desfase)#*160

#~ Pointers
rangoPointerInt = limites(0 + desfase*4, total + desfase*4) #*161 - 170
rangoPointerFloat = limites(rangoConstInt.ls + desfase, rangoConstInt.ls + total + desfase)
rangoPointerBool = limites(rangoConstFloat.ls + desfase, rangoConstFloat.ls + total + desfase)
rangoPointerString = limites(rangoConstBool.ls + desfase, rangoConstBool.ls + total + desfase)

#& Memoria
mainMemory = [ None for _ in range(rangoPointerString.ls)]
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

def apartarMemoriaPointer(tipo):
    miRango = None
    if tipo == 'int':
        miRango = rangoPointerInt
    elif tipo == 'float':
        miRango = rangoPointerFloat
    elif tipo == 'bool':
        miRango = rangoPointerBool
    elif tipo == 'String':
        miRango = rangoPointerString
    indice = miRango.li + miRango.cont
    miRango.cont += 1 
    checkCounter(miRango)
    mainMemory[indice] = -1
    return indice

#^ Siempre es de los locales
def clearMemory(tipo, direccion):
    miRango = None
    if tipo == 'int':
        miRango = rangoLocalInt
    elif tipo == 'float':
        miRango = rangoLocalFloat
    elif tipo == 'bool':
        miRango = rangoLocalBool
    elif tipo == 'String':
        miRango = rangoLocalStirng
    miRango.cont -= 1 
    mainMemory[direccion] = None
    