let num = +prompt()
let sum = 0
for (let i = 1; i <= num; i += 2) {
  sum += i
}
console.log("Сумма нечетных чисел от 1 до", num, "равна", sum)