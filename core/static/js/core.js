
  function adjustPadding() {
    const header = document.querySelector('.sticky-header');
    const pageContent = document.querySelector('.page-content');
    if (header && pageContent) {
      pageContent.style.paddingTop = header.offsetHeight + 'px';
    }
  }

  window.addEventListener('DOMContentLoaded', adjustPadding);
  window.addEventListener('resize', adjustPadding);
