document.addEventListener("DOMContentLoaded", function() {
    // Find all flash messages
    const flashMessages = document.querySelectorAll(".flash-message");

    // Set a timer to hide each flash message after 10 seconds (10000 milliseconds)
    flashMessages.forEach((flashMessage) => {
        setTimeout(() => {
            // Remove the 'show' class to trigger Bootstrap's fade-out effect
            flashMessage.classList.remove("show");

            // Optional: Delay to completely remove the message after fading out (500ms)
            setTimeout(() => {
                flashMessage.style.display = "none";  // Remove message from DOM
            }, 500); // 500ms delay after fade-out effect
        }, 10000); // 10 seconds = 10000 milliseconds
    });
});
