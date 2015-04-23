// Example by Casey Reas and Ben Fry
// http://processingjs.org/learning/basic/distance2d/

frameRate(25);
size(640, 360); 
noStroke();
var max_distance = dist(0, 0, width, height);

draw = function () {
  background(51);

  for(int i = 0; i <= width; i += 20) {
    for(int j = 0; j <= height; j += 20) {
      size = dist(mouseX, mouseY, i, j);
      size = size/max_distance * 66;
      ellipse(i, j, size, size);
    }
  }
};
