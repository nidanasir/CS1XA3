var i = 0;
var txt = 'Student, Programmer, Enthuastic Learner, Hard Worker.';
var speed = 50;

;(function typeWriter() {
  if (i < txt.length) {
    document.getElementById("demo").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
})()