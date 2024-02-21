let a = Number(prompt("Введите первое число: "));



let b = Number(prompt("Введите второе число: "));



 



function func(a, b) {



  if (a > b) {



    return a + ' больше, чем ' + b;



  }



 



  else if ( a == b){



    return b + ' равно ' + a;



  }



  else {



    return b + ' больше, чем ' + a;



  }





 



}



 



let result = func (a, b);



console.log (result);