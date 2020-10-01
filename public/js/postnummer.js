
// Make a list with the compatible zipcodes
const listOfZipCodes = [
    "98138",
    "98139",
    "98140",
    "98142"
];

// Makes variables
let zipInputElement;
let zipInputText;
let inputSubmitButton;

// Defines variables
zipInputElement = document.getElementById("input-zipcode")
inputSubmitButton = document.getElementById("submit-zip")

// When button is pressed, run zipCheck function
inputSubmitButton.addEventListener("click", zipCheck)

// Prevents site from reloading when pressing enter in form
$("#form-zip").keypress(function(e) {
    //Enter key
    if (e.which == 13) {
        e.preventDefault();
        zipCheck()
    }
  });

// Looks through list of compatible zipcodes to see if they match
// If they match, creates a popover == > "Vi kör hem till dig!"
// If not, creates a popover == > "Vi kör inte hem till dig!"
// NOTE: Popover aka the little box that appears under the element
function zipCheck() {
    zipInputText = zipInputElement.value.replace(/\s/g,'')  
    for (i = 0; i < 4; i++) {
        if (zipInputText == listOfZipCodes[i]) {
            $("#input-zipcode").attr("data-content", "Vi kör hem till dig!")
            $("#input-zipcode").popover('enable')
            $("#input-zipcode").popover('show')
            $("#input-zipcode").popover('disable')
            break;
        } 
        else {
            $("#input-zipcode").attr("data-content", "Vi kör inte hem till dig!")
            $("#input-zipcode").popover('enable')
            $("#input-zipcode").popover('show')
            $("#input-zipcode").popover('disable')
        }
    }
}   
