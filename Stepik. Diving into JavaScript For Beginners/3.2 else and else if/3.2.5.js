let mood = parseInt(prompt("Введите число от 1 до 10: "), 10);

if (mood >= 1 && mood <= 3) {
    console.log("Плохое");
} else if (mood >= 4 && mood <= 7) {
    console.log("Нормальное");
} else if (mood >= 8 && mood <= 10) {
    console.log("Хорошее");
} else {
    console.log("Число вне диапазона");
}