// https://www.khanacademy.org/cs/urskive/5702161407410176
// 
// Idéer til akvititeter
//
//  * Vi udleverer et skelet hvor tegnViser er tom og hvor sekundArm,
//    minutArm, timeArm er læst fast til et tidspunkt, f.eks. 17:30:35
//    og de skal så skrive tegnViser
//
//  * Derefter skal de skrive udtrykkene til at beregne sekundArm,
//    minutArm, timeArm.

strokeWeight(3);

// Centrum af tegningen
var xCentrum = width / 2;
var yCentrum = height / 2;

// Radius på urskiven
var radius = min(xCentrum, yCentrum);

// Længder på viserne som procentdel af radius
var timeLaengde   = radius * 0.5;
var minutLaengde  = radius * 0.8;
var sekundLaengde = radius * 0.9;

var tegnViser = function(rotation, laengde) {
    // Udregn spidsen af viseren
    var xSpids = xCentrum + cos(rotation * 360 - 90) * laengde;
    var ySpids = xCentrum + sin(rotation * 360 - 90) * laengde;
    
    line(xCentrum, yCentrum, xSpids, ySpids);
};

draw = function() {
    background(255,255,255);
    ellipse(xCentrum, yCentrum, 2 * radius , 2 * radius);
    
    // Hvor mange procent af et minut er der gået?
    var sekundArm = second() / 60;

    // Hvor mange procent af en time er der gået?
    var minutArm = minute() / 60 +
                   second() / (60 * 60);

    // Hvor mange procent af et halvt døgn er gået?
    var timeArm = (hour() % 12) / 12 +
                  minute() / (12 * 60);

    // Tegn visere
    tegnViser(sekundArm, sekundLaengde);
    tegnViser(minutArm, minutLaengde);
    tegnViser(timeArm, timeLaengde);
};
