// Toggle sidebar for mobile and desktop
document.getElementById('mobile-menu').addEventListener('click', function() {
    document.getElementById('sidebar').classList.add('open');
});

// Close sidebar when close button is clicked
document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('sidebar').classList.remove('open');
});

const inputText = document.getElementById('inputText');
const outputText = document.getElementById('outputText');


document.getElementById('isDecode').addEventListener('click', function() {
    if (this.checked) {
        this.nextSibling.textContent = "Decode"
    } else {
        this.nextSibling.textContent = "Encode"
    }
})

document.getElementById('translator-form').onsubmit = function(e) {
    e.preventDefault();
}

document.getElementById('copyBtn').addEventListener('click', function() {
    navigator.clipboard.writeText(outputText.value);
})

const params = new URLSearchParams(window.location.search);
const topic = params.get('e');
const tool = params.get('c')
if (topic && tool) {
    document.getElementById('topic-using').textContent = topic
    document.getElementById('tool-using').textContent = tool
} else {
    console.log("no data")
}
