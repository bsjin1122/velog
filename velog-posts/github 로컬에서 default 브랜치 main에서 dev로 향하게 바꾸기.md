<h2 id="상황">상황</h2>
<ul>
<li>초기에 main 브랜치로만 진행을 하다보니 브랜치명이 &quot;main&quot; 하나를 default로 잡아두었었다. (초기 명령어)</li>
<li>이후 dev를 default branch로 변경되었음에도 push를 하는데 origin/main 으로 계속 잡고 있어서 찾아보게 되었다.</li>
</ul>
<h2 id="해결">해결</h2>
<pre><code class="language-shell">git branch -m master main : 현재 브랜치 이름을 master에서 main으로 변경함
git fetch origin : 원격저장소 origin에서 최신 변경 사항을 가져옴
git branch -u origin/dev main 
: 로컬 main 브랜치를 원격 'origin/dev' 브랜치와 추적하도록 설정합니다.
git remote set-head origin -a: 원격 저장소 origin의 기본 브랜치를 자동으로 감지하고 설정합니다.</code></pre>
<blockquote>
<ul>
<li>git branch -m master main: 이부분은 할 필요가 없어서 안했다.</li>
</ul>
</blockquote>
<ul>
<li>git fetch origin </li>
<li>git branch -u origin/dev local: 로컬 브랜치를 &quot;local&quot;로 해뒀었다.</li>
<li>git remote set-head origin -a</li>
</ul>
<ul>
<li>이제 브랜치 기능별로 생성하고, 다시 dev에 올라가지겠지!!?</li>
</ul>
