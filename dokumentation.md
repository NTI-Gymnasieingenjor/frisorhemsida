# Dokumentation för projekt

## Branches

Projektet har just nu två permanenta branches: `master` och `development`. Detta är för att vi ska kunna köra git push på vår kod utan att det påverkar GitLab Pages-hemsidan, t.ex. ifall ofärdig kod är fast på någons dator. Eftersom vi alltid parprogrammerar kändes detta som nödvändigt, även om det kanske är en tillfällig lösning.

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