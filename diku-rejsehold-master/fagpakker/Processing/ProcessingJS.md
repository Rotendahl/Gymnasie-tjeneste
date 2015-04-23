Hej mentorer (gymnasie task force!!)

Vi (Troels og Martin) er blevet bedt om at komme med nogle idéer til
hvad I kan tage med ud i gymnasieklasserne som del af det her
"Gymnasie Task Force". Formatet bliver formentlig at I tager ud på et
gymnasie og er 2 x 45 min i hver klasse (helst flere klasser på en
dag, parallelt eller sekventielt). Idéen er vist at DIKU kommer til at
have to-tre "pakker" gymnasielærerne kan vælge imellem. Lige nu er det
ikke helt fastlagt hvad de forskellige pakker skal være, vi er stadig
i idé-fasen.


Vores forslag til sådan en "pakke" omhandler kreativitet og
visualisering. Det kommer til primært til at være "hands-on" for
eleverne, med en del programmering. Vi forventer som minimum at de
skal kunne simpel trigonometri og geometri.

I de første 45 minutter sætter vi dem i gang med at skrive meget
simple programmer der kan tegne nogle figurer (firkanter, cirkler,
linjer). Forhåbentlig kan de nå at programmere sig frem til nogle små
animationer og bruge lidt af deres egen kreativitet.

I de næste 45 minutter skal de se at det ikke bare er sjov og ballade.
En idé er skitseret nedenfor med Monte Carlo simulering til at finde
π, samt eksempler på andre anvendelser af Monte Carlo simulering.  Det
kunne også være at simulere en hoppende bold (Breakout for dem der har
det let?), hvor de kan bruge noget fra fysik-undervisningen eller
måske noget helt andet...

Håbet er at de efter vi har været os selv kan gå videre, med noget af
det online materiale der er.

Stil endelig spørgsmål!

Mvh. Troels og Martin



Processing
----------
Processing er et Java (og JavaScript) bibliotek til at programmering
af visualiseringer. Man kan relativt hurtigt kan komme i gang med at
programmere og lave simple animationer. Vi har valgt Processing, da
der er så meget let tilgængeligt online materiale at de interesserede
elever kan fortsætte på egen hånd efter I har været på besøg.

Eksempel på hvad I kan give af introduktion ude i klassen:
  http://vimeo.com/channels/688713

Online-materiale
----------------
Online editor: https://www.khanacademy.org/cs/new/pjs
Editoren bruger JavaScript-udgaven af Processing ("Processing.js").

Alene eller hele klassen kan fortsætte her:

 * Fysik: http://natureofcode.com/

 * Kunst: http://www.generative-gestaltung.de/code
          http://www.openprocessing.org/classroom/1640

 * Spil: https://www.khanacademy.org/computing/cs/programming-games-visualizations

Moduler (forslag)
-----------------
Første modul (45 min.):
  * Basal brug af Processing
      - Tegne figurer
      - Benytte farver
      - Simple animationer
  * Tid til fri leg, sjov og ballade
  * Efter de første 45 min er håbet at de kan lave noget i denne stil:
    https://www.khanacademy.org/cs/bounce/6695477938749440
      eller måske:
    https://www.khanacademy.org/cs/roterende-cirkler/5236043496554496

Andet modul (45 min.):

 * Målet er at de skal se hvordan man kan bruge tilfældighed til at
   simulere sig frem til en løsning på et problem. 

   Et simpelt eksempel er en metode til at finde π.  Her er en
   forklaring:
   http://vishnumenon.com/2013/03/29/monte-carlo-pi-and-processingjs/

   Aktivitet:
     * Vi lader dem beregne π ved at kaste riskorn ud på en kvadratisk
       plade og tælle sig frem.

     * Bagefter udleverer vi en skabelon til et program, der gør det
       de lige har gjort med riskorn, men hvor de skal tilføje lidt
       for at få det til at virke

     * Eksempel implementation:
       https://www.khanacademy.org/cs/pi/6117540168466432

 * Til sidst vises eksempler på brug af samme teknik i andre fag
   f.eks. meteorologi, simulering af gasarter (kemi), smitte spredning
   i en befolkning (biologi), protein foldning (biologi), simulering
   af dannelsen af bilkøer, simulering af aktiekurser m.m.

   Troels og jeg programmerer nogle simple Processing-eksempler I kan
   vise frem.  Vi skal nok sætte jer grundigt ind i det hele!!
