// Get the "Email" list item element
const emailListItem = document.querySelector('li:nth-of-type(1)');

// Add a click event listener to the "Email" list item
emailListItem.addEventListener('click', () => {
  // Display an alert with the email address
  alert('Email: pozhilenkov@gmail.com');
});

// Get the "About" section element
const aboutSection = document.querySelector('.section:nth-of-type(1)');

// Add a click event listener to the "About" section
aboutSection.addEventListener('click', () => {
  // Toggle the visibility of the paragraph element within the "About" section
  const aboutParagraph = aboutSection.querySelector('p');
  aboutParagraph.classList.toggle('hidden');
});

function changeBackgroundColor() {
  const colorSelect = document.getElementById("colorSelect");
  const selectedColor = colorSelect.value;
  document.body.style.backgroundColor = selectedColor;
}

function toggleVisibility(id) {
        const element = document.getElementById(id);
        element.classList.toggle("visible");
        element.classList.toggle("hidden");
      }