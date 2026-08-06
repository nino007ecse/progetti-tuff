const btn = document.getElementById('game-btn');
const instructions = document.getElementById('instructions');
const result = document.getElementById('result');

let startTime = 0;
let timeoutId = null;
let state = 'start';

btn.addEventListener('click', () => {
    if (state === 'start') {
        state = 'waiting';
        btn.className = 'ready';
        instructions.textContent = 'PRONTO... Aspetta il verde!';
        result.textContent = '';

        const randomDelay = Math.floor(Math.random() * 3000) + 2000;

        timeoutId = setTimeout(() => {
            state = 'go';
            btn.className = 'go';
            instructions.textContent = 'CLICCA ORA!';
            startTime = Date.now();
        }, randomDelay);

    } else if (state === 'waiting') {
        clearTimeout(timeoutId);
        state = 'start';
        btn.className = 'waiting';
        instructions.textContent = 'Troppo presto!';
        result.textContent = 'Clicca per riprovare.';

    } else if (state === 'go') {
        const reactionTime = Date.now() - startTime;
        state = 'start';
        btn.className = 'waiting';
        instructions.textContent = `${reactionTime} ms!`;
        result.textContent = 'Clicca per fare un altro tentativo.';
    }
});