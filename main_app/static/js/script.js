// CONSTANTS
// -----------------------------
const currentYear = new Date().getFullYear();

// CACHED ELEMENT REFERENCES
// -----------------------------
const footerContent = document.querySelector('footer > div');
footerContent.innerHTML = `&copy; ${currentYear} Threadarium &nbsp;`;
