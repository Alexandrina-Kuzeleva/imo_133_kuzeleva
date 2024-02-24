let num1 = +prompt()
let num2 = +prompt()
let num3 = +prompt()
let num4 = +prompt()

function findMax (n,n1) {
  if (n > n1){
    return n
  } else{
    return n1
  }
}

function compareMax (n, n1) {
  if (n > n1) {
    console.log("Максимальное число первого набора больше")
  } else if (n1 > n) {
    console.log("Максимальное число второго набора больше")
  } else {
    console.log("Максимальные числа наборов равны")
  }
}

compareMax(findMax(num1,num2),findMax(num3,num4))