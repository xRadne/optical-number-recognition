

function sampleImage() {
  samples = [];
  imageSize = 420;
  var imageData = ctx.getImageData(0, 0, imageSize, imageSize);

  var index;
  for (let i = 0; i < 28; i++) {
    for (let j = 0; j < 28; j++) {
      index = (j * imageSize / 28 * 4) + (i * imageSize * imageSize / 28 * 4) + 3;
      samples.push(imageData.data[index] / 255);
    }
  }
  return samples;
}

//Classify
classifyButton = document.getElementById('classifyButton');

function classifyXHR(e) {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://127.0.0.1:5000/classify', true);

  xhr.onload = function () {
    answer.innerHTML = xhr.response;
  };

  testData = sampleImage();

  xhr.send(JSON.stringify(testData));
}

classifyButton.addEventListener('click', classifyXHR);

//clear
clearButton = document.getElementById('clearButton');
answer = document.getElementById('answerBox');

function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  answer.innerHTML = "";
}

clearButton.addEventListener('click', clearCanvas);

//submit data
var submitButton = document.getElementById('submit');
var labelInput = document.getElementById('label');

var submitMode = false;

function submit(e) {
  submitMode = !submitMode;
  if (submitMode) {
    submitButton.classList.add('active');
  }
  else {
    submitButton.classList.remove('active');
  }
}

submitButton.addEventListener('click', submit);

function storeDataXHR(e) {
  var label = labelInput.value;
  if (label == null) return;

  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://127.0.0.1:5000/data', true);

  xhr.onload = clearCanvas;

  data = {
    image: sampleImage(),
    label: Number(label)
  }

  xhr.send(JSON.stringify(data));
}