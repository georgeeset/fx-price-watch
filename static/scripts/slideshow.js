const indexSlide = document.getElementById('slideShow')

const UPDATE_TIME_INTERVAL = 3000

//  Enter URLs of your own custom images
const imagesArray = [
  "/static/styles/imgs/slide1.png",
  "/static/styles/imgs/slide2.png",
  "/static/styles/imgs/slide3.png",
  "/static/styles/imgs/slide4.png",
]

let i = 0

setInterval(()=>{
  if(i == 3){
    i = 0
  }
  else {i = i + 1};
  console.log('i was run',i)
  indexSlide.src = imagesArray[i]
},UPDATE_TIME_INTERVAL)