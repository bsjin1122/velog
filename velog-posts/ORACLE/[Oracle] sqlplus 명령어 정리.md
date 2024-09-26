<h1 id="sqlplus">SQL*Plus</h1>
<h2 id="숫자-풀기">숫자 풀기</h2>
<pre><code class="language-sql">  SELECT 123123123123123112 FROM dual;
  SET LINE 500
  /
  확인했을 땐 1E7+ (숫자가 아닌 과학적 숫자로 표기됨)
  SET NUM 38
  /
  숫자가 풀려서 보인다.</code></pre>
<ul>
<li>help set</li>
</ul>
<h2 id="set-time-on-set-timing-on">SET TIME ON, SET TIMING ON</h2>
<ul>
<li><p>💚<code>set time on</code> : SQL*Plus 세션에 현재 시간을 표시</p>
<ul>
<li>SQL 프롬프트에 명령을 입력할 때마다 현재 시간이 표시된다. <ul>
<li><code>/</code>: PL/SQL 블록 실행</li>
</ul>
</li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li>SQL*Plus에서는 PL/SQL 블록이 입력될 때, 해당 블록은 세미콜론(;)으로 끝나지 않고 단일 슬래시(/)로 끝내야 실행된다. <code>/</code>으로 실행을 트리거 한다고 보면 된다.<ul>
<li>SQL명령: 세미콜론(;)으로 즉시 실행</li>
</ul>
</li>
</ul>
</blockquote>
<ul>
<li>💎<code>set timing on</code>: SQL문 또는 PL/SQL 블록을 실행하는 데 걸리는 시간을 표시</li>
</ul>
<hr />
<pre><code class="language-sql">  SQL&gt; SET TIME ON
💚15:30:21 SQL&gt; SET TIMING ON
15:30:25 SQL&gt; SELECT * FROM employees WHERE department_id = 10;

EMPLOYEE_ID FIRST_NAME  LAST_NAME  EMAIL       PHONE_NUMBER  HIRE_DATE   JOB_ID     SALARY
----------- ------------ ---------- ---------- ------------ ---------- ---------- ---------
178         Kim         Smith      KSMITH      515.123.4567  21-JUN-01   SA_REP     6000

💎Elapsed: 00:00:00.02
</code></pre>
<hr />
<h2 id="help-set">help set</h2>
<ul>
<li><p>SET 명령에서 나오는 옵션들.. 이것저것 많이 알고 있어야 해요. </p>
</li>
<li><p><code>SET ECHO {ON|OFF}</code>: SQL 스크립트의 명령을 실행하면서, 화면에 표시할지 여부를 설정</p>
</li>
<li><p><code>SET FEEDBACK {ON|OFF}</code>: 영향 받은 행의 수를 표시 on/off</p>
</li>
<li><p><code>SET LINESIZE n</code>: 한 페이지에 표시될 수 있는 최대 행 수를 지정</p>
</li>
<li><p><code>SET PAGESIZE n</code>: 한 페이지에 표시될 수 있는 최대 행 수를 지정</p>
</li>
<li><p><code>SET SQLPROMPT 'text'</code> : 프롬프트를 사용자가 원하는 텍스트로 변경</p>
<ul>
<li>ex: SET SQLPROMPT 'BSJ&gt; '</li>
</ul>
</li>
</ul>
<pre><code class="language-sql">  BSJ&gt; SELECT * FROM employees WHERE employee_id = 100;</code></pre>
<ul>
<li><code>SET SERVEROUTPUT {ON|OFF}</code>: PL/SQL 블록에서 DBMS_OUTPUT.PUT_LINE과 같은 명령을 통해 생성된 출력이 표시될지 여부를 설정한다.</li>
</ul>
<pre><code class="language-SQL">  SET SERVEROUTPUT ON;
  BEGIN 
      DBMS_OUTPUT.PUT_LINE('Hello, SQL*Plus!');
  END;
  /

  ##출력문으로########################################
  Hello, SQL*Plus!
  PL/SQL procedure successfully completed.
