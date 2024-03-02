let S = +prompt()
let h = +prompt()
let operation = prompt()

if (operation === 'цилиндр') {
    let calculateCylinderVolume = (S, h) => (S*h)
    console.log('Объем цилиндра:',calculateCylinderVolume(S,h))
} else {
    let calculateConeVolume = (S,h) => ((1/3)*S*h)
    console.log('Объем конуса:',calculateConeVolume(S,h))
}