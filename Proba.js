"use strict";

function check() {
    let p1 = document.getElementById("p1");
    let p2 = document.getElementById("p2");
    if (p1.value != p2.value) {
      p2.setCustomValidity("Пароли не совпадают");
      return false; // prevent the form from submitting
    } else {
      p2.setCustomValidity('');
    }
  }
  

  function CheckPassword() 
{ 
  let p1 = document.getElementById("p1");  
  /*if(p1.value.length < 8) {  

    //Выводит внизу формы, а должен как уведомление в строке (set.CustomValidity), но НЕ РАБОТАЕТ
    document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters";  

    //При return завершается программа? Тогда объединить if, если ЭТА МРАЗЬ ЗАРАБОТАЕТ
    return false;  

  }    */
  let pasw = /(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/;
  if(p1.value.match(pasw)) { 
    console.log('Cработало');
    return true;
    
  }
  else { 
    //работает только со 2 клика
    p1.setCustomValidity("Пароль должен содержать как минимум одну цифру, одну заглавную и одну строчную букву и быть длиной от 8 до 20 символов");
    console.log('Работай, падла');
    return false;
  }
}


