<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>발야구 전략 웹앱</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body { font-family: 'Arial', sans-serif; text-align: center; background-color: #f0f8ff; }
    #field {
      position: relative;
      width: 100%;
      max-width: 800px;
      height: 500px;
      margin: auto;
      background: url('야구장배경.png') no-repeat center/cover;
      border: 2px solid #333;
    }
    .player, .ball {
      position: absolute;
      width: 50px; height: 50px;
      border-radius: 50%;
      line-height: 50px; text-align: center;
      font-size: 14px;
      font-weight: bold;
      cursor: move;
    }
    .teamA { background-color: #ff9999; }
    .teamB { background-color: #99ccff; }
    .ball { background-color: yellow; }
    #controls, #nameEditor, #scoreBoard { margin-top: 10px; }
    .tab { display: none; }
    .tab.active { display: block; }
    button, input, select { margin: 5px; padding: 10px; font-size: 14px; }
    @media (max-width: 600px) {
      .player, .ball { width: 40px; height: 40px; line-height: 40px; font-size: 12px; }
    }
  </style>
</head>
<body>
  <h1>발야구 전략 시뮬레이터</h1>

  <div id="controls">
    <button onclick="setMode('offense')">⚾ 공격 모드</button>
    <button onclick="setMode('defense')">🧤 수비 모드</button>
    <button onclick="applyDefenseStrategy()">🧩 기본 수비전략</button>
    <button onclick="toggleTab('rules')">📖 발야구 규칙 설명</button>
  </div>

  <div id="scoreBoard">
    <span>팀 A: <span id="scoreA">0</span></span>
    &nbsp;|&nbsp;
    <span>팀 B: <span id="scoreB">0</span></span>
    <button onclick="incrementScore('A')">A 점수 +1</button>
    <button onclick="incrementScore('B')">B 점수 +1</button>
  </div>

  <div id="field">
    <div class="player teamA" id="player1" style="top: 400px; left: 370px;">선수 1</div>
    <div class="player teamB" id="player2" style="top: 100px; left: 370px;">선수 2</div>
    <div class="ball" id="ball" style="top: 400px; left: 390px;">발야구 공</div>
  </div>

  <div id="nameEditor">
    <select id="playerSelect">
      <option value="player1">선수 1</option>
      <option value="player2">선수 2</option>
    </select>
    <input type="text" id="newName" placeholder="새 이름 입력">
    <button onclick="changePlayerName()">이름 변경</button>
  </div>

  <div id="rules" class="tab">
    <h2>발야구 규칙</h2>
    <ul id="ruleList">
      <li>1루, 2루, 3루, 홈이 있음</li>
      <li>공을 차면 달릴 수 있음</li>
    </ul>
    <input type="text" id="newRule" placeholder="새 규칙 입력">
    <button onclick="addRule()">추가</button>
    <button onclick="removeRule()">마지막 삭제</button>
  </div>

  <script>
    function setMode(mode) {
      alert(mode === 'offense' ? '⚾ 공격 모드로 전환합니다.' : '🧤 수비 모드로 전환합니다.');
    }

    function toggleTab(tabId) {
      const tab = document.getElementById(tabId);
      tab.classList.toggle('active');
    }

    function addRule() {
      const ruleText = document.getElementById('newRule').value;
      if (ruleText.trim()) {
        const li = document.createElement('li');
        li.textContent = ruleText;
        document.getElementById('ruleList').appendChild(li);
        document.getElementById('newRule').value = '';
      }
    }

    function removeRule() {
      const list = document.getElementById('ruleList');
      if (list.children.length > 0) {
        list.removeChild(list.lastChild);
      }
    }

    function incrementScore(team) {
      const scoreEl = document.getElementById('score' + team);
      let score = parseInt(scoreEl.textContent);
      scoreEl.textContent = score + 1;
    }

    function changePlayerName() {
      const selected = document.getElementById('playerSelect').value;
      const newName = document.getElementById('newName').value.trim();
      if (newName) {
        document.getElementById(selected).textContent = newName;
      }
    }

    function applyDefenseStrategy() {
      const defensePositions = [
        { id: 'player1', top: '350px', left: '200px' },
        { id: 'player2', top: '100px', left: '300px' }
      ];
      defensePositions.forEach(pos => {
        const el = document.getElementById(pos.id);
        if (el) {
          el.style.top = pos.top;
          el.style.left = pos.left;
        }
      });
    }

    document.querySelectorAll('.player, .ball').forEach(elem => {
      elem.onmousedown = function (e) {
        const el = e.target;
        const offsetX = e.clientX - el.offsetLeft;
        const offsetY = e.clientY - el.offsetTop;

        function moveHandler(e) {
          el.style.left = (e.clientX - offsetX) + 'px';
          el.style.top = (e.clientY - offsetY) + 'px';
        }

        function upHandler() {
          document.removeEventListener('mousemove', moveHandler);
          document.removeEventListener('mouseup', upHandler);
        }

        document.addEventListener('mousemove', moveHandler);
        document.addEventListener('mouseup', upHandler);
      };
    });
  </script>
</body>
</html>
