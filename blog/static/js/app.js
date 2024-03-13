/* Theme Name: Trenddy  - Responsive Blog Template
   Author: Pichforest
   Version: 1.0.0
   File Description: Main JS file of the template
*/

// Swiper
var swiper = new Swiper('.swiper-main-slider', {
    slidesPerView: 2.2,
    centeredSlides: false,
    slidesPerGroupSkip: 1,
    grabCursor: true,
    keyboard: {
        enabled: true,
    },

    breakpoints: {
        576: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 1,
        },
        1500: {
          slidesPerView: 1.6,
          Slides:true,
        },
    }
});


// Swiper
var swiper = new Swiper('.swiper-one-view', {
  slidesPerView: 1,
  spaceBetween: 10,
  centeredSlides: false,
  slidesPerGroupSkip: 1,
  grabCursor: true,
  keyboard: {
      enabled: true,
  },

  breakpoints: {
      576: {
        slidesPerView: 1,
        spaceBetween: 10,
      },
      768: {
        slidesPerView: 1,
        spaceBetween: 10,
      },
      1500: {
        slidesPerView: 1,
        spaceBetween: 10,
      },
  }
});

// Swiper 2 view
var swiper = new Swiper('.swiper-two-view', {
  slidesPerView: 2,
  spaceBetween: 10,
  centeredSlides: false,
  slidesPerGroupSkip: 1,
  keyboard: {
      enabled: true,
  },
  breakpoints: {
    576: {
      slidesPerView: 1,
      spaceBetween: 10,
      centeredSlides: true,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    1500: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
}
});

// Swiper 3 view
var swiper = new Swiper('.swiper-three-view', {
  slidesPerView: 3,
  spaceBetween: 10,
  keyboard: {
      enabled: true,
  },
  breakpoints: {
    576: {
      slidesPerView: 1,
      spaceBetween: 10,
      centeredSlides: true,
    },
    768: {
      spaceBetween: 10,
      slidesPerView: 2,
    },
    1500: {
      spaceBetween: 10,
      slidesPerView: 3,
    },
}
});





// Contact Form
function validateForm() {
  var name = document.forms["myForm"]["name"].value;
  var email = document.forms["myForm"]["email"].value;
  var subject = document.forms["myForm"]["subject"].value;
  var comments = document.forms["myForm"]["comments"].value;
  document.getElementById("error-msg").style.opacity = 0;
  document.getElementById('error-msg').innerHTML = "";
  if (name == "" || name == null) {
      document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning'>*Please enter a Name*</div>";
      fadeIn();
      return false;
  }
  if (email == "" || email == null) {
      document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning'>*Please enter a Email*</div>";
      fadeIn();
      return false;
  }
  if (subject == "" || subject == null) {
      document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning'>*Please enter a Subject*</div>";
      fadeIn();
      return false;
  }
  if (comments == "" || comments == null) {
      document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning'>*Please enter a Comments*</div>";
      fadeIn();
      return false;
  }

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
          document.getElementById("simple-msg").innerHTML = this.responseText;
          document.forms["myForm"]["name"].value = "";
          document.forms["myForm"]["email"].value = "";
          document.forms["myForm"]["subject"].value = "";
          document.forms["myForm"]["comments"].value = "";
      }
  };
  xhttp.open("POST", "php/contact.php", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("name=" + name + "&email=" + email + "&subject=" + subject + "&comments=" + comments);
  return false;
}

function fadeIn() {
  var fade = document.getElementById("error-msg");
  var opacity = 0;
  var intervalID = setInterval(function () {
      if (opacity < 1) {
          opacity = opacity + 0.5
          fade.style.opacity = opacity;
      } else {
          clearInterval(intervalID);
      }
  }, 200);
}


//
/********************* Swicher js ************************/
//

function toggleSwitcher() {
  var i = document.getElementById("style-switcher");
  if (i.style.left === "-189px") {
    i.style.left = "-0px";
  } else {
    i.style.left = "-189px";
  }
}

function setColor(theme) {
  document.getElementById("color-opt").href = "./css/colors/" + theme + ".css";
  toggleSwitcher(false);
}