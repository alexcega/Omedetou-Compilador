# Omedetou-Compilador
Proyecto de compilador para la materia de Compiladores enero - junio 2022
Se hace uso de la libreria Lark para la gramatica tokens parser y lexer
Hacemos uso de un _Visitor_ como parte de la libreria para recorrer nuestro árbol 
para inicial instala la libreria con el comando:

`pip install lark`

Para ejecutar el programa usar:

`python omedetouLark.py`

*Recomendado visualizar codigo con la extension [colorful comments](https://marketplace.visualstudio.com/items?itemName=ParthR2031.colorful-comments)*

Si lo desea puede cambiar el input a parsear por uno de los contenidos en [/Tests](Tests)

Compilador en base a programacion orientada a objetos con soporte de acceso a sus funciones y atributos

Equipo:
* [Alejandro Cedillo](https://github.com/alexcega) A00824742
* [Sergio Guasso](https://github.com/Guasso) A00826042

## Tokens
| Nombre      | Signo |
| ----------- | :-----------: |
| START      | Start       |
| FINISH   | Finish        |
| VAR      | Var       |
| WHILE      | While       |
| IF   | If        |
| ELSE      | Else       |
| DEF   | Def        |
| RETURN      | Return       |
| CLASS   | Class        |
| PRINT      | Print       |
 | MAIN   | Main        |
 | LEFT_CURRLY_BRACES   | { 
|RIGHT_CURRLY_BRACES      | }       |
| LEFT_PARENTHESIS   | (        |
| RIGHT_PARENTHESIS      | )       |
| LEFT_BRACKET   | \[        |
| RIGHT_BRACKET      | ]       |
| COMMA   | ,        |
| COLON      | :       |
 | DOT   | .        |
 | NEW_LINE   | \n 
|   LESS_THAN    |    <    |
| GREATER_THAN   |    >     |
| NOT_EQUAL   | (        |
| RIGHT_PARENTHESIS      | )       |
| EQUAL_COMPARATION  | ==        |
| EQUAL      | =       |
| OR   | \|        |
| AND      |    &    |
 | PLUS   | +        |
 | MINUS   | -     | 
|   ASTERISK    | *       |
| SLASH   |  /        |
| COMMENT   | #        |

## Tipos de datos
* Int
* Float
* String
* Bool
 
## Estatutos lineales
* Print
* Asignacion
* Declaracion
* Comentarios 

# Estatutos no linealies
* While
* If
* Else
* Funciones

## ✅ Fase 0 
Propuesta de compilador con lista de tokens, diagramas de sintaxis y otras consideraciones.
* [Diagramas](https://app.diagrams.net/#G1mg31Oh5NAC9qVDS2xzRFxlYAqREs92jk)
* [Propuesta inicial](https://docs.google.com/document/u/1/d/1IB2_lkkOPdiqoC8whCE7xx_i_9poXJEuTV0k2HAAKgI/edit) 

##  ✅Fase 1 
Ejemplo de codigo en lenguaje Omedetou, archivo sencillo de python con sintaxis en lark y ejemplo de funcionamiento en Lark IDE.

## ✅Fase 2
Ejemplo de clase funcional, corrección de diagramas de flujo, e inicio de lógica en puntos neuralgicos.

## ✅Fase 3
Semantica basica de expresiones, cubo semantico, generacion de expresiones aritmeticas y secuenciales.

## ✅Fase 4
Generacion de codigo de estatutos condicionales
* Validacion de gotof
* Validacion de ciclos anidados

## ✅Fase 5 
Generacion de codigo de funciones
* Directorio de funciones
* Creacion de objeto clase
* Variables locales
* Parche Guadalupano (Declaracion de funcion en globalVars)
* Recursion

##  ❓Fase 6 
Mapa de memoria / Maquina virtual
* ❓Estatutos secuenciales en MV
* ❓Expresiones aritmeticas en MV
* ✅Creacion de directorio de objetos
* ✅Creacion de objeto para linkear Tabla de Variables y directorio de funciones en objetos
* ❓Mapa de memoria



