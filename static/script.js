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




  $("#contactForm").submit(function(e) {

    e.preventDefault(); 

    var form = $(this);
    var actionUrl = form.attr('action');
    
    $.ajax({
        type: "POST",
        url: actionUrl,
        data: form.serialize(), 
        success: function(data)
        {
            Swal.fire({
                title: 'Message!',
                text: 'Your message has been sent.',
                icon: 'success',
                confirmButtonText: 'Ok'
              })
              $('#contactForm').trigger("reset");
        }
    });
    
});