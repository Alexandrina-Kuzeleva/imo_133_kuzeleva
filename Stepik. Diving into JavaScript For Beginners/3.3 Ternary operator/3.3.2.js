let weight = +prompt()
let priceDelivery = (weight > 5) ? 350 : 200
console.log('Стоимость доставки:', priceDelivery, 'рублей')