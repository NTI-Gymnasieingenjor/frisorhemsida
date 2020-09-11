default_dir="../public"

# Validerar skickad fil och skriver ut output
validate() {
    file=$1
    file_type=$2

    echo "$file:"

    # Validerar medskickad fil
    if [ "$file_type" == "html" ]
    then
        output=$(curl -s -F out=gnu -F "content=<$file" https://validator.nu/)
    elif [ "$file_type" == "css" ]
    then
        output=$(curl -s -F output=gnu -F "text=<$file" https://jigsaw.w3.org/css-validator/validator)
    else
        output="Okänd filtyp."
    fi

    # Skriver ut eventuella errors
    if [ "$output" == "" ]
    then
        echo "Ser bra ut!"
    else
        echo "$output"
    fi
}

# Söker efter alla filer inom specificerad mapp och dess submappar med specificerad filtyp och validerar dem.
iterate() {
    dir=$1
    file_type=$2
    

    echo -e "${file_type^^}:\n"
    
    for file in $(find $dir -type f -name "*.$file_type")
    do
        validate $file $file_type
        echo
    done
}

# Kollar om argument skickas med, annars valideras alla HTML- och CSS-filer programmet hittar.
if [ $# == 0 ]
then
    iterate $default_dir "html"
    echo
    iterate $default_dir "css"
else
    for arg in "$@"
    do
        # Skriver ut information för användning av programmet
        if [ "$arg" == "-help" ]
        then
            bold=$(tput bold)
            normal=$(tput sgr0)
            echo "${bold}Använding:${normal} validation.sh [-allhtml] [-allcss] [-help]"
            echo -e "${bold}default:${normal}      Validera alla html- och css-filer i den specifierade mappen. Den hittar också filer i submappar.\n"
            echo "${bold}-allhtml:${normal}     Validera alla html-filer i den specifierade mappen. Den hittar också filer i submappar."
            echo "${bold}-allcss:${normal}      Validera alla css-filer i den specifierade mappen. Den hittar också filer i submappar."
            echo "${bold}-help:${normal}        Skriv ut information om användning av kommandot."
            echo
        # Validerar enbart alla HTML-filer
        elif [ "$arg" == "-allhtml" ]
        then
            iterate $default_dir "html"

        # Validerar enbart alla CSS-filer
        elif [ "$arg" == "-allcss" ]
        then
            iterate $default_dir "css"

        # Körs om argumentet är ogiltigt
        else
            echo "Ogiltigt argument: $arg"
        fi
        echo
    done
    
fi