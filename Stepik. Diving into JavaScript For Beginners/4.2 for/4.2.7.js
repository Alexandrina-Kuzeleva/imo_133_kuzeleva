let a=Number(prompt());
let sum1=0;
let sum2=0;
for (let b=1;a>=b;b++) {
if (b%2==0) {
sum1+=1
}
else if (b%2!==0) {
sum2+=1
}
}
console.log ("Количество четных чисел:", sum1)
console.log ("Количество нечетных чисел:",sum2)