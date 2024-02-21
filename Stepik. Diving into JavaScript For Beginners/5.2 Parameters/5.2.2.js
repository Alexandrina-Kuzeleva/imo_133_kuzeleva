let userNum = +prompt()
function factorial(num) {
  let numFactorial = 1
  let count = 1
  while (count <= num) {
    numFactorial *= count
    count++
  }
  console.log(numFactorial)
}
factorial(userNum)