let lengthCar = Number(prompt());
let engineCar = Number(prompt());
if (lengthCar <= 3.8 && engineCar <= 1.2) {
    console.log("Класс A")
}
else if (lengthCar <= 4 && engineCar <= 1.6) {
    console.log ("Класс B")
}
else if (lengthCar <= 4.5 && engineCar > 1.6 && engineCar <= 2) {
    console.log ("Класс C")
}
else {
console.log("Выберите автомобиль другого класса")
}