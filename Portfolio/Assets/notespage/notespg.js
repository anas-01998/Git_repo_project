showNotes();
let addButton = document.getElementById("addBtn");
addButton.addEventListener("click", function (e) {
  let TextArea = document.getElementById("floatingTextarea");

  let notes = localStorage.getItem("notes");

  if (notes == null) {
    notesObj = []; // blank array
  }
  else { // I am going to be storing my notes in the array.
    notesObj = JSON.parse(notes);
  }
  notesObj.push(TextArea.value);

  // converting the notesObj to a string using the stringify method [below] as we can only work with strings in the local storage
  localStorage.setItem("notes", JSON.stringify(notesObj));

  TextArea.value = "";
  console.log(notesObj);
  showNotes();
});

// Following function to display the notes on the page
function showNotes() {
  let notes = localStorage.getItem("notes");
  if (notes == null) {
    notesObj = []; // blank array
  }
  else { // I am going to be storing my notes in the array.
    notesObj = JSON.parse(notes);
  }

  // this.id ==> this will send the element's ID on which it is clicked
  let html = "";
  notesObj.forEach(function (element, index) {
    html += `
    <div class="card mx-2 my-2 noteCard" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Note ${index + 1}</h5>
          <p class="card-text">${element}</p>
          <button id="${index}" class="btn btn-primary" onclick="deleteNote(this.id)">Delete Note</butt>
        </div>
      </div>
    `
  });
  let notesElm = document.getElementById("notes");
  if (notesObj.length != 0) {
    notesElm.innerHTML = html;
  }
}
function deleteNote(index) {
  let notes = localStorage.getItem("notes");
  if (notes == null) {
    notesObj = []; // blank array
  }
  else {    // I am going to be storing my notes in the array.
    notesObj = JSON.parse(notes);
  }
  notesObj.splice(index, 1);

  localStorage.setItem("notes", JSON.stringify(notesObj));
  showNotes();
}

let search = document.getElementById("searchTxt");
search.addEventListener("input", function () {
  let inputVal = search.value;

  let noteCards = document.getElementsByClassName("noteCard");
  Array.from(noteCards).forEach(function (element) {
    let cardText = element.getElementsByTagName("p")[0].innerText;

    if (cardText.includes(inputVal)) {
      element.style.display = "block";
    }
    else {
      element.style.display = "none";
    }
  })
});