</code></pre>
<h2 id="실행계획-보기">실행계획 보기</h2>
<ul>
<li><p><code>SET AUTOT ON EXP</code>: SET AUTOTRACE ON EXPLAIN; SQL문 실행 후 실행 계획만 표시한다. 결과는 나타나지 않는다.</p>
</li>
<li><p><code>SET AUTOTRACE ON</code>: SQL문 실행 결과와 함께 실행 계획 및 통계 정보가 표시된다.</p>
</li>
<li><p><code>SET AUTOTRACE TRACEONLY</code>: SQL문 실행 결과는 숨기고 실행 계획 및 통계 정보만 표시</p>
</li>
</ul>
<h2 id="history">history</h2>
<ul>
<li>history </li>
<li>hist 8 run &lt;- history가 보여지는 것들 중 8번째 쿼리를 실행</li>
</ul>
<h2 id="csv-형식으로-출력하기">csv 형식으로 출력하기</h2>
<pre><code class="language-sql">SELECT * FROM V$INSTANCE;
SELECT MARKUP CSV ON QUOTE OFF
/
엔터</code></pre>
<ul>
<li><p><code>SELECT MARKUP CSV ON</code>
: SQL*Plus에서 결과를 csv(Comma-Separated Values) 형식으로 출력하도록 설정한다.</p>
</li>
<li><p><code>QUOTE OFF</code>
: 출력 값에 대해 따옴표를 사용하지 않도록 설정한다.</p>
</li>
</ul>
<h2 id="날짜-출력하기">날짜 출력하기</h2>
<pre><code class="language-sql">ALTER SESSION SET NLS_DATE_FORMAT='YYYY/MM/DD HH24:MI:SS';

SELECT SYSDATE FROM DUAL;

# 결과

SYSDATE
-------------------
2024/09/26 15:45:30
</code></pre>
<h2 id="현재-시스템에서-실행중인-프로세스-찾기">현재 시스템에서 실행중인 프로세스 찾기</h2>
<pre><code class="language-sql">ps -ef | grep tns</code></pre>
<ul>
<li>ps -ef: 현재 시스템에서 실행 중인 모든 프로세스를 상세하게 출력한다.<ul>
<li><code>-e</code> : 모든 프로세스를 출력한다. </li>
<li><code>-f</code>: 자세한 형식으로 출력한다.</li>
</ul>
</li>
</ul>
<h2 id="리스너-상태-확인">리스너 상태 확인</h2>
<pre><code class="language-sql">lsnrctl status ORADVLT_LISTENER

### 결과
############################################################################
LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 26-SEP-2024 10:30:00

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=myhost)(PORT=1521)))
STATUS of the LISTENER
------------------------
Alias                     ORADVLT_LISTENER
Version                   TNSLSNR for Linux: Version 19.0.0.0.0 - Production
Start Date                26-SEP-2024 10:00:00
Uptime                    0 days 0 hr. 30 min. 0 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Listener Parameter File   /u01/app/oracle/product/19c/dbhome_1/network/admin/listener.ora
Listener Log File         /u01/app/oracle/diag/tnslsnr/myhost/ORADVLT_LISTENER/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=myhost)(PORT=1521)))
Services Summary...
Service &quot;ORCL&quot; has 1 instance(s).
  Instance &quot;ORCL&quot;, status READY, has 1 handler(s) for this service...
The command completed successfully

</code></pre>
<ul>
<li>Oracle Listener Control (lsnrctl) 유틸리티를 사용하여 <code>ORADVLT_LISTENER</code>라는 이름의 리스너의 현재 상태를 확인하는 데 사용</li>
<li>Oracle 데이터베이스에서 클라이언트와 서버 간의 통신을 관리하는 
TNS Listener의 상태를 확인하는 방법</li>
</ul>
<h2 id="오라클-리스너-파일-실시간으로-확인">오라클 리스너 파일 실시간으로 확인</h2>
<pre><code class="language-sql">tail -f listener.log</code></pre>
<ul>
<li>tail -f listener.log 명령은 Oracle Listener 로그 파일의 마지막 부분을 실시간으로 모니터링하는 데 사용</li>
</ul>
<h2 id="ls--ltrf">ls -ltrF</h2>
<ul>
<li><code>ls</code> : 현재 디렉터리의 파일과 디렉터리 목록을 표시하는 기본 명령</li>
<li><code>-l</code> : 긴 형식으로 상세정보를 표시한다. 파일 권한, 소유자, 그룹, 파일 크기, 수정 날짜 및 파일 이름 등이 포함된다.</li>
<li><code>-t</code>: 파일을 수정 시간 순서로 정렬한다. 수정된 파일이 가장 마지막에 나타난다.</li>
<li><code>-r</code>: 역순(reverse order) 로 정렬한다. 즉, 오래된 파일이 먼저 나오고, 최근 파일이 마지막에 표시된다. </li>
<li><code>-F</code>: 파일 디렉터리 유형을 식별하기 위해, 파일 이름에 식별문자를 추가한다.<ul>
<li><code>/</code>: 디렉터리</li>
<li><code>*</code>: 실행 파일</li>
<li><code>@</code>: 심볼릭 링크</li>
<li><code>|</code>: 파이프</li>
<li><code>=:</code>: 소켓</li>
</ul>
</li>
</ul>