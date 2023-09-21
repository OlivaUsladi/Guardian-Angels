let fname = document.querySelector('#fname');
let lname = document.querySelector('#lname');
let email = document.querySelector('#email');
let pas1 = document.querySelector('#p1');
let pas2 = document.querySelector('#p2');
let submit = document.querySelector('#submit');

let users={};

function User(fname, lname, email, pas1){
    this.fname = fname;
    this.lname = lname;
    this.email = email;
    this.pas1 = pas1;
}

function createID(users){
    return Object.keys(users).length;
}

submit.addEventListener("click", () => {
    const fnameUser = fname.value;
    const lnameUser = lname.value;
    const emailUser = email.value;
    const passwordUser = pas1.value;

    const user = new User(fnameUser, lnameUser, emailUser, passwordUser);

    const userId = 'User' + createID(users);
    users[userId] = user;

    console.log(users);
})