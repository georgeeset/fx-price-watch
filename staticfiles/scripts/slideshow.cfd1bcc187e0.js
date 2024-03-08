
window.addEventListener("DOMContentLoaded", (e) => {

  // Original JavaScript code by Chirp Internet: www.chirpinternet.eu
  // Please acknowledge use of this code by including this header.

  document.querySelectorAll(".fading-slideshow > li").forEach((slide) => {
    slide.addEventListener("animationend", (item) => {
      item.target.parentNode.appendChild(item.target);
    });
  });

});