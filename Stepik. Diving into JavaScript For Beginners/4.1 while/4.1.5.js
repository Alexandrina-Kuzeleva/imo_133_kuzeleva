let num1 = +prompt();
let num2 = +prompt();
if (num1 > num2) {
  while (num1 >= num2) {
    console.log(num1)
    num1--
  }
} else {
  while (num1 <= num2) {
    console.log(num1)
    num1++
  }
}