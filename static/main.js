let items = [];

let choiceQueue = [];

let ul = document.getElementById("itemsList");

let currentlyHighlighted = null;
let draggedItem = null;

function registerEventListeners() {
    document.getElementById('darkModeToggle').addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');
        document.querySelector('.overlay-content').classList.toggle('dark-mode');
    });

    document.getElementById('orderButton').addEventListener('click', function () {
        document.getElementById('overlay').style.display = 'block';
        resetChoiceQueue(items);
        resetItemScores();
        setOverlayOptions();
    });

    document.getElementById('overlay').addEventListener('click', function (event) {
        if (event.target === this) {
            this.style.display = 'none';
        }
    });

    document.getElementById('leftHalf').addEventListener('click', function () {
        sideClicked('left');
    });

    document.getElementById('rightHalf').addEventListener('click', function () {
        sideClicked('right');
    });
}

document.addEventListener('DOMContentLoaded', async function () {
    try {
        const response = await fetch('/api/items/');
        const data = await response.json();
        items = data;
        displayItems();
    } catch (error) {
        console.error('Error fetching items:', error);
    }
    registerEventListeners();
});

function resetChoiceQueue(items) {
    choiceQueue = [];
    for (let i = 0; i < items.length; i++) {
        for (let j = i + 1; j < items.length; j++) {
            choiceQueue.push([items[i].id, items[j].id]);
        }
    }
}

function displayItems() {
    items.sort((a, b) => b.score - a.score);
    ul.innerHTML = "";
    for (let i = 0; i < items.length; i++) {
        let li = document.createElement("li");
        li.textContent = items[i].title;
        li.setAttribute('draggable', 'true');

        li.addEventListener('click', handleItemClick);
        li.addEventListener('dragstart', handleDragStart);
        li.addEventListener('dragover', handleDragOver);
        li.addEventListener('dragend', handleDragEnd);

        ul.appendChild(li);
    }
}

function resetItemScores() {
    items.forEach(x => {
        x.score = 0;
    });
}

function setOverlayOptions() {
    const choicePair = choiceQueue.pop();
    const leftItemId = choicePair[0];
    const rightItemId = choicePair[1];
    const leftItem = findItemById(leftItemId);
    const rightItem = findItemById(rightItemId);
    const leftHalf = document.getElementById('leftHalf');
    leftHalf.innerHTML = leftItem.title;
    leftHalf.setAttribute("itemId", leftItem.id);
    const rightHalf = document.getElementById('rightHalf');
    rightHalf.innerHTML = rightItem.title;
    rightHalf.setAttribute("itemId", rightItem.id);
    if (choiceQueue.length == 0) {
        document.getElementById('overlay').style.display = 'none';
        displayItems();
    }
}

function findItemById(id) {
    return items.find(item => item.id === id);
}

function sideClicked(side) {
    const leftHalf = document.getElementById('leftHalf');
    const rightHalf = document.getElementById('rightHalf');
    if (side == 'left') {
        const id = parseInt(leftHalf.getAttribute("itemId"));
        const item = findItemById(id);
        item.score += 1;
    } else {
        const id = parseInt(rightHalf.getAttribute("itemId"));
        const item = findItemById(id);
        item.score += 1;
    }

    setOverlayOptions();
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
