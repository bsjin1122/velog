<h2 id="상황">상황</h2>
<p>깜박하고 이메일인증 브랜치에서 작업해야할 것을 ... 안 바꾸고 회원가입 브랜치에서 작업을 해버렸다...</p>
<h2 id="해결">해결</h2>
<pre><code class="language-shell">git stash
git checkout [올바른 브랜치명]
git stash pop
git add .
git commit -m &quot;적절한 커밋 메시지&quot;</code></pre>
<p><strong>1. 현재 변경사항을 스태시(stash) 하기</strong></p>
<pre><code>git stash</code></pre><ul>
<li>현재 작업중인 내용을 안전하게 저장해야 합니다. </li>
<li>현재 변경사항을 임시로 저장할 수 있습니다.</li>
</ul>
<p><strong>2. 올바른 브랜치로 이동하기</strong></p>
<pre><code>git checkout [올바른 브랜치명]</code></pre><ul>
<li>변경 사항이 스태시에 안전하게 저장되었으므로, 원하는 브랜치로 이동할 수 있습니다.</li>
</ul>
<p><strong>3. 스태시된 작업 적용하기</strong></p>
<pre><code class="language-shell">git stash pop</code></pre>
<ul>
<li>올바른 브랜치로 이동한 후, 스태시된 변경 사항을 다시 워킹 디렉토리에 적용할 수 있습니다.</li>
</ul>
<p><strong>4. 변경사항 커밋하기</strong></p>
<pre><code class="language-shell">git add .
git commit -m &quot;적절한 커밋 메시지&quot;</code></pre>
<p><strong>5. 스태시를 복원하는 대신 브랜치를 새로 생성</strong></p>
<pre><code class="language-shell">git checkout -b [새로운 브랜치명]</code></pre>
<ul>
<li>새로운 브랜치로 이동한 상태에서, 작업을 계속할 수 있다.</li>
</ul>