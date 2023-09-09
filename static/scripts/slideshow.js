const indexSlide = document.getElementById('slideShow')

const UPDATE_TIME_INTERVAL = 3000

//  Enter URLs of your own custom images
const imagesArray = [
  "/static/styles/imgs/whatsapp-logo.png",
  "/static/styles/imgs/telegram-logo.png",
]

let i = 0

setInterval(()=>{
  if(i == 1){
    i = 0
  }
  else {i = i + 1};
  console.log('i was run',i)
  indexSlide.src = imagesArray[i]
},UPDATE_TIME_INTERVAL)