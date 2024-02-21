let userName = prompt()
let userAge = +prompt()
function printHello(name,age) {
  console.log("Привет,",name+".","Тебе", age,"лет.")
}

printHello(userName,userAge)