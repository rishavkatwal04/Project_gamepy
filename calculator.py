<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Smart Calculator</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.min.js"></script>

<style>
:root {
  --bg: #fff1e6;
  --card: #ffffff;
  --primary: #ff8a65;
  --primary-dark: #f4511e;
  --accent: #ffd6c9;
  --text: #3a2c2c;
  --muted: #7a6b6b;
}

.dark {
  --bg: #1e1b18;
  --card: #2a2521;
  --primary: #ffab91;
  --primary-dark: #ff8a65;
  --accent: #3a2f2a;
  --text: #f3edea;
  --muted: #bdb2ac;
}

body {
  margin: 0;
  min-height: 100vh;
  font-family: system-ui, sans-serif;
  background: linear-gradient(135deg, var(--bg), var(--accent));
  display: flex;
  justify-content: center;
  align-items: center;
  transition: 0.3s;
}

.calculator {
  width: 100%;
  max-width: 380px;
  background: var(--card);
  padding: 22px;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
  display: grid;
  gap: 14px;
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from {opacity:0; transform: translateY(20px);}
  to {opacity:1; transform: translateY(0);}
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

h1 {
  font-size: 20px;
  margin: 0;
  color: var(--primary-dark);
}

.toggle {
  cursor: pointer;
  font-size: 18px;
}

input {
  padding: 12px;
  font-size: 16px;
  border-radius: 12px;
  border: 1px solid var(--accent);
  background: transparent;
  color: var(--text);
}

.result {
  padding: 14px;
  background: var(--accent);
  border-radius: 12px;
  font-weight: 600;
  min-height: 32px;
}

.error {
  color: #ff5252;
}

.keypad {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.keypad button {
  padding: 14px;
  border-radius: 12px;
  border: none;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  background: var(--accent);
  color: var(--text);
  transition: 0.15s;
}

.keypad button:hover {
  transform: translateY(-2px);
}

.keypad .op {
  background: var(--primary);
  color: white;
}

.keypad .equal {
  grid-column: span 2;
  background: var(--primary-dark);
  color: white;
}

.history {
  max-height: 120px;
  overflow-y: auto;
  font-size: 13px;
  color: var(--muted);
}

.history-item {
  padding: 6px;
}
</style>
</head>

<body>
<div class="calculator">
  <header>
    <h1>Smart Calculator</h1>
    <div class="toggle" id="themeToggle">🌙</div>
  </header>

  <input id="expr" placeholder="Enter your expression here">
  <div id="out" class="result">Result will appear here</div>

  <div class="keypad">
    <button onclick="add('7')">7</button>
    <button onclick="add('8')">8</button>
    <button onclick="add('9')">9</button>
    <button class="op" onclick="add('/')">÷</button>

    <button onclick="add('4')">4</button>
    <button onclick="add('5')">5</button>
    <button onclick="add('6')">6</button>
    <button class="op" onclick="add('*')">×</button>

    <button onclick="add('1')">1</button>
    <button onclick="add('2')">2</button>
    <button onclick="add('3')">3</button>
    <button class="op" onclick="add('-')">−</button>

    <button onclick="add('0')">0</button>
    <button onclick="add('.')">.</button>
    <button onclick="add('ans')">ANS</button>
    <button class="op" onclick="add('+')">+</button>

    <button onclick="clearAll()">C</button>
    <button class="equal" onclick="evaluateInput()">=</button>
  </div>

  <div class="history" id="history"></div>
</div>

<script>
let lastResult = 0;

const exprEl = document.getElementById("expr");
const outEl = document.getElementById("out");
const historyEl = document.getElementById("history");

function add(v) {
  exprEl.value += v;
}

function clearAll() {
  exprEl.value = "";
  outEl.textContent = "Result will appear here";
  outEl.classList.remove("error");
}

function preprocess(exp) {
  exp = exp.toLowerCase().replace(/\s+/g,'');
  exp = exp.replace(/(\d)\(/g,'$1*(')
           .replace(/\)(\d)/g,')*$1')
           .replace(/\)\(/g,')*(')
           .replace(/ans/g, lastResult < 0 ? `(${lastResult})` : lastResult);
  return exp;
}

function evaluateInput() {
  try {
    const clean = preprocess(exprEl.value);
    const result = math.evaluate(clean);
    lastResult = result;
    outEl.textContent = "Result: " + result;
    outEl.classList.remove("error");

    const div = document.createElement("div");
    div.className = "history-item";
    div.textContent = exprEl.value + " → " + result;
    historyEl.prepend(div);
  } catch {
    outEl.textContent = "Error";
    outEl.classList.add("error");
  }
}

document.getElementById("themeToggle").onclick = () => {
  document.body.classList.toggle("dark");
};
</script>
</body>
</html>
