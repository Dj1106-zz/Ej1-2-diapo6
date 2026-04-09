En este proyecto se implementan los algoritmos necesarios para calcular los conjuntos PRIMEROS (FIRST), SIGUIENTES (FOLLOW) y PREDICCIÓN (PREDICT) a partir de una gramática libre de contexto.

Estos conceptos son fundamentales en la construcción de analizadores sintácticos, especialmente en parsers tipo LL(1), ya que permiten decidir qué producción aplicar en función del símbolo de entrada.

⚙️ Funcionamiento del programa

El programa recibe una gramática representada como un diccionario en Python y realiza tres procesos principales:

Calcula los conjuntos FIRST para cada no terminal
Calcula los conjuntos FOLLOW para cada no terminal
Calcula los conjuntos PREDICT para cada producción

Los resultados se imprimen en consola de forma clara.

🔹 Cálculo de FIRST (Primeros)

El conjunto FIRST contiene los símbolos terminales con los que puede comenzar una derivación desde un no terminal.

El algoritmo funciona así:

Se recorren todas las producciones de cada no terminal
Si el primer símbolo es un terminal, se agrega directamente
Si es un no terminal, se agregan sus FIRST (sin incluir ε)
Si ese símbolo puede producir ε, se continúa con el siguiente
Si toda la producción puede generar ε, entonces se agrega ε

Este proceso se repite en un ciclo hasta que no haya cambios en los conjuntos.

🔹 Cálculo de FOLLOW (Siguientes)

El conjunto FOLLOW contiene los símbolos que pueden aparecer inmediatamente después de un no terminal.

El algoritmo sigue estas reglas:

El símbolo inicial siempre contiene $ (fin de cadena)
Si un no terminal es seguido por otro símbolo, se agregan los FIRST de ese símbolo
Si ese símbolo puede producir ε, también se agregan los FOLLOW del no terminal actual
Si el no terminal está al final de una producción, hereda el FOLLOW del lado izquierdo

Se utiliza un ciclo iterativo para propagar correctamente la información hasta estabilizar los resultados.

🔹 Cálculo de PREDICT (Predicción)

El conjunto PREDICT se calcula para cada producción y sirve para decidir cuándo usarla.

Se calcula así:

Si la producción no genera ε:
→ PREDICT = FIRST(α)
Si la producción puede generar ε:
→ PREDICT = FIRST(α) - {ε} ∪ FOLLOW(A)

Esto permite construir tablas de análisis sintáctico.

🔁 Uso de iteraciones

Los algoritmos de FIRST y FOLLOW utilizan ciclos while porque los valores se van propagando entre los no terminales.
El proceso continúa hasta que los conjuntos dejan de cambiar, garantizando que el resultado es completo.
