'use strict';



function updateMatrixStr() {
    const ip = Array.from(document.getElementsByClassName('e_matrix')).map(x => x.value); //document.getElementsByClassName('e_matrix');
    let matrixBuild = `[[${ip[0]}, ${ip[1]}, ${ip[2]}], [${ip[3]}, ${ip[4]}, ${ip[5]}], [${ip[6]}, ${ip[7]}, ${ip[8]}]]`;
    document.getElementById('matrix_str').textContent = matrixBuild
}

updateMatrixStr()

document.querySelectorAll('input[type="text"]').forEach(input => {
    input.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent form submission or default behavior
            const inputs = Array.from(document.querySelectorAll('input[type="text"]'));
            const index = inputs.indexOf(event.target);
            console.log("hi")
            if (index !== -1 && index < inputs.length - 1) {
                let length = inputs[index + 1].value.length;
                input.setSelectionRange(length, length);
                inputs[index + 1].focus(); // Focus the next input
            }
        }
    });
    input.addEventListener('change', updateMatrixStr)
});
function validateMatrixInput(event) {
    var char = String.fromCharCode(event.which);
    if (!/[0-9-]/.test(char)) {
        event.preventDefault();
    }
}
function validateStringInput(event) {
    var input = event.target.value;
    event.target.value = input.toUpperCase().replace(/[^A-Z ]/g, '');
}

document.getElementById('copy_encode').addEventListener('click', function() {
    let encoded = document.getElementById('encoded_output').textContent
    if (encoded) {
        navigator.clipboard.writeText(encoded);
    } else {
        alert("Copy: Please Encode first")
    }
})
document.getElementById('copy_decode').addEventListener('click', function() {
    let decoded = document.getElementById('decoded_output').textContent
    if (decoded) {
        navigator.clipboard.writeText(decoded);
    } else {
        alert("Copy: Please Decode first")
    }
})