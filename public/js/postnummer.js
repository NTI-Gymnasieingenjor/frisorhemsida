document.getElementById("submit-zip").addEventListener("click", zipCheck)

let workingZips = ["98138", "98139", "98140", "98142"]
let submitZip = document.getElementById("submit-zip")

function zipCheck() {
    let inputValue = textInputElement.value.replace(" ", "")
}

onload = (() => {
        let input = document.getElementById("input-zipcode")
        let submitZip = document.getElementById("submit-zip")

        input.addEventListener("keyup", function (event) {
            if (e.key === "Enter") {
                e.preventDefault();
                submitZip.click();
        };
        
    });
});

// let workingZips = ["98138", "98139", "98140", "98142"]

// function zipCheck(){

//     let input = document.getElementById("input-zipcode")
//     // Startvärde på variabel; Hur länge loopen körs; vad som händer när loopen körts
//     for (i = 0; i < 4; i++) {
//         if (input == workingZips[i]) {
//             document.getElementById("result").innerHTML = "Vi kör hem till dig!";
//             break;
//         }
//         else {
//             document.getElementById("result").innerHTML = "Vi kör inte hem till dig!"; 
//         }
//     }   
// }

// let workingZips = ["98138", "98139", "98140", "98142"]
// let input = document.getElementById("input-zipcode").value
// let currentZip = workingZips[input]

// function zipCheck() {
//     let input = document.getElementById("input-zipcode").value

//     return input
// }

// function zipCheck() {
//     let workingZips = ["98138", "98139", "98140", "98142"]
//     let input = document.getElementById("input-zipcode").value
//     let currentZip = workingZips[input]
//     switch (currentZip) {
//         case "98138": 
//             document.getElementById("result").innerHTML = "Vi kör hem till dig!";
//             break;
//         case "98139": 
//             document.getElementById("result").innerHTML = "Vi kör hem till dig!";
//             break;
//         case "98140": 
//             document.getElementById("result").innerHTML = "Vi kör hem till dig!";
//             break;
//         case "98142": 
//             document.getElementById("result").innerHTML = "Vi kör hem till dig!";
//             break;
//         default:
//             document.getElementById("result").innerHTML = "Vi kör inte hem till dig!";
//             break;
//         return input
//     }
// }
