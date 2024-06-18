var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    autoplay: true,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });



  var cards= document.querySelectorAll('.card-img img');
  

  cards.forEach(element => {
    element.classList.add('w-100')
  });




  // $("#contactForm").submit(function(e) {

  //   e.preventDefault(); 

  //   var form = $(this);
  //   var actionUrl = form.attr('action');
    
  //   $.ajax({
  //       type: "POST",
  //       url: actionUrl,
  //       data: form.serialize(), 
  //       success: function(data)
  //       {
  //           Swal.fire({
  //               title: 'Message!',
  //               text: 'Your message has been sent.',
  //               icon: 'success',
  //               confirmButtonText: 'Ok'
  //             })
  //             $('#contactForm').trigger("reset");
  //       }
  //   });
    
// });



document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    // Get form data
    const formData = new FormData(form);
    const name = formData.get("name");
    const email = formData.get("email");
    const phone = formData.get("phone");
    const address = formData.get("address");
    const message = formData.get("message");

    // Construct WhatsApp link with form data
    const whatsappLink = `https://wa.me/6392008441?text=Name: ${name}%0AEmail: ${email}%0APhone: ${phone}%0AAddress: ${address}%0AMessage: ${message}`;

    // Open WhatsApp link in a new tab/window
    window.open(whatsappLink, "_blank");
  });
});