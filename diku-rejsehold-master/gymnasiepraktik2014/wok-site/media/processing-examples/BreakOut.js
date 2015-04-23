// Example by Martin Dybdal
// Inspiration: http://www.trsp.net/teaching/gamemod/

var Rectangle = function (x, y, w, h, color) {
  this.x = x;
  this.y = y;
  this.width = w;
  this.height = h;
  this.color = color;
  this.alive = true;
};
var drawRectangle = function(r) {
    fill(r.color);
    rect(r.x, r.y, r.width, r.height);
};

var collision = function(rect1, rect2) {
   return rect1.x < rect2.x + rect2.width &&
          rect1.x + rect1.width > rect2.x &&
          rect1.y < rect2.y + rect2.height &&
          rect1.height + rect1.y > rect2.y;
};

size(400,400);
stroke(0,0,0);

var frame = new Rectangle(0,0,width,height);
var ballSize = 5;
var ball = new Rectangle(width*random(), 150, ballSize, ballSize);
var ballVelX = 3;
var ballVelY = 3;

var paddleWidth = 60;
var paddleHeight = 5;
var paddle = new Rectangle(mouseX, 370, paddleWidth, paddleHeight);

var numberOfBricks = 60;
var bricksPerRow = 10;
var rowsColors = [0xffff00ff, 0xffff0000, 0xffff9900, 0xffffff00, 0xff00ff00, 0xff00ffff];
var brickHeight = 10;
var brickWidth = width/bricksPerRow;
var yBricks = 50;
var bricks = new Array (numberOfBricks);
for (var i = 0; i < numberOfBricks; i++) {
    var rowNum = Math.floor(i/bricksPerRow);
    // coords
    var x = brickWidth* (i % bricksPerRow);
    //x -= rowNum*bricksPerRow*brickWidth;
    var y = yBricks+(rowNum*brickHeight);
    // color
    var num = min(rowNum, rowsColors.length-1);
    var rowColor = rowsColors[num];
    bricks[i] = new Rectangle(x,y,brickWidth, brickHeight, rowColor);
}

var handleCollisions = function () {
  // Handle any collisions
  if(collision(ball, paddle)){
    ballVelY = - ballVelY;  
  }
  
  if(ball.x <= 0 || ball.x+ballSize >= width) {
      ballVelX = - ballVelX;
  }

  for(var i = 0; i < numberOfBricks; i++) {
     if(bricks[i].alive && collision(ball, bricks[i])) {
        ballVelY = - ballVelY;
        bricks[i].alive = false;
     }
  }
};

var drawEverything = function () {
  drawRectangle(paddle);
  drawRectangle(ball);
  for (var i = 0; i < numberOfBricks; i++) {
      if(bricks[i].alive) {
        drawRectangle(bricks[i]);  
      }
  }
};

var isMouseOver = false;
mouseOut = function() {
    isMouseOver = false;
};

mouseOver = function() {
     isMouseOver = true;
};

draw = function() {
  background(0,0,0);

  // Update position of paddle
  if(isMouseOver) {
     paddle.x = mouseX-paddle.width/2;
  } else {
     paddle.x = ball.x-paddleWidth/2;
  }

  // Update position of ball
  ball.x = ball.x + ballVelX;
  ball.y = ball.y + ballVelY;

  handleCollisions();
  
  drawEverything();
};
