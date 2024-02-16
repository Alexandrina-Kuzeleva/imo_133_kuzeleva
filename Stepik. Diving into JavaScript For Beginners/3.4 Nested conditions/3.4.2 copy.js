let weight = Number(prompt())
let status = prompt()

if (weight <= 5)

{ if (status === "экспресс"){console.log('Стоимость доставки: '+1000+' рублей');}

else if (status === "обычная"){console.log('Стоимость доставки: '+500+' рублей');}

else {console.log('Некорректный статус доставки');}}


if(weight>5)

{if (status === "экспресс"){console.log('Стоимость доставки: '+1500+' рублей')}

else if (status === "обычная"){console.log('Стоимость доставки: '+800+' рублей')}

else {console.log('Некорректный статус доставки')} }