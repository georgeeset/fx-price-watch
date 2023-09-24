
// Get the modal
var modal = document.getElementById("modalDialog");

// Get the button that opens the modal
var btn = document.getElementById("alertCard");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];



// Ger alert list items
var alerts = document.querySelectorAll("div.cardInfo");

function generateContent(mapData){
  // console.log(mapData);
  data = "";
  for (k in mapData){
    data = data.concat(`<div class="dataLine"><p class="titleColumn"> ${k.replace('_', ' ').toUpperCase()} :</p> <p>${mapData[k]}</p></div><hr>`);
  }
  // console.log(data);
  return data;
}

alerts.forEach((card) => {
  card.addEventListener('click', () =>{
    var dataItem = JSON.parse (card.dataset.item);
    var isActive = card.dataset.isactive;
    // console.log(dataItem);
    console.log(isActive);
    modalContent = generateContent(dataItem);

    modalContent=modalContent.concat(`<div class="cardAction">`);
    if (isActive == 'True'){
      modalContent = modalContent.concat(`
      <a class="btnDefault" href="/user/edit-alert/${card.id}" role="button">Edit</a>
      `);
    }

    modalContent = modalContent.concat(`
    <a class="btnAlarm" href="/user/delete-alert/${card.id}"role="button">Delete</a></div>
    `);

    document.getElementById("alertData").innerHTML = modalContent;
    modal.style.display= "block";
  });
});

// When the user clicks the button, open the modal 
// btn.onclick = function() {
//   modal.style.display = "block";
// }

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
