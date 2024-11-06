// Toggle sidebar for mobile and desktop
const sidebar = document.getElementById('sidebar');

document.getElementById('mobile-menu').addEventListener('click', function() {
    sidebar.classList.add('open');
});

// Close sidebar when close button is clicked
document.getElementById('close-btn').addEventListener('click', function() {
    sidebar.classList.remove('open');
});

const inputText = document.getElementById('inputText');
const outputText = document.getElementById('outputText');
const searchBox = document.getElementById('search-box');

const topicUsing = document.getElementById('topic-using');
const toolUsing = document.getElementById('tool-using');

document.getElementById('isDecode').addEventListener('click', function() {
    if (this.checked) {
        this.nextSibling.textContent = "Decode"
    } else {
        this.nextSibling.textContent = "Encode"
    }
    const temp = inputText.value
    inputText.value = outputText.value
    outputText.value = temp
})

document.getElementById('translator-form').onsubmit = function(e) {
    e.preventDefault();
}

// document.getElementById('clearBtn').addEventListener('click', function() {
//     inputText.value = ""
//     outputText.value = ""
// })


document.getElementById('copyBtn').addEventListener('click', function() {
    navigator.clipboard.writeText(outputText.value);
})

const params = new URLSearchParams(window.location.search);
const tool = params.get('c')
if (tool) {
    toolUsing.textContent = tool
}


const userPrefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
const savedTheme = localStorage.getItem('theme') || (userPrefersDark ? 'dark' : 'light');

// Apply the saved or prefered theme
if (savedTheme === 'dark') {
  document.body.classList.add('dark-mode');
}

// Toggle and save theme
function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  console.log("toggle")
  const currentTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
  localStorage.setItem('theme', currentTheme);
}


// const toolRemember = localStorage.getItem('tool') || 'base64';
// const topicRemember = localStorage.getItem('topic') || 'binary';





function searching(e) {
    const searchValue = e.target.value.toUpperCase();
    const items = searchBox.getElementsByTagName('li');

    for (let i = 0; i < items.length; i++) {
        const a = items[i].getElementsByTagName('span')[0];
        const textValue = a.textContent || a.innerText;
        if (textValue.toUpperCase().indexOf(searchValue) > -1) {
            items[i].style.display = '';
        } else {
            items[i].style.display = 'none';
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const items = searchBox.getElementsByTagName('li');
    for (let i of items) {
        const a = i.getElementsByTagName('span')[0];
        a.addEventListener('click', (e) => {
            console.log("hello")
            toolUsing.textContent = a.textContent || a.innerText;
            sidebar.classList.remove('open');
        })
        const textValue = a.textContent || a.innerText;
            console.log("hi", textValue)
    }
})
