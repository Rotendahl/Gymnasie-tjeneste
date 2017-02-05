
# Opgave om kombinatorik
## Spørgsmål
Et CPR-nummer er som bekendt af formen DDMMÅÅ-XXXX, hvor XXXX er et løbenummer.
En kontrolsum gør, at kun ca. 5,4% af løbenumrene er gyldige.
Hvor mange CPR-numre kan der findes i alt?
    a) ca.   5.500.000.
    b) ca.  20.000.000.
    c) ca.  55.000.000.
    d) ca, 365.000.000.

## Svar
Der er ca. 365*100 mulige datoer og 5,4% lovlige løbenumre blandt 10.000 mulige.
Det giver i alt 365*100*10.000*0,054 = 19710000.
-------


# Dataformater og kunne størrelsesordener.

## Spørgsmål
En journalist er kommet i tvivl om hvorvidt flodheste nogle gange er kødædende.
Hvilken af følgende (sande) oplysninger kunne afgøre spørgsmålet?
a) Der er ingen vilde flodheste i Danmark.
b) Løver er bange for flodheste.
c) Flodheste i Zoologisk Have får kun grøntsager.
d) Man kan ride på en tam flodhest.
e) Flodheste har skarpe tænder.
f) Ingen af oplysningerne kan bruges.

## Svar
Ingen af de andre udsagn kan i sig selv afgøre hvorvidt flodheste er kødædende
(hvilket de faktisk bliver i tærkeperioder). En datalog skal kunne forstå
logiske sammenhænge og ræssonere på et rationelt grundlag.


## Spørgsmål
En app på din smartphone har adgang til det åbne internet, dine GPS-koordinater,
din acceleration og et kompas. Hvilken af følgende oplysninger kan app'en helt
sikkert ikke regne sig frem til?
a) Temperaturen udendørs.
b) Din nuværende hastighed.
c) Nummerpladen på den bil, du befinder dig i lige nu.
d) Din nuværende højde over havoverfladen.
e) Om du ofte kører på cykel.
f) Hvor langt du er fra Aarhus.

## Svar
Det er umuligt for en app på en telefon at vide, hvilken bil du konkret sidder
i på et givet tidspunkt, da ingen feature i telefonen registrerer dette og ingen
database på internettet registrerer dette i forhold til GPS koordinater.
Derimod kan a), b), d) og f) afgøres ud fra GPS koordinater og åbne databaser.
Selv e) kan faktisk estimeres meget præcist ved over en periode, at overvåge din
hastighed og dit bevægelsesmønster.
En datalog skal have en forståelse for, hvilke informationer der realistisk er
tilgængelige, og hvordan disse kan kombineres.

## Spørgsmål
Lagerplads på computere måles i de voksende enheder kilo, mega, giga og tera,
hvor man ganger med 1024 i hvert skridt. Nogle producenter "snyder" dog og
ganger kun med 1000. Hvad er den reelle forskel på 1 terabyte, hvis
producenterne snød mest muligt?
a) ca.    1%
b) ca.   10%
c) ca,  100%
d) ca, 1000%

## Svar
Hver tilfælde af snyd koster 1024/1000, og gentaget fire gange giver dette
9,95%.


## Spørgsmål
Hvad er en cookie?
a) En tilladelse til at en webserver hæver et bestemt beløb på din konto.
b) En ulovlig overvågning af din adfærd på nettet.
c) En almindelig møde at lave virusbekæmpelse på.
d) En oplysning som en webserver kan skrive og læse på din harddisk.
e) Et program, der kører i baggrunden på din computer.

## Svar
Svarene a), c) og e) er helt ude i skoven.  
Svaret b) er en mulig anvendelse af cookies, men ikke essensen af denne ofte
nyttige teknologi. En datalog skal have en intution om udbredt teknologi, selv
om alle tekniske detaljer selvfølgelig vil blive undervist på studiet. Men
tænk hvor mange gange, man som bruger har accepteret en cookie politik.


## Spørgsmål
Du er nået til bonusrunden i et gameshow på TV2. Hvilket af følgende tilbudte
slutspil bør du vælge, hvis du i gennemsnit gerne vil få den største bonus?
a) Du smider en mønt på gulvet og før 100 hvis den viser plat, ellers
   ingenting.
b) Du trækker et kort fra et almindeligt spil (52 kort) og får 300 kr hvis det
   er en hjerter, ellers ingenting.
c) Du smider to mønter på gulvet og får 300 kr hvis de lander med forskellige
   sider opad, ellers ingenting.
d) Du drejer et lykkehjul med tallenen fra 1 til 13 og får 1000 kr hvis den
   ender på det ene tal du valgte på forhånd, ellers ingenting.
