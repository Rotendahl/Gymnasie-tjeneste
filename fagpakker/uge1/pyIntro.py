

# Dette er en kommentar som python ikke ser.

""" Dette er en kommentar, der kan strække sig over flere linjer
    Hvor vildt! """

# hvis vi gerne vil se resultatet af en udregning sætter vi "print" foran


# I python kan man nemt lave udregninger.
print 2 + 2
print 10 / 2
print 1.1 * 9

# Hvis vi gerne vil gemme vores udregninger gøres det sålede
hilsen = "Hej med jer"
tal1   = 2 + 2
tal2   = 10 / 2
tal3   = 1.1 * 9

# Vi kan så bruge vores gemte tal.
print tal4 = tal1 * tal3 / tal2


# Hvis man vil styre hvad der skal ske kan det gøres med "if" udtryk
if(tal1 < tal2):
    print "Tal 1 er mindre end tal 2"
else:
    print "Tal 1 er større eller lig med tal 2"


# Hvis vi vil gentage noget et bestemt antal gange kan vi bruge en "for" løkke
# Erstat "n" med antal gange det skal køres.

for i in range(0,n):
    # Her skal den kode som skal gentages skrives

    # Her printes antal gange løkken har kørt. 
    print "Jeg har kørt: " + str(i) + " gange"
