# Sparar alla errors till variabler. output=gnu ger fin output, med en rad per error

cssout=$(curl -s -F output=gnu -F "text=<../public/css/style.css" https://jigsaw.w3.org/css-validator/validator)

htmlout=$(curl -s -F out=gnu -F "content=<../public/index.html" https://validator.nu/)


# Kollar om HTML-validatorn ger några errors, och printar dem isåfall (echo). Annars printas det att allt ser bra ut.
echo -e "HTML:\n"

if [ "$htmlout" == "" ]
then
    echo "All HTML ser bra ut!"
else
    echo "$htmlout"
fi

# Samma sak för CSS
echo -e "\n\nCSS:\n"

if [ "$cssout" == "" ]
then
    echo "All CSS ser bra ut!"
else
    echo "$cssout"
fi