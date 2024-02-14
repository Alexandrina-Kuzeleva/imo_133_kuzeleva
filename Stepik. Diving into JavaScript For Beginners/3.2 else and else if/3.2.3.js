let score = +prompt()
if (score >= 84) {
  console.log("Отлично")
} else if (score >= 64 && score < 84) {
  console.log("Хорошо")
} else {
  console.log("Учись")
}