// Online på: https://www.khanacademy.org/cs/pi/6117540168466432
//
// Idéer til aktiviteter:
//
//  * Vi udleverer funktionen uden den del der tjekker om et punkt er
//    inde i cirklen og opdaterer hits/misses og beder dem skrive
//    betingelsen.
//
//  * Bed dem derefter tilføje så farven af punkterne ændrer sig
//  * baseret på om det er et hit eller miss.


// Radius
var r = 200;

// Tællere
var misses = 0;
var hits = 0;

strokeWeight(3);
noFill();
ellipse(r,r,2*r,2*r);

draw = function() {
    // Vælg et tilfældigt punkt i kvadratet
    var x = random(0,2*r);
    var y = random(0,2*r);
    
    // Er (x,y) inde i cirklen?
    if (sqrt(pow(x-r,2)+pow(y-r,2)) <= r) {
        hits++;
        stroke(0, 0, 0);
    }
    else {
        misses++;
        stroke(255, 0, 0);  
    }
    point(x,y);

    
    // Estimér pi ud fra antal hits i cirklen
    var pi_estimate = 4*(hits/(hits+misses));
    
    // Opdater tekst-felt
    noStroke();
    fill(255, 255, 255);
    rect(0,0,200,30);
    fill(0, 0, 0);
    text("pi estimat: " + pi_estimate, 10, 20);
};
