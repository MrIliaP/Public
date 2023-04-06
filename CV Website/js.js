

function copyEmail() {
        const email = 'pozhilenkov@gmail.com';
        navigator.clipboard.writeText(email);
        alert(`Email "${email}" has been copied to the clipboard.`);
      }


function changeBackgroundColor() {
  const colorSelect = document.getElementById("colorSelect");
  const selectedColor = colorSelect.value;
  document.body.style.backgroundColor = selectedColor;
}

function toggleVisibility(id, buttonId) {
        const element = document.getElementById(id);
        element.classList.toggle("visible");
        element.classList.toggle("hidden");
        const button = document.getElementById(buttonId);
        if (element.classList.contains("visible")) {
          button.textContent = "Hide";
        } else {
          button.textContent = "Show Content";
        }
      }
