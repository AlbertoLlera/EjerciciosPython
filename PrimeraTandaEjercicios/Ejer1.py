a=248
b=200
z=a+b
print("El resultado es de la suma de ", a, "+", b, " es ", z)

/* Versión ideada por mi, pero que no funciona. Lanza un error y detiene el programa.
Esto sucede porque estaba mezclando exportar funciones con el closure.
Lo que hago aquí en realidad, es devolver la función y no el array como tal.
Para que funcione, tiene que ser como en el segundo ejemplo, donde realmente lo que hace el closure es almacenar el array.
export function registrarJugada(jugada){
    let historialMovimientos = [];
    return function (){
        historialMovimientos.push(jugada);
        return historialMovimientos;
    }
}
 */

//Esta es la versión que me ha dado chatGPT