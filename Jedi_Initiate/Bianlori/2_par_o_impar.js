/* 2. El destino del droide (Par o impar)
Contexto temático:
R2-D2 debe resolver un problema en los circuitos de la nave.
 Para decidir qué ruta seguir, debe determinar si un número dado es par o impar.

Objetivo:
Crea un programa que determine si un número es par o impar.

Instrucciones:

La función debe recibir un número entero y determinar si es par o impar.
Si el número es divisible por 2, es par; si no, es impar.
Pista:
El operador módulo (%) es útil para saber si un número es divisible por otro.

 */

function numEntero(a) {
   let resultdo = a % 2;
    if (resultdo === 0) {
        console.log("par : " + a);   
    } else{
        console.log("impar: " + a); 
    }
}
(numEntero(3));

