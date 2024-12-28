<ul>
<li>show parameter local</li>
</ul>
<h2 id="1-동적-인스턴스-등록-dynamic-instance-registration">1. 동적 인스턴스 등록 (Dynamic Instance Registration)</h2>
<ul>
<li><p>열려 있는 것을 리스너가 찾아가는 방식</p>
</li>
<li><p>데이터베이스 인스턴스가 자동으로 리스너에 등록</p>
</li>
<li><p>데이터베이스를 시작하거나, <code>ALTER SYSTEM REGISTER;</code> 명령을 실행하면 PMON 프로세스가 리스너에게 자신을 등록한다.</p>
</li>
<li><p>주로 동적 포트를 사용하며, <code>LOCAL_LISTENER</code> 또는 <code>REMOTE_LISTENER</code> 설정이 필요하다</p>
</li>
<li><p>개발 테스트 환경에서 주로 사용</p>
</li>
</ul>
<h3 id="절차">절차</h3>
<ol>
<li><p>리스너 시작 : lsnrctl start; 리스너 프로세스 시작</p>
</li>
<li><p>데이터베이스 시작: startup;</p>
</li>
<li><p>동적 등록 확인: lsnrctl status;</p>
</li>
<li><p>수동으로 등록 요청 (필요 시) </p>
</li>
</ol>
<ul>
<li>데이터베이스가 이미 실행 중이고, 리스너가 다시 시작된 경우 PMON이 등록 요청을 보낸다.</li>
<li>ALTER SYSTEM REGISTER;</li>
</ul>
<hr />
<h2 id="2-정적-인스턴스-등록-static-instance-registration">2. 정적 인스턴스 등록 (Static Instance Registration)</h2>
<ul>
<li>데이터베이스 인스턴스를 리스너 구성 파일(listener.ora)에 정적으로 정의</li>
<li>데이터베이스가 동적으로 등록되지 않아도 항상 특정 포트를 통해 접근 가능</li>
<li>고정 환경(예: 특정 IP/포트를 사용하는 시스템)에서 사용</li>
<li>고정 IP/포트를 사용하는 프로덕션 환경에서 주로 사용</li>
</ul>
<h3 id="절차-1">절차</h3>
<ol>
<li>listener.ora<blockquote>
<pre><code class="language-shell">SID_LIST_LISTENER =
(SID_LIST =
 (SID_DESC =
   (GLOBAL_DBNAME = mydb)
   (ORACLE_HOME = /u01/app/oracle/product/19c/dbhome_1)
   (SID_NAME = mydb)
 )
)</code></pre>
</blockquote>
</li>
</ol>
<pre><code>2. listener 다시 시작
- lsnrctl stop
- lsnrctl start
3. 리스너 상태 확인
- lsnrctl status

## ALTER SYSTEM REGISTER의 역할
- 데이터베이스에서 리스너로 등록 요청을 보낸다.
- 리스너가 재시작된 경우, PMON이 동적 등록을 아직 수행하지 않은 경우!</code></pre>