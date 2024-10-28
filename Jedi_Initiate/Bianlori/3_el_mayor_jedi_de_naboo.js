/* 3. El mayor Jedi de Naboo (Máximo de tres números)
Contexto temático:
Obi-Wan Kenobi, Qui-Gon Jinn y el joven Anakin Skywalker están compitiendo en una carrera en Naboo.
 Solo uno de ellos alcanzará la mayor velocidad en sus naves. Encuentra al más rápido.

Objetivo:
Dado tres números, encuentra el mayor de ellos.

Instrucciones:

La función debe recibir tres números y devolver el mayor de los tres.
No utilices funciones incorporadas como max().
Pista:
Compara los números dos a dos para encontrar el mayor. */

console.log("sirve");


let numeros = [8, 9, 12]

    if (numeros[0] >= numeros[1] && numeros[0] >= numeros[2]  ){
        console.log(`${numeros[0]} es mayor`);
    } else if ( numeros [1] >= numeros[2]){
        console.log(`${numeros[1]} es mayor`);
    }else {
        console.log(`${numeros[2]} es mayor`);
    }
