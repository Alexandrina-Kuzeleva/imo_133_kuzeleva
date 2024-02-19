let start = Number(prompt("Введите начальное значение диапазона:"));
let end = Number(prompt("Введите конечное значение диапазона:"));
let sum = 0;

for (let i = start; i <= end; i++) {
  sum += i;
}
console.log(sum);