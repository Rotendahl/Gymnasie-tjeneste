// https://www.khanacademy.org/cs/accelererende-cirkler/4940971701960704
//
// Idéer til aktiviteter:
//
// * Vi udleverer et skelet hvor cirklerne bliver tegnet men ikke
//   roterer. Først skal de tilføje x-parameteren og på den måde ændre
//   vinklen I hver omgang.
//
// * Bag efter beder vi dem få x til at stige hurtigere og hurtigere,
//   for at skabe acceleration.
//
// * Hvorfor virker det som om vi accelererer op og ned og op og ned,
//   men ikke kun accelererer op?

// Valg af farver
strokeWeight(3);
stroke(57, 0, 214);
fill(0, 210, 247);

// Hvor ofte draw() funktionen kaldes
frameRate(60);

var x = 0;
var a = 0.1;

// Denne funktion kaldes automatisk
// hver gang billedet skal opdateres
draw = function() {
    
    // Ryd billedet ved starten af hver frame
    background(255, 255, 255);
    
    // Cirkel i punkt (200,200)
    ellipse(200, 200, 30, 30);
    
    // Fire roterende cirkler
    // Bemærk cos() og sin() tager antal grader og 
    // ikke radianer som argument
    for (var i = 0; i < 4; i++) {
      var angle = i*90+x*360/8;
      
      ellipse(200+50*cos(angle), 
              200+50*sin(angle),
              30, 30);
    }
    
    x += a;
    a += 0.001;
};
