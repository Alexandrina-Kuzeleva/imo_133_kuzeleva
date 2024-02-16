let price = +prompt()
let status = prompt()
if (price > 1000) {
  if (status === 'VIP') {
    console.log(price*0.9)
  } else {
    console.log(price*0.95)
  }
} else {
  console.log(price)
}