e) Du slår med en terning og får 700 kr hvis det bliver en sekser, ellers
   ingenting.

## Svar
Den forventede bonus er i alle tilfælde beløbets størrelse ganget med
sandsynligheden for at vinde. For c) er der 4 mulige udfald, hvoraf de 2 giver
gevinst. Den forventede gevinst er derfor (2/4)*300 = 150 kr, hvilket slår alle
de andre spil. En datalog skal kunne overskue sandsynlighedsregning, blandt
andet til at kunne analysere randomiserede algoritmer.

## Spørgsmål
Information vil være fri, siger nogen, men er det altid klogt? Hvilken af
følgende oplysninger er den dummeste at offentliggøre på sin hjemmeside?
a) IP-adressen på den sidste person, der har besøgt din hjemmeside.
b) Nummeret på din bankkonto.
c) Adgangskoden til dit WiFi netværk.
d) De NemID kombinationer, som du allerede har brugt.
e) Datoen for din sidste Facebook opdatering.

## Svar
Utilsigtet adgang til dit WiFi netværk kan udnyttes til overvågning og
forfalskning. Alle de andre oplysninger er helt harmløse. En datalog skal kunne
overskue konsekvenserne af, hvordan information flyder rundt.

## Spørgsmål
Sproget ville nogle gange være lettere at forstå, hvis man brugte parenteser i
stedet for kommaer eller blot ingenting. Hvordan skulle parenteserne mest
rimeligt støttes i denne sætning:
Min bror skød en kanin med en gulerod der vejede 4 kg med en grøn hue på.
a) Min bror (skød (en kanin) (med en gulerod (der vejede 4 kg)) (med en grøn hue på))
b) Min bror (skød (en kanin (med en gulerod) (der vejede 4 kg (med en grøn hue på))))
c) Min bror (skød (en kanin (med en gulerod) (der vejede 4 kg))) (med en grøn hue på)
d) Min bror (skød (en kanin (med en gulerod (der vejede 4 kg)) (med en grøn hue på)))
De andre scenarier er lidt komiske.
En datalogi skal kunne se den strukturelle opbygning af komplicerede s�tninger, fx til forst�else af programmeringssprog.
9
Der er ca. 7 milliarder mennesker i verden. Med en passende antagelse om, hvor meget et st�ende menneske fylder, hvad er s� det mindste af f�lgende steder, hvor hele verdens befolkning rea�istisk kan st�?
6
d
a) R�dhuspladsen i K�benhavn (29,000 m2)
b) Langeland (284 km2)
c) Bornholm (589 km2)
d) Sj�lland (7,000 km2)
e) Island (100,000 km2)
f) Gr�nland (2,000,000 km2)
Vi antager 1 person/m2, hvilket er rigeligt. Bornholm kr�ver mere end 11 personer/m2, hvilket er helt urealistisk.
En datalog skal kunne udf�re back-of-the-envelope beregninger for at kunne estimere n�dvendige ressourcer.
10
Hvilken slags tal findes ikke?
5
c
a) Et lige primtal.
b) Et ulige kvadrattal.
c) Et primtal, der ogs� er et kvadrattal.
d) Et kvadrattal, der ogs� er et kubiktal.
e) Et kubiktal, der ogs� er et kvadrattal.
Et kvadrattal har sin kvadratrod som faktor, s� det kan ikke v�re et primtal.  Eksempler p� de andre tal er henholdsvis: 2, 49, 64, og 64.
En datalog skal v�re fortrolig med tal og matematisk tankegang.
11
En mand har to busstop uden for sit hus. Den ene bus k�rer til Fakta og den anden k�rer til Netto. Begge busser kommer altid pr�cis, og de har forskellige minuttal. Manden g�r ud p� indk�b hver dag p� et tilf�ldigt tidspunkt og tager den f�rste bus der kommer. Hvad kan ikke ske?
4
d
a) Han kommer oftere til Netto end til Fakta.
b) Han kommer oftere til Fakta end til Netto.
c) Han kommer lige tit til Fakta og Netto.
d) Han kommer aldrig til Netto.
S� l�nge busserne har forskellige minuttal, vil der altid v�re et vindue, hvor han kommer til Netto. De andre tilf�lde opst�r ved forskellige kombinationer af k�replaner.
En datalog skal kunne foretage en logisk modellering og analyse af komplicerede problemstillinger.
12
En kvinde g�r til bageren og ser, at der er ventetid ved de to kasser, der har hver sin k�. Hun stiller sig op i den korteste k�. Vi antager, at en ekspedition bed kassen kan tage vilk�rlig (men ikke uendelig) lang tid. Hvad kan der ikke ske, hvis bageren i stedet havde en f�lles k� til de to kasser?
4
c
a) Hun f�r en l�ngere ventetid.
b) Hun f�r en kortere ventetid.
c) Alle skal vente l�ngere.
d) Ingen skal vente l�ngere.
Afh�ngigt af l�ngderne af de to k�er og de enkeltes ekspeditionstider, s� kan de tre andre tilf�lde opst�.
En datalog skal kunne analysere de mulige udfald af et givet scenarie. K�er er specielt interessante at forst�, for at kunne forudsige svartider i komplekse systemer.
13
Som bekendt er n! produktet af tallene fra n ned til 1, Fx er 4! = 4*3*2*1 = 24.  Hvad er det 13nde sidste ciffer i tallet 100!?
10
a
a) 0.
b) 1.
c) 2.
d) 3.
e) 4.
f) 5.
g) 6.
h) 7.
i) 8.
j) 9.
Tallet 100! er produktet af 9 tal, der slutter p� "0", og mange par af tal, der slutter p� henholdsvis 2" og "5". Resultatet af dette giver mange nuller sidst i tallet.
En datalog skal v�re fortrolig med tal og kunne finde logiske genveje til korrekte svar.
14
Du er logget ind som kunde i en webshop og putter ting i din indk�bskurv. Efter hvilke af disse h�ndelser vil din indk�bskurv i bedste fald v�re intakt, n�r du igen logger ind p� webshoppen?
5
d
a) Du lukker pludselig din browser.
b) Du slukker pludselig din computer.
c) Du br�nder pludselig din computer.
d) Alle h�ndelserne kan efterlade indk�bskurven intakt.
e) Ingen af h�ndelserne kan efterlade indk�bskurven intakt.
indk�bskurven gemmes p� serveren og er bundet op til brugernavnet.
En datalog skal kunne overskue placeringen af data og konsekvenserne af dette.
15
Du sidder i et IC3-tog og snakker tankel�st i mobiltelefon om dit Dankort.  Hvilken af f�lgende udtalelser afsl�rer mest om din pinkode til en der tilf�ldigt overh�rer samtalen?
6
c
a) Den indeholder ikke to ens cifre.
b) Den er ogs� min kats f�dselsdag (DDMM).
c) Den er et kvadrattal.
d) Den er det samme som p� mit MasterCard.
e) Den indeholder ingen lige cifre.
f) Ingen af udtalelserne afsl�rer noget om min pinkodes
Kun 100 kvadrattal er mindre end 10.000. For de andre svar er antallet af mulige pinkoder henholdsvis: 5.040 (10*9*8*7), 366 (med skuddag), 9.999, og 625 (5*5*5*5).
En datalog skal v�re fortrolig med tal og kunne beherske simpel kombinatorik.
16
En kvinde pakker en r�d, gr�n og bl� kuffert. Hun putter et par r�de h�jh�lede sko i den gr�nne kuffert, en gul bluse i den r�de, en h�rt�rrer i den bl�, to par gr�nne sokker i den r�de, et par flade sko i den bl�, et kr�llejern i den gr�nne, et par gule st�vler i den r�de, og en bl� sweater i den bl�. S� bytter hun rundt p� de to elektriske apparater, flytter de h�jh�lede sko til den samme kuffert som den bl� sweater og smider alle gule ting ud. Hvad er der nu i den gr�nne kuffert?
5
b
a) To par gr�nne sokker.
b) En h�rt�rrer.
c) Et kr�llejern og et par flade sko.
d) En bl� sweater og et par h�jh�lede sko.
e) Ingenting.

