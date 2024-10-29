/* 4. El poder de la Fuerza (Número factorial)
Contexto temático:
En su entrenamiento, Anakin debe calcular el poder de la Fuerza que ha acumulado. 
Este poder crece exponencialmente como el factorial de un número dado.

Objetivo:
Calcula el factorial de un número utilizando un bucle.

Instrucciones:

Escribe una función que reciba un número entero y devuelva su factorial.
Utiliza un bucle para multiplicar los números desde 1 hasta el número dado.
Pista:
El factorial de un número n es el producto de todos los números desde 1 hasta n.

 */

 function factorial (numEntero) {
    let factorialNumeroEntero = 1;
    let i = 1;
    while (i <= numEntero) {
        factorialNumeroEntero *= i;
        i++;
    }

    return factorialNumeroEntero;
    
}
console.log(factorial(4));




