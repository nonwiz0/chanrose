const video = document.querySelector('.player');
const canvas = document.querySelector('.photo');
const ctx = canvas.getContext('2d');
const strip = document.querySelector('.strip');
const snap = document.querySelector('.snap');

function getVideo() {
  navigator.mediaDevices.getUserMedia({video: true, audio: false})
    .then(localMediaStream => {
      console.log(localMediaStream);
      video.srcObject = localMediaStream;
      video.play();
    })
    .catch(error => {
      console.log(error);
    })
};

function redEffect(pixels) {
  console.log(pixels, "red effect", pixels.data);
  for (let i = 0; i < pixels.data.length; i+=4) {
    pixels.data[i + 0] += 200;
    pixels.data[i + 1] -= 50;
    pixels.data[i + 2] *= 0.5;
  }
  return pixels;
}
function greenEffect(pixels) {
  console.log(pixels, "red effect", pixels.data);
  for (let i = 0; i < pixels.data.length; i+=4) {
    pixels.data[i + 0] -= 50;
    pixels.data[i + 1] += 150;
    pixels.data[i + 2] *= 0.8;
  }
  return pixels;
}

function randomEffect(pixels) {
  console.log(pixels, "red effect", pixels.data);
  for (let i = 0; i < pixels.data.length; i+=4) {
    pixels.data[i + 0] -= Math.random() * Math.random();
    pixels.data[i + 1] += Math.random() * Math.random();
    pixels.data[i + 2] *= Math.random() * Math.random();
  }
  return pixels;
}


function paintToCanvas() {
  const [width, height] = [video.videoWidth, video.videoHeight];
  [canvas.width, canvas.height] = [width, height];
  [video.width, video.height] = ["300", "300"]
  console.log("paint");

  return setInterval(() => {
    ctx.drawImage(video, 0, 0, width, height);
    let pixels = ctx.getImageData(0, 0, width, height);
    let filter = document.querySelector("#filter");
    if (filter.value == "Red")
      pixels = redEffect(pixels);
    else if (filter.value == 'Green')
      pixels = greenEffect(pixels);
    else
      pixels = randomEffect(pixels);
    ctx.putImageData(pixels, 0, 0);
  }, 500);

}

function takePhoto() {
  snap.currentTime = 0;
  snap.play();

  const data = canvas.toDataURL('image/jpeg');
  const link = document.createElement('a');
  link.href = data;
  link.setAttribute('download', '001');
  link.innerHTML = `<img src="${data}" alt="handsomeboi" class="thumb" />`;
  strip.insertBefore(link, strip.firstChild);

}

getVideo();

video.addEventListener('canplay', paintToCanvas)

