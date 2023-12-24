// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Get the form elements
    const searchForm = document.querySelector('form[action*="search"]');
    const queryInput = searchForm.querySelector('input[name="query"]');

    // Add an event listener for the form submission
    searchForm.addEventListener('submit', function(event) {
        // Prevent the form from being submitted
        event.preventDefault();

        // Get the query from the input
        const query = queryInput.value.trim();

        // If the query is not empty, submit the form
        if (query !== '') {
            searchForm.submit();
        }
    });
});
