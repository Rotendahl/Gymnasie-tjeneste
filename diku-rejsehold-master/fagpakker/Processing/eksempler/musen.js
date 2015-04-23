fill(168, 174, 255);
strokeWeight(3);
stroke(57, 71, 227);

draw = function() {
  background(255);
  line(0,0,mouseX,mouseY);
  line(width,height,mouseX,mouseY);
  line(0,height,mouseX,mouseY);
  line(width,0,mouseX,mouseY);
  ellipse(mouseX,mouseY, 30,30);
};
