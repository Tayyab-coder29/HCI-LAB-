let cart = [];

function addToCart(name, price) {
  cart.push({name, price});
  localStorage.setItem("cart", JSON.stringify(cart));
  alert(name + " added to cart!");
}

window.onload = function() {
  if(document.getElementById("cart-items")) {
    cart = JSON.parse(localStorage.getItem("cart")) || [];
    let container = document.getElementById("cart-items");
    container.innerHTML = cart.map(item => `<p>${item.name} - PKR ${item.price}</p>`).join("");
  }
};
document.getElementById("checkout-form")?.addEventListener("submit", function(e) {
  e.preventDefault(); // stop page reload

  // Example: save to Firebase if connected
  // db.collection("orders").add({ ... })

  // Show confirmation message
  const formCard = document.querySelector(".form-card");
  formCard.innerHTML = `
    <h2>✅ Order Confirmed</h2>
    <p>Thank you for your purchase! Your order has been placed successfully.</p>
    <a href="index.html" class="btn">Return to Home</a>
  `;
});
let currentIndex = 0;
function moveSlide(step) {
  const slides = document.querySelector(".slides");
  const total = slides.children.length;
  currentIndex = (currentIndex + step + total) % total;
  slides.style.transform = `translateX(-${currentIndex * 100}%)`;
}
setInterval(() => moveSlide(1), 3000); // auto-slide every 3 seconds
let currentIndex = 0;

let currentIndex = 0;

function moveSlide(step) {
  const slides = document.querySelector(".slides");
  const total = slides.children.length;
  currentIndex = (currentIndex + step + total) % total;
  slides.style.transform = `translateX(-${currentIndex * 800}px)`; // match width
}

// Auto-play every 5 seconds
setInterval(() => moveSlide(1), 5000);
