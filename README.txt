Como ejecutar:

Basta correr el archivo main para tener una simulacion funcional

Controles:

K_UP = trasladar camara hacia arriba
K_DOWN = trasladar camara hacia abajo
K_LEFT = trasladar camara hacia la izquierda
K_RIGHT = trasladar camara hacia la derecha
K_o = Alejarse del plano
K_p = Acercarse al plano

Otras simulaciones:

Basta modificar los parametros de la linea 33, 34, 35.
Otra forma es descomentando la linea 36 ya que esta contiene condiciones iniciales distintas y cambia el aspecto de la ola, en este caso, se debe comentar la linea 37.

Existen setups pre definidos para algunas perturbaciones, para utilizar estas, se debe en la linea 38 dar un argumento a get_G() el cual debe ser el nombre de cualquiera de los archivos
llamados '4_20_03_98.txt' por ej. Para utilizar estas simulaciones se recomienda utilizar de parametros los valores indicados en el nombre del archivo de la siguiente forma:

'ANCHO_LARGO_DISTANCIA_GRAVEDAD.txt'

Bugs conocidos:

Para distancias <0.3 el modelo no es estable y diverge en la mayoria de los casos.
para X e Y < 3 , el modelo no compila, requiere al menos una grilla de 3x3 vertices.