En datalog skal kunne opbygge og vedligeholde en mental model af et systems tilstand.
17
Vi vil gerne udtrykke, at der findes flagermus i visse klokket�rne.  Hvilken af f�lgende s�tninger siger netop dette?
6
f
a) Der er n�dvendigvis ikke flagermus i alle klokket�rne.
b) Der er ikke n�dvendigvis flagermus i nogen klokket�rne.
c) Der er n�dvendigvis flagermus i alle klokket�rne.
d) Der er n�dvendigvis ikke flagermus i nogen klokket�rne.
e) Der er ikke n�dvendigvis flagermus i alle klokket�rne.
f) Der er n�dvendigvis flagermus i nogle klokket�rne.
De andre svar betyder alle (subtilt) forskellige ting.
En datalog skal kunne udtrykke sig pr�cist og have styr p� logiske kvantorer.
18
Befolkningen er bekymret over det farlige stof hypertrioxalklorat. Der blev udledt 86 ton i 2014 og 97 ton i 2015. Heldigvis oplyser Milj�ministeriet, at v�ksten i udledningen vil falde i b�de 2016 og 2017. Hvis vi regner i hele ton, hvad er s� den maksimale udledning i 2017?
8
f
a) 86 ton.
b) 87 ton.
c) 95 ton.
d) 96 ton.
e) 97 ton.
f) 116 ton.
g) 149 ton.
h) Det kan v�re hvad som helst.
V�ksten i udledningen var fra 2014 til 2015 11 tons. Hvis stigningen i udledningen falder de n�ste to �r, s� kan den maksimalt v�re henholdvis 10 og 9 ton. S� i 2017 kan der udledes 97+10+9=116 ton.
En datalog skal kende forskel p� en st�rrelse og �ndringen i st�rrelsen.
19
En familie med far, mor og to b�rn har farvede tallerkens�t i r�d, gul, gr�n og bl�.  Hvert s�t best�r af en stor, en mellem og en lille, og de bliver alle tolv brugt til alle m�ltider. I forbindelse med opvasken t�rrer b�rnene af og stabler tallerknerne ovenp� hinanden i skabet efterh�nden som de bliver klar. Dog overholder de deres mors regel om, at tallerknerne skal stables i st�rrelsesorden. Hvilken af f�lgende r�kkef�lger af fire tallerkner oven p� hinanden kan aldrig optr�de i stablen?
5
b
a) R�d bl�, r�d, bl�.
b) Stor, mellem, r�d, lille.
c) Mellem, bl�, r�d, lille.
d) Gul, stor, mellem, gul.
e) R�d, gul, gr�n, bl�.
Der skal v�re mindst 4 tallerkner mellem en stor og en lille.
En datalog skal kunne opbygge og analysere en mental model.
20
Til et party ankommer 10 �gtepar. Alle giver h�nd til hinanden, undtagen �gtef�ller indbyrdes. Hvor mange h�ndtryk bliver der givet i alt?
5
c
a) 100.
b) 150.
c) 180.
d) 190.
e) 400.
Der er 20 menensker, hvilket giver 20*19/2=190 h�ndtryk, da man ikke giver sig selv h�nden og h�ndtryk t�ller begge veje. Herfra skal man tr�kke de 10 h�ndtryk mellem �gtef�ller, s� svaret bliver 180.
En datalog skal kunne forst� simpel kombinatorik.
21
Hvem kan din mosters fars barnebarn ikke v�re?
6
b
a) Din s�ster.
b) Din onkel.
c) Dig selv.
d) Din bror.
e) Din f�tter.
f) Din kusine.
Personen er i samme lag i sl�gtstr�et som dig.
En datalog skal kunne overskue og navigere rundt i en tr�struktur, som fx et sl�gtstr�.
22
Hvilket af f�lgende udtryk er det samme som (2x+2)-(4-2x^2)?
5
a
a) 2x^2+2x-2
b) 2x^2-2x+2
c) -2x^2+2x-2
d) 2x^2+2x-4.
e) -4x^2+3x+6

