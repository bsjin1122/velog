<h1 id="bind-peeking">Bind Peeking</h1>
<ul>
<li>Oracle 데이터베이스에서 SQL 문장이 실행될 때 바인드 변수의 실제(바인드 값)을 참조(peek)하여 최적화된 실행 계획을 생성하는 기능</li>
</ul>
<h2 id="동작-원리">동작 원리</h2>
<ol>
<li>SQL문이 처음 실행될 때 </li>
</ol>
<ul>
<li>Oracle 옵티마이저는 바인드 변수에 전달된 실제 값을 확인(peek)</li>
<li>이 값을 기준으로 통계 정보를 활용하여 최적의 실행 계획 생성 </li>
</ul>
<ol start="2">
<li>실행 계획 재사용</li>
</ol>
<ul>
<li>이후 동일한 SQL문이 실행될 때는 첫 번째 실행 시 생성된 실행 계획이 그대로 재사용된다.</li>
<li>바인드 변수에 다른 값이 입력되어도 기존 실행 계획이 적용</li>
</ul>
<h2 id="bind-peeking의-문제점">Bind Peeking의 문제점</h2>
<ul>
<li>바인드 변수 값에 따라 최적의 실행 계획이 달라질 수 있음에도 불구, 첫 번째 실행 시 생성된 실행 계획이 모든 값에 재사용된다.
편향된 실행 계획
성능 저하
ex) :dept_id가 10일 때, 인덱스 스캔이 최적이지만 50일 때는 풀 테이블 스캔이 유리함에도 불구하고 인덱스 스캔 실행 계획이 재사용됨.</li>
</ul>
<h2 id="bind-peeking-문제-해결-방법">Bind Peeking 문제 해결 방법</h2>
<ol>
<li>Adaptive Cursor Sharing</li>
</ol>
<ul>
<li>Oracle 11g부터 도입된 기능으로, 실행 계획이 바인드 변수 값에 따라 적합하지 않으면 다른 실행 계획을 생성하도록 조정한다.</li>
</ul>
<ol start="2">
<li>SQL Plan Baseline</li>
</ol>
<ul>
<li>실행 계획을 고정하거나, 최적의 계획을 유지하여 일관된 성능을 보장한다.</li>
</ul>
<ol start="3">
<li>히스토그램 사용</li>
</ol>
<ul>
<li>데이터 분포가 비대칭인 경우, 히스토그램을 사용하면 옵티마이저가 데이터 분포를 정확히 파악하여 실행 계획을 개선</li>
</ul>
<ol start="4">
<li>바인드 변수 대신 리터럴 사용</li>
</ol>
<ul>
<li>바인드 피킹 문제를 방지할 수 있지만, 소프트 파싱이 불가능해져 CPU 오버헤드 발생.</li>
</ul>
<ol start="5">
<li>CURSOR_SHARING 파라미터 조정</li>
</ol>
<ul>
<li>FORCE로 설정하면 SQL 문장의 실행 계획을 더욱 유연하게 생성할 수 있지만, 성능 테스트가 필요하다.</li>
</ul>