let num1 = +prompt();
let num2 = +prompt();
let action = prompt();
let result

function actionMath (num1, num2, action) {
    if (action == "+") {
        result = num1 + num2;
    } else if (action == "-") {
        result = num1 - num2;
    } else if (action == "*") {
        result = num1 * num2;
    } else if (action == "/") {
        result = num1 / num2;
    } else {
        result = "Неверный оператор";
    }
console.log(result);
}

actionMath (num1, num2, action)