<blockquote>
<p>출처: 그림으로 보는 오라클 구조</p>
</blockquote>
<h2 id="패치patch">패치(patch)</h2>
<ul>
<li>소프트웨어의 기능을 추가하거나, 버그 등을 수정하는 프로그램</li>
<li>오라클 12c R2 이후부터는 3개월마다 RU 및 RUR 두 가지 패치가 정기적으로 제공되고 있음(단, 윈도우 제외)</li>
</ul>
<h2 id="rurelease-update">RU(Release Update)</h2>
<ul>
<li>보안, 옵티마이저의 동작, 기능 추가에 관련된 수정 내용이 포함된다.</li>
<li>누적형 패치로서, 최신 릴리즈를 적용하면 모든 수정 내용을 적용할 수 있다.</li>
</ul>
<h2 id="rurrelease-update-revisions">RUR(Release Update Revisions)</h2>
<ul>
<li>RU를 적용한 환경에만 적용할 수 있는 수정 패치</li>
<li>같은 시기에 릴리즈된 RU와 비교해서 옵티마이저의 동작, 기능 추가의 수정은 포함되지 않음</li>
<li><code>보안이나 가벼운 버그 수정</code>만이 포함된다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/8d00ed75-a7b5-4339-99de-7ff6342d6174/image.png" /></p>
<ul>
<li><p>RU에 대응되는 RUR이 두 번째 분기까지 릴리즈된다. </p>
<ul>
<li>새로운 RU가 릴리즈되는 시점에 RU1에 RUR을 적용할 수도 있으며, 좀 더 많은 수정 사항이 포함된 RU2를 적용할 수도 있다.</li>
</ul>
<h2 id="interim-패치">Interim 패치</h2>
<ul>
<li>Oracle Database와 관련된 소프트웨어에서 특정 문제를 해결하기 위해 제공되는 <b>임시 패치</b><blockquote>
<ul>
<li>긴급한 버그 수정</li>
</ul>
</blockquote>
</li>
<li>정기 패치 이전의 문제 해결</li>
<li>개별적인 문제 해결</li>
</ul>
</li>
</ul>