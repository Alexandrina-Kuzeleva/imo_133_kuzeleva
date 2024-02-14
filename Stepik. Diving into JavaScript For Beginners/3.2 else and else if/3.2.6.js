let side1 = + prompt(), side2 = + prompt(), side3 = + prompt();
if (side1 === side2 && side3 === side2) {
  console.log('Равносторонний')
} else if (side1 === side2 || side1 === side3 || side2 === side3) {
  console.log('Равнобедренный')
} else {
  console.log('Разносторонний')
}