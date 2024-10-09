// Toggle sidebar for mobile and desktop
document.getElementById('mobile-menu').addEventListener('click', function() {
    document.getElementById('sidebar').classList.add('open');
});

// Close sidebar when close button is clicked
document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('sidebar').classList.remove('open');
});

// Mockup translation functionality
document.getElementById('translateBtn').addEventListener('click', function() {
    const inputText = document.getElementById('inputText').value;
    const outputText = inputText.split('').reverse().join('');
    document.getElementById('outputText').value = outputText;
});
