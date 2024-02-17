let num1=Number(prompt("Введите число:"));

let num2=Number(prompt("Введите число:"));

if (num1>num2){while(num1>=num2){if(num1%3===0){

    console.log(num1);}

    num1-=1;}}

else if(num1<num2){while(num1<=num2){if(num1%3===0){

    console.log(num1);}

    num1+=1;}}