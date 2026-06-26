const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const COLS = 18;
const ROWS = 18;
const CELL = canvas.width / COLS;

let snake = [{ x: 9, y: 9 }];
let direction = "right";

let food = { 
    x: Math.floor(Math.random() * COLS), 
    y: Math.floor(Math.random() * ROWS) 
};

let score = 0;
const scoreEl = document.getElementById("score");

document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowUp" && direction !== "down") direction = "up";
    else if (e.key === "ArrowDown" && direction !== "up") direction = "down";
    else if (e.key === "ArrowLeft" && direction !== "right") direction = "left";
    else if (e.key === "ArrowRight" && direction !== "left") direction = "right";
});

function update() {
    let head = { ...snake[0] };

    if (direction === "up") head.y--;
    if (direction === "down") head.y++;
    if (direction === "left") head.x--;
    if (direction === "right") head.x++;

    snake.unshift(head);

    if (head.x < 0 || head.x >= COLS || head.y < 0 || head.y >= ROWS) {
        alert("Game Over! discord.gg/aisypub");
        location.reload();
        return;
    }

    for (let i = 1; i < snake.length; i++) {
        if (head.x === snake[i].x && head.y === snake[i].y) {
            alert("Game Over! discord.gg/aisypub");
            location.reload();
            return;
        }
    }

    if (head.x === food.x && head.y === food.y) {
        food = {
            x: Math.floor(Math.random() * COLS),
            y: Math.floor(Math.random() * ROWS)
        };
        score++;
        scoreEl.textContent = score;
    } else {
        snake.pop();
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawGrid();

    ctx.fillStyle = "green";
    snake.forEach(part => {
        ctx.fillRect(part.x * CELL, part.y * CELL, CELL, CELL);
    });

    ctx.fillStyle = "red";
    ctx.fillRect(food.x * CELL, food.y * CELL, CELL, CELL);
}

function drawGrid() {
    ctx.strokeStyle = "#333";
    ctx.lineWidth = 0.5;

    for (let x = 0; x <= COLS; x++) {
        ctx.beginPath();
        ctx.moveTo(x * CELL, 0);
        ctx.lineTo(x * CELL, canvas.height);
        ctx.stroke();
    }

    for (let y = 0; y <= ROWS; y++) {
        ctx.beginPath();
        ctx.moveTo(0, y * CELL);
        ctx.lineTo(canvas.width, y * CELL);
        ctx.stroke();
    }
}

drawGrid();

function gameLoop() {
    update();
    draw();
}

setInterval(gameLoop, 150);