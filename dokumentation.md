# Dokumentation för projekt

## Testning / Screenshots

`testing.py` är en kompilation av tester för de olika funktioner som hemsidan ska innhålla. Varje gång vi lägger till en funktion, så lägger vi även till några rader kod för att testa så att den fungerar. `testing.py` tar även screenshots på index.html i olika upplösningar när den körs.

För tillfället måste `testing.py` köras från VSCode med chromedriver.exe/geckodriver.exe i root working directory.

`screenshots.py` tar screenshots på hemsidan lokalt/online i olika upplösningar som definieras i en array i början av koden.

I både `testing.py` och `screenshots.py` kan man skicka med argument för att påverka hur programmet körs:

- [-online] - Testar sidan på GitLab Pages istället för den lokala sidan
- [-firefox] - Använder Firefox istället för Chrome.

## HTML/CSS-validation

`validation.sh` söker igenom "public"-mappen efter HTML- och CSS-filer, och skickar de till två olika validator-hemsidor för att sedan kunna skriva ut deras output i terminalen.

`validation.bat` består endast av ett kort kommando som startar den riktiga validatorn: `validation.sh`. Detta system finns bara för att det ska vara lätt och snabbt att köra filen.

Validatorn använder kommandot *curl* för att skicka kod till hemsidan och få svar. Som standard valideras alla HTML- och CSS-filer som programmet kan hitta, men om man skickar med argumentet "-help", visas ytterliggare info om hur programmet kan användas. Argument som skickas till `validation.bat` förs vidare till `validation.sh`.

Vi använder WSL för att kunna köra detta på datorn.


Information om CSS-validatorn:
- https://jigsaw.w3.org/css-validator
- https://jigsaw.w3.org/css-validator/manual.html


Information om HTML-validatorn:
- https://validator.nu/
- https://github.com/validator/validator/wiki/Service-%C2%BB-Input-%C2%BB-textarea
- https://github.com/validator/validator/wiki/Service-%C2%BB-Common-params

## Branches

Projektet har just nu två permanenta branches: `master` och `development`. Detta är för att vi ska kunna köra git push på vår kod utan att det påverkar GitLab Pages-hemsidan, t.ex. ifall ofärdig kod är fast på någons dator. Eftersom vi alltid parprogrammerar kändes detta som nödvändigt, även om det kanske är en tillfällig lösning.

## WSL

WSL (Windows Subsystem for Linux) är en funktion i Windows som låter dig köra ett helt Linux-operativsystem.

Vi använder operativsystemet Ubuntu genom WSL för att arbeta med shell-filer.

## Alternativ för layout av hemsida

Vi skriver HTML- och CSS-kod med hjälp av ramverket Bootstrap.

Vi bytte från att skriva allt från grunden till att använda Bootstrap efter att ha läst på om fem alternativ till layouting av hemsida. Vi dokumenterade för- och nackdelar med varje alternativ och valde sedan utifrån dem att använda Bootstrap. Vi valde att använda Bootstrap eftersom det:

- Används ofta och är väldokumenterat.
- Verkade mer effektivt att använda ett helt ramverk än en enkel metod.
- Är mer avancerat och välprövat än ramverket W3.CSS.
- Verkar som en bra sak att lära sig.

### Flexbox Layout

    Fördelar:
    - Lätt att centrera perfekt.
    - Bra för att strukturera objekt på sidan.
    - Flexibelt och responsivt utan att använda positionering.
    - Väldokumenterat.
    
    Nackdelar:
    - Inte lika omfattande som ett helt ramverk.
    - Fungerar inte med Internet Explorer 10 eller tidigare.

### Grid Layout

    Fördelar:
    - Anpassar sidan så att proporionerna alltid är korrekta.
    - Enkelt att strukturera hemsidan i rader och kolumner.
    - Väldokumenterat.

    Nackdelar:
    - Inte lika omfattande som ett helt ramverk.
    - Innehållet är inte lika responsivt som raderna/kolumnerna.

### Float Layout

    Fördelar:
    - Lätt att placera saker intill varandra.
    - Väldokumenterat.

    Nackdelar:
    - Buggigt när det används till mycket på en hemsida.

### W3.CSS

    Fördelar:
    - Ett helt ramverk.
    - Lätt att använda.
    - Använder enbart HTML och CSS.

    Nackdelar:
    - Inte det vanligaste ramverket (inte lika dokumenterat).

### Bootstrap

    Fördelar:
    - Ett helt ramverk.
    - Mycket väldokumenterat (det kändaste och mest använda ramverket).
    - Mer flexibel än W3.CSS.

    Nackdelar:
    - Högst inlärningskurva av alla alternativ.

## Live Share

Live Share är en extension till VSCode som vi har använt för att kunna arbeta tillsammans på distans. Live Share låter en person dela sin kod med andra, ungefär som ett Google-dokument. Alla kan redigera samtidigt, men filerna ligger på datorn hos den som är host för tillfället.

Detta kan leda till att alla commits på Git ser ut att vara från samma person, så vi ser till att byta host när det är lämpligt.

Två problem vi stött på med Live Share är:

- Bara host kan köra filerna.
- [CTRL + Z] kan förstöra andras kod.

https://fabilus.gitlab.io/frisorhemsida/