let num = +prompt()
let numFactorial = 1
let count = 1
while (count <= num) {
  numFactorial *= count
  count++
}
console.log('Факториал числа', num, 'равен', numFactorial)