En datalog skal kunne mestre element�r algebra.
23
En telefons�lger har d�rlig samvittighed over at ringe og genere folk med tilbud. Han f�r hver morgen 100 telefonnumre, og efter reglerne skal han ringe til hver person op til 3 gange, hvis de endnu ikke har k�bt noget. P� grund af sin d�rlige samvittighed ringer han dog kun en enkelt gang til hver. Hvis sandsynligheden for at s�lge noget altid er 1%, hvor mange opkald slipper telefons�lgeren s� for at lave hver dag?
5
c
a) ca.  99.
b) ca. 149.
c) ca. 197.
d) ca. 199.
e) ca. 200.
Normalt skulle s�lgeren regne med at lave 100*0,99 = 99 opkald anden gang og 100*0,99*0.99 = 98,01 opkald tredje gang, s� i alt ca. 197 opkald.
En datalog skal kunne mestre element�r sandsynlighedsregning.
24
En kvinde skal finde det bedste par sko til en kjole. Hun har 113 par sko.  Hun tager to par sko af gangen ud af skabet og kasserer det d�rligste af dem, indtil der ikke er flere sko i skabet. Nu gentager hun processen med de par der overlevede, og bliver ved indtil  hun ender med det bedste par sko. Hvor mange sammenligninger kommer hun til at lave, inden det bedste par sko er fundet?
5
c
a)  63.
b)  92.
c) 112.
d) 113.
e) 223.
Hver sammenligning forkaster et enkelt par sko, s� 112 sammenligninger er n�dvendige.
En datalog skal kunne analysere algoritmers kompleksitet og have �je for logiske genveje.
