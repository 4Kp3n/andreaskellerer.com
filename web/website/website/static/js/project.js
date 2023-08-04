/* Project specific Javascript goes here. */

  const toggleButton = document.querySelector('.nav-btn');
  const navbarContent = document.querySelector('.mob-nav');

  toggleButton.addEventListener('click', () => {
    if (navbarContent.classList.contains('hidden')) {
      navbarContent.classList.replace('hidden', 'flex');
    } else {
      navbarContent.classList.replace('flex', 'hidden');
    }
  });

  // Store DOM elements in variables
  const searchBtn = document.querySelector(".searchBtn");
  const searchBtn1 = document.querySelector(".searchBtn1");
  const searchModal = document.querySelector(".searchModal");
  const Modal = document.querySelector(".modal");
  const searchCloseBtn = document.querySelector(".searchCloseBtn");
  const searchSubmitBtn = document.querySelector(".searchSubmitBtn");
  const searchInput = document.querySelector(".searchInput");

  // Show Search Modal function
  function showSearchModal() {
    searchModal.style.display = "block";
  }

  // Hide Search Modal function
  function hideSearchModal() {
    searchModal.style.display = "none";
  }

  // Submit Search Form function
  function submitSearchForm(event) {
    event.preventDefault();
    const searchQuery = searchInput.value.trim();
    if (!searchQuery) {
      searchInput.classList.add('shake');
      setTimeout(function() {
        searchInput.classList.remove('shake');
      }, 500);
      return;
    }
    window.open("/search/?q=" + encodeURIComponent(searchQuery));
  }

  // Add event listeners
  searchBtn.addEventListener("click", showSearchModal);
  searchBtn1.addEventListener("click", showSearchModal);
  searchCloseBtn.addEventListener("click", hideSearchModal);
  searchSubmitBtn.addEventListener("click", submitSearchForm);
