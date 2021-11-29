"use strict";
$(document).ready(() => {
  const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
  const passwordPattern=/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -/:-@\[-`{-~]).{6,64}$/;

  $("#registration_form").submit((evt) => {
    let isValid = true;

    // validate the name text
    let username=$("#username")
    const name =username.val().trim();
    console.log(name)
    if (name === "") {
      username.next().text("This field is required.");
      isValid = false;
    } else {
      username.next().text("");
    }
    username.val(name);

    // validate the email1 input
    let email1=$("#email1")
    const email1Val = email1.val().trim();
    console.log(email1Val)
   if (!emailPattern.test(email1Val)) {
      // email1.next().text("Must be a valid email address.");
      isValid = false;
      email1.next().text("Must be a valid email address.");

    } else {
      email1.next().text("");
    }
    email1.val(email1Val);

    // validate the email2 input
    let email2=$("#email2")
    const email2Val = email2.val().trim();
    if (!emailPattern.test(email2Val)) {
      email2.next().text("Must be a valid email address.");
      isValid = false;
    } else if(email2Val !== email1Val){
       email2.next().text("emails doesn't match");
      isValid = false;
    }else {
      email2.next().text("");
    }
    email2.val(email2Val);

 // validate the password input
    let pass1=$("#pass1")
    const pass1val = pass1.val().trim();
    if (!passwordPattern.test(pass1val)) {
      pass1.next().text("must include capital and small letters,number,special characters and the length between 6:64 ");
      isValid = false;
    } else {
      pass1.next().text("");
    }
    pass1.val(pass1val);

    // validate the password2 input
    let pass2=$("#pass2")
    const pass2val = pass2.val().trim();
    if (!passwordPattern.test(pass2val)) {
      pass2.next().text("must include capital and small letters,number,special characters and the length between 6:64 ");
      isValid = false;
    } else if(pass2val!==pass1val){
       pass2.next().text("password doesn't match");
      isValid = false;
    }else {
      pass2.next().text("");
    }
    pass2.val(pass2val);

    if (isValid === false) {
      evt.preventDefault();
    }
  });
}); // end ready
