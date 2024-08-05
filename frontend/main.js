let items = [{ id: "1", title: "Cooking", priority: 0 },
{ id: "2", title: "Reading", priority: 0 },
{ id: "3", title: "Studying", priority: 0 },
{ id: "4", title: "Walking", priority: 0 },
{ id: "5", title: "Dancing", priority: 0 }];

let ul = document.getElementById("itemsList");

let currentlyHighlighted = null;
let draggedItem = null;

for (let i = 0; i < items.length; i++) {
    let li = document.createElement("li");
    li.textContent = items[i].title;
    li.setAttribute('draggable', 'true');

    li.addEventListener("click", handleItemClick);
    li.addEventListener('dragstart', handleDragStart);
    li.addEventListener('dragover', handleDragOver);
    li.addEventListener('dragend', handleDragEnd);

    ul.appendChild(li);
}

document.getElementById('orderButton').addEventListener('click', function () {
    document.getElementById('overlay').style.display = 'block';
});

document.getElementById('overlay').addEventListener('click', function (event) {
    if (event.target === this) {
        this.style.display = 'none';
    }
});

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

function handleDragStart(event) {
    draggedItem = event.target;
    event.target.classList.add('dragging');
    event.dataTransfer.effectAllowed = 'move';
    event.dataTransfer.setData('text/html', event.target.innerHTML);

    let img = new Image();
    img.src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAwAB/gnq0zIAAAAASUVORK5CYII=';
    event.dataTransfer.setDragImage(img, 0, 0);
}

function handleDragOver(event) {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';

    const draggingOver = event.target;
    if (draggingOver && draggingOver.nodeName === "LI" && draggingOver !== draggedItem) {
        const bounding = draggingOver.getBoundingClientRect();
        const offset = bounding.y + (bounding.height / 2);

        if (event.clientY - offset > 0) {
            draggingOver.parentNode.insertBefore(draggedItem, draggingOver.nextSibling);
        } else {
            draggingOver.parentNode.insertBefore(draggedItem, draggingOver);
        }
    }
    return false;
}

function handleDragEnd(event) {
    let items = document.querySelectorAll('li');
    items.forEach(function (item) {
        item.classList.remove('dragging');
    });
}