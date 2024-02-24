let num1 = +prompt()
let num2 = +prompt()
let num3 = +prompt()

function checkTriangleExistence (n,n1,n2) {
  if (n < n1+n2 && n1 < n+n2 && n2< n1+n) {
    console.log("Треугольник существует")
  } else {
    console.log("Треугольник не существует")
  }
}
checkTriangleExistence(num1,num2,num3)