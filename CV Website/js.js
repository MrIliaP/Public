// Get the "Email" list item element
const emailListItem = document.querySelector('li:nth-of-type(1)');

// Add a click event listener to the "Email" list item
emailListItem.addEventListener('click', () => {
  // Display an alert with the email address
  alert('Email: pozhilenkov@gmail.com');
});

<<<<<<< HEAD
=======

>>>>>>> e55e77ba46cbd8f53f6a730c675490bbbd0b2254

function changeBackgroundColor() {
  const colorSelect = document.getElementById("colorSelect");
  const selectedColor = colorSelect.value;
  document.body.style.backgroundColor = selectedColor;
}

function toggleVisibility(id, buttonId) {
        const element = document.getElementById(id);
        element.classList.toggle("visible");
        element.classList.toggle("hidden");
<<<<<<< HEAD
        const button = document.getElementById(buttonId);
        if (element.classList.contains("visible")) {
          button.textContent = "Hide";
        } else {
          button.textContent = "Show Content";
        }
      }

function toggleVisibility(id, buttonId) {
        const element = document.getElementById(id);
        element.classList.toggle("visible");
        element.classList.toggle("hidden");
        const button = document.getElementById(buttonId);
        if (element.classList.contains("visible")) {
          button.textContent = "Hide Content";
        } else {
          button.textContent = "Show Content";
        }
      }
=======
      }
>>>>>>> e55e77ba46cbd8f53f6a730c675490bbbd0b2254
