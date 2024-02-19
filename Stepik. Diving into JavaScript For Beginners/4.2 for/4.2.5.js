let debet = +prompt()
let month = +prompt()
debet /= 2
for (let i = 1; i <= month; i++) {
  debet *= 2
  console.log("Месяц",i+":",debet)
}