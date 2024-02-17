let num = +prompt()
let result = num
let count = 0
while (result < 1000) {
  result *=2
  count +=1
}
console.log('Итоговое число:', result)
console.log('Количество итераций:', count)