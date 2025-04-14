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

  // Initialize Carousel (if using Bootstrap)
  const feedbackCarousel = document.querySelector('#feedbackCarousel');
  if (feedbackCarousel) {
    const carousel = new bootstrap.Carousel(feedbackCarousel, {
      interval: 4000,
      ride: 'carousel'
    });
  }

  // Circular Rating Chart
  const ratingCircle = document.querySelector('.circle-rating');
  if (ratingCircle) {
    const value = parseFloat(ratingCircle.dataset.rating);
    const percentage = (value / 5) * 100;
    const circle = ratingCircle.querySelector('circle:last-child');
    const radius = circle.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (percentage / 100) * circumference;

    circle.style.strokeDasharray = `${circumference} ${circumference}`;
    circle.style.strokeDashoffset = offset;
  }
});
