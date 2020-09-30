document.getElementById("submit-zip").addEventListener("click", ourfunction)

workingZips = ["98138", "98139", "98140", "98142"]


function zipCheck(){
    input = input-zipcode.replace(/\s/g, '');
    for (i = 0; i < 4; i++) {
        if (input = workingZips[i]) {
            document.getElementById("result").innerHTML = "Vi kör hem till dig!";
            break;
        }
         else {
            document.getElementById("result").innerHTML = "Vi kör inte hem till dig!"; 
        }
    }   
}

