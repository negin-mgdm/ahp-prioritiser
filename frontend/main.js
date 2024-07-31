let items = ["Cooking", "Studying", "Reading", "Walking", "Dancing"];
let ul = document.getElementById("itemsList");
for (let i = 0; i < items.length; i++) {
    let li = document.createElement("li");
    li.textContent = items[i];
    ul.appendChild(li);
}