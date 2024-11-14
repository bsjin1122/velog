<h1 id="1-alert-log">1. Alert Log</h1>
<ul>
<li><p>데이터베이스의 전반적인 상태를 모니터링하고, 주요 이벤트 및 에러를 기록하는 시스템 로그 파일. </p>
<h2 id="내용">내용</h2>
</li>
<li><p>데이터베이스와 관련된 주요 이벤트 기록</p>
<ul>
<li>인스턴스 시작(startup) 및 종료(shutdown) 정보</li>
<li>데이터베이스 구조 변경(예: 테이블스페이스 추가/삭제, 데이터파일 추가/확장 등)</li>
<li>로그 스위치 발생</li>
<li>복구 작업(ex: Media Recovery, Archive 로그 생성)</li>
<li>심각한 에러(예: ORA-00600), ORA-07445 등)</li>
<li>데이터베이스 경고 또는 상태 변경 <h2 id="위치">위치</h2>
</li>
</ul>
</li>
<li><p>Oracle Database 11g 이후:</p>
<blockquote>
<p>$ORACLE_BASE/diag/rdbms/{db_name}/{instance_name}/trace/alert_{instance_name}.log</p>
</blockquote>
</li>
<li><p>Oracle Database 10g 및 이전 버전:</p>
<blockquote>
<p>$ORACLE_HOME/admin/{db_name}/bdump/alert_{SID}.log</p>
</blockquote>
</li>
</ul>
<hr />
<h1 id="2-trace-file">2. Trace File</h1>
<ul>
<li><p>특정 세션이나, 프로세스에서 발생한 상세한 정보를 기록하여 문제를 디버깅하는 데 사용</p>
</li>
<li><p>개별 프로세스 또는 세션에 대한 자세한 정보</p>
<ul>
<li>세션 관련 SQL 수행 내역</li>
<li>시스템 이벤트와 대기 현황</li>
<li>메모리 덤프</li>
<li>특정 오류의 상세 정보 (예: ORA-600 발생 시 진단 정보)</li>
</ul>
</li>
<li><p>프로세스별 또는 이벤트별로 생성되며, 내용이 매우 상세하고 기술적.</p>
</li>
<li><p>예를 들어, 특정 세션의 성능 문제를 분석하거나, 심각한 에러 발생 시 원인을 찾는 데 유용</p>
</li>
</ul>
<blockquote>
<ol>
<li>Alert Log</li>
</ol>
</blockquote>
<ul>
<li>데이터베이스 전반적인 문제를 빠르게 확인, 진단의 첫 단서로 사용</li>
</ul>
<ol start="2">
<li>Trace File</li>
</ol>
<ul>
<li>Alert Log에서 발견된 문제의 상세 원인을 추적</li>
<li>ORA-600 오류가 발생한 경우, 관련 Trace File을 분석하여 문제 원인을 확인</li>
</ul>
<blockquote>
<ul>
<li>Alert Log는 데이터베이스의 전반의 &quot;큰 그림&quot;을 보여주며, 주요 이벤트 및 경고를 관리</li>
</ul>
</blockquote>
<ul>
<li>Trace File은 특정 세션 또는 프로세스와 관련된 &quot;세부 정보&quot;를 제공하여, 문제를 심층 분석.</li>
</ul>