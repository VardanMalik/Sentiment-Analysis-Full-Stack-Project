// script.js

document.addEventListener('DOMContentLoaded', () => {
  // Sticky Header
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('header-scrolled');
    } else {
      header.classList.remove('header-scrolled');
    }
  });

  // Carousel (Bootstrap)
  const feedbackCarousel = document.querySelector('#feedbackCarousel');
  if (feedbackCarousel) {
    new bootstrap.Carousel(feedbackCarousel, {
      interval: 4000,
      ride: 'carousel'
    });
  }

  // Circular Rating Animation
  const ratingCircle = document.querySelector('.circle-rating');
  if (ratingCircle) {
    const value = parseFloat(ratingCircle.dataset.rating);
    const percentage = (value / 5) * 100;
    const circle = ratingCircle.querySelector('circle:last-child');
    const radius = circle.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (percentage / 100) * circumference;

    circle.style.strokeDasharray = `${circumference} ${circumference}`;
    circle.style.strokeDashoffset = circumference;

    setTimeout(() => {
      circle.style.transition = 'stroke-dashoffset 1s ease';
      circle.style.strokeDashoffset = offset;
    }, 100);
  }
});
