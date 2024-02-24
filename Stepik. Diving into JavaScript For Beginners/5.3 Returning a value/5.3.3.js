let num1 = +prompt()
let num2 = +prompt()
let num3 = +prompt()
let num4 = +prompt()

function calculateAverage (n,n1) {
  return (n+n1)/2
}

function compareAverages (n, n1) {
  if (n > n1) {
    console.log("Среднее значение первого набора больше")
  } else if (n1 > n) {
    console.log("Среднее значение второго набора больше")
  } else {
    console.log("Средние значения наборов равны")
  }
}

compareAverages(calculateAverage(num1,num2),calculateAverage(num3,num4))