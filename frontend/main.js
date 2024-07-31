let items = ["Cooking", "Studying", "Reading", "Walking", "Dancing"];
let ul = document.getElementById("itemsList");
let currentlyHighlighted = null;
for (let i = 0; i < items.length; i++) {
    let li = document.createElement("li");
    li.textContent = items[i];
    li.addEventListener("click", handleItemClick);
    ul.appendChild(li);
}

function handleItemClick(event) {
    let li = event.target;
    if (li === currentlyHighlighted) {
        li.classList.remove("highlighted");
        currentlyHighlighted = null;
    } else {
        if (currentlyHighlighted) {
            currentlyHighlighted.classList.remove("highlighted");
        }
        li.classList.add("highlighted");
        currentlyHighlighted = li;
    }
}