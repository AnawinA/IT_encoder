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
const searchBox = document.getElementById('search-box');

const topicUsing = document.getElementById('topic-using');
const toolUsing = document.getElementById('tool-using');

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
    topicUsing.textContent = topic
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

const toolRemember = localStorage.getItem('tool') || 'base64';
const topicRemember = localStorage.getItem('topic') || 'binary';

toolUsing.textContent = toolRemember;
topicUsing.textContent = topicRemember;

inputText.addEventListener('change', function() {
    localStorage.setItem('tool', toolUsing.textContent);
    localStorage.setItem('topic', topicUsing.textContent);
})





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


// Modal
const modal = document.getElementById('modal');
const openModalBtn = document.getElementById('openModal');
const closeModalBtn = document.getElementById('close-modal-btn');
const arrowOverlap = document.getElementsByClassName('arrow-translate')[0];

openModalBtn.addEventListener('click', () => {
  modal.style.display = 'flex';
  modal.classList.add('show');
  modal.classList.remove('hide');
  arrowOverlap.style.visibility = 'hidden';
});


modal.addEventListener('click', (event) => {
    console.log("hi")
    if (event.target === modal || event.target === closeModalBtn) {
      modal.classList.add('hide');
      modal.classList.remove('show');
      setTimeout(() => {
        modal.style.display = 'none';
        arrowOverlap.style.visibility = 'visible';
      }, 400); // Timeout matches animation duration for smooth transition
    }
  });