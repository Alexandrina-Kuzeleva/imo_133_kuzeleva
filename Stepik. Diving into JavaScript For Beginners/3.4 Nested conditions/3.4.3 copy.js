let mon=+prompt("Месяц")

let tempr=+prompt()

let season=""

let output=""

if(mon ==1 || mon==2 || mon==12)

{

    season="Зима"

    output=season+((tempr<=-25)?' (холодная '+season.toLowerCase()+')':"")

}

else if(mon ==3 || mon==4 || mon==5)

{

    season="Весна"

    output=season+((tempr<15)?' (прохладная '+season.toLowerCase()+')':"")

}

else if(mon ==6 || mon==7 || mon==8)

{

    season="Лето"

    output=season+((tempr>=30)?' (жаркое '+season.toLowerCase()+')':"")

}

else if(mon ==9 || mon==10 || mon==11)

{

    season="Осень"

    output=season+((tempr<0)?' (прохладная '+ season.toLowerCase()+')':"")

}

console.log(output)