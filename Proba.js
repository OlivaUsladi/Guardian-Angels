"use strict";

function check() {
    let p1 = document.getElementById("p1");
    let p2 = document.getElementById("p2");
    if (p1.value != p2.value) {
      p2.setCustomValidity("Пароли не совпадают");
      return false; 
    } else {
      p2.setCustomValidity('');
      return true;
    }
  }
  

  function CheckPassword() 
{ 
  let p1 = document.getElementById("p1");  
  let pasw = /(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/;
  if(p1.value.match(pasw)) { 
    p1.setCustomValidity('');
    return true;
    
  }
  else { 
    p1.setCustomValidity("Пароль должен содержать как минимум одну цифру, одну заглавную и одну строчную букву и быть длиной не менее 8 символов");
    return false;
  }
}

