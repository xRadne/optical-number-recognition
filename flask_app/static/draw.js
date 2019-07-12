canvas = document.getElementById('canvas');
ctx = canvas.getContext('2d');
animationTimer = null;
drawing = false;
var x = 0;
var y = 0;

function startDrawing(e) {
  drawing = true;
  x = e.offsetX;
  y = e.offsetY;
}

function draw(e) {
  if (drawing) {
    drawLine(ctx, x, y, e.offsetX, e.offsetY);
    x = e.offsetX;
    y = e.offsetY;
  }
}

function stopDrawing(e) {
  drawLine(ctx, x, y, e.offsetX, e.offsetY);
  drawing = false;

  if (submitMode) {
    storeDataXHR();
  }
  else {
    animationTimer = AnimationTimer(
      updateColor,
      () => {
        updateColor(0);
        sendClassifyRequest();
      },
      2000,
      100);
  }
}

function drawLine(context, x1, y1, x2, y2) {
  context.beginPath();
  context.strokeStyle = 'black';
  context.lineWidth = 25;
  context.lineCap = 'round';
  context.moveTo(x1, y1);
  context.lineTo(x2, y2);
  context.stroke();
  context.closePath();
}

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);