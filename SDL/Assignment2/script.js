function validateForm() {
    var username = document.getElementById('Username').value;
    var email = document.getElementById('exampleInputEmail1').value;
    var password = document.getElementById('Password').value;
    var languages = document.querySelectorAll('#language input[type="checkbox"]:checked');
    var country = document.getElementById('exampleFormControlSelect1').value;
    var gender = document.querySelector('#gender input[name="gender"]:checked');
    var address = document.getElementById('inputAddress').value;
    var pincode = document.getElementById('inputZip').value;
    var about = document.getElementById('w3review').value;

    if (validateUsername(username) &&
        validateEmail(email) &&
        validatePassword(password) &&
        validateLanguages(languages) &&
        validateCountry(country) &&
        validateGender(gender) &&
        validateAddress(address) &&
        validatePincode(pincode) &&
        validateAbout(about)) {
        alert('Form validation passed. You can proceed with submission.');
    }
}

function validateUsername(username) {
    if (username.trim() === '') {
        alert('Please enter a username.');
        return false;
    }
    return true;
}

function validateEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        return false;
    }
    return true;
}

function validatePassword(password) {
    var passwordRegex = /^(?=.*[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?])(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;

    if (!passwordRegex.test(password)) {
        alert('Password must contain at least 1 special character, 1 uppercase letter, 1 lowercase letter, and 1 digit.');
        return false;
    }
    if (password.length < 8) {
        alert('Password must be at least 8 characters long.');
        return false;
    }
    return true;
}

function validateLanguages(languages) {
    if (languages.length === 0) {
        alert('Please select at least one language.');
        return false;
    }
    return true;
}

function validateCountry(country) {
    if (country === '') {
        alert('Please select a country.');
        return false;
    }
    return true;
}

function validateGender(gender) {
    if (!gender) {
        alert('Please select a gender.');
        return false;
    }
    return true;
}

function validateAddress(address) {
    if (address.trim() === '') {
        alert('Please enter an address.');
        return false;
    }
    return true;
}

function validatePincode(pincode) {
    var pincodeRegex = /^\d{6}$/;
    if (!pincodeRegex.test(pincode)) {
        alert('Please enter a valid 6-digit pincode.');
        return false;
    }
    return true;
}

function validateAbout(about) {
    if (about.trim() === '') {
        alert('Please provide information about yourself.');
        return false;
    }
    return true;
}
