function check() {
    var p1 = document.getElementById("p1");
    var p2 = document.getElementById("p2");
    if (p1.value != p2.value) {
      p2.setCustomValidity("Пароли не совпадают");
      return false; // prevent the form from submitting
    } else {
      p2.setCustomValidity('');
    }
  }
  

  function CheckPassword() 
{ 
  var p1 = document.getElementById("p1").value;  
  if(p1.length < 8) {  

    document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters";  

    return false;  

  }    
  var pasw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
  if(p1.match(pasw)) { 
  return true;
  }
  else { 
    p1.setCustomValidity("Пароль должен содержать как минимум одну цифру, одну заглавную и одну строчную букву и быть длиной от 8 до 20 символов");
    return false;
  }
}
