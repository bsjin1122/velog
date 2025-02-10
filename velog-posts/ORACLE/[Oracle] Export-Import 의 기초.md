<blockquote>
<ul>
<li>출처: <a href="https://www.oracle.com/jp/a/tech/docs/technical-resources/20100908-expimp-beginner.pdf">의외로 모르는 Export/Import의 기초</a></li>
</ul>
</blockquote>
<ul>
<li><a href="https://docs.oracle.com/cd/E15817_01/server.111/e05768.pdf">11g Utility</a></li>
<li>expdp/impdp help 내용 정리하기 전에 도움이 될 것 같아서 정리해본다.</li>
</ul>
<h2 id="data-pump">Data Pump</h2>
<ul>
<li>Oracle Database 10g부터 도입된 새로운 유틸리티</li>
<li>Oracle Data Pump 기술을 사용하면 Data 및 MetaData를 데이터베이스간 빠른 속도로 이동이 가능하다.<blockquote>
<p>사용 방법</p>
</blockquote>
</li>
<li>expdp/impdp command</li>
<li>Enterprise Manager</li>
<li>DBMS_DATAPUMP PL/SQL 패키지</li>
<li>그 외, 외부 테이블 등 engine으로서 내부 이용</li>
<li>관련 메뉴얼 </li>
</ul>
<h1 id="direct-path-api-개선에-의한-처리-속도-향상"><em>Direct Path API 개선에 의한 처리 속도 향상</em></h1>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/c01f3838-3e46-4bba-b021-9d1408cd8094/image.png" /></p>
<ul>
<li>export: original export에 비해 2배 고속</li>
<li>import: original import에 비해 15~40배 고속</li>
</ul>
<blockquote>
<p><strong>Data Pump는, 대량의 데이터를 다루는 큰 작업(Job) 용도</strong></p>
</blockquote>
<ul>
<li><p>Data Pump에서는, Master Table을 생성하기 위한 Overhead에 의해 작은 작업은 늦어지지만, 대량의 데이터를 고속으로 처리하는 것은 중/대규모 작업에서 가장 큰 메리트이다.</p>
</li>
<li><p>Direct Path API란?
Direct Path API는 Oracle 데이터베이스에서 디스크 I/O 작업을 최적화하고, 데이터를 효율적으로 디스크에 쓰고 읽는 방법을 제공하는 고속 데이터 전송 메커니즘</p>
</li>
</ul>
<h2 id="exportimport---export-디렉토리-지정">Export/Import - export 디렉토리 지정</h2>
<ul>
<li><p>Datapump에서는 client가 아닌 server에 의해 파일이 쓰여지기 때문에, 처리할 directory를 위치가 특정되어 있을 필요가 있다.</p>
</li>
<li><p>Dump File을 출력할 디렉토리에 대해, DB 상에 Directory Object를 생성한다.</p>
</li>
<li><p>실행 시에는, Directory Object를 DIRECTORY 파라미터로 지정한다.</p>
<pre><code class="language-sql"># 디렉토리 오브젝트 생성 
SQL&gt; CREATE DIRECTORY DPUMP_DIR1 AS 'home/oracle/oradata/dpump_dir';
SQL&gt; GRANT READ, WRITE ON DIRECTORY dpump_dir1 TO scott; -- 권한 부여
COMMAND&gt; expdp scott/tiger tables=emp,dept directory=dpump_dir1</code></pre>
</li>
<li><p>파라미터로 디렉토리를 지정하지 않은 경우, OS환경변수 <code>DATA_PUMP_DIR</code>, 혹은 Directory Object <code>DATA_PUMP_DIR</code>가 참조된다.</p>
<pre><code class="language-shell"># 환경변수의 설정
COMMAND&gt; set DATA_PUMP_DIR=DPUMP_DIR1; export DATA_PUMP_DIR
COMMAND&gt; expdp scott/tiger schemas=scott</code></pre>
</li>
</ul>
<h2 id="export-data-pump">Export (Data Pump)</h2>
<table>
<thead>
<tr>
<th><strong>모드</strong></th>
<th><strong>기능 설명</strong></th>
<th><strong>파라미터</strong></th>
</tr>
</thead>
<tbody><tr>
<td><strong>전체(Full)</strong></td>
<td>데이터베이스 전체를 내보내기</td>
<td><code>FULL=y</code></td>
</tr>
<tr>
<td><strong>스키마(Schema)</strong></td>
<td>지정된 스키마 전체를 내보내기</td>
<td><code>SCHEMAS=schema[, …]</code></td>
</tr>
<tr>
<td><strong>테이블(Table)</strong></td>
<td>지정된 테이블 전체를 내보내기</td>
<td><code>TABLES=table[, …]</code></td>
</tr>
<tr>
<td><strong>테이블스페이스(Tablespace)</strong></td>
<td>지정된 테이블스페이스 전체를 내보내기</td>
<td><code>TABLESPACES=tablespace[, …]</code></td>
</tr>
</tbody></table>
<pre><code class="language-sql">ex1&gt; expdp scott/tiger full=y &lt;&lt;------- full mode
ex2&gt; expdp scott/tiger dumpfile=exp.dmp tables=emp,dept &lt;&lt;------- table모드</code></pre>
<h2 id="filter-처리를-수행">Filter 처리를 수행</h2>
<h3 id="includeexclude">INCLUDE/EXCLUDE</h3>
<ul>
<li><p>필터 처리를 수행하고, export의 대상이 되는 object를 세밀하게 설정이 가능하다.</p>
</li>
<li><p>INCLUDE/EXCLUDE 파라미터는 동시에 지정할 수 없다.</p>
</li>
<li><p>export 대상 object를 include 파라미터로 지정한다.</p>
<pre><code class="language-shell">COMMAND&gt; expdp scott/tiger include=table
COMMAND&gt; expdp scott/tiger include=index</code></pre>
</li>
<li><p>export 대상으로부터 제외할 오브젝트를 EXCLUDE 파라미터로 지정한다.</p>
</li>
<li><p>COMMAND&gt;<code>expdp scott/tiger exclude=index:&quot;LIKE 'EMP%'&quot;</code></p>
</li>
</ul>
<blockquote>
<p>공백 등을 구분자로 하지 않도록 <code>&quot;</code>이 필요하지만, OS에 따라서 escape 문자가 필요하게 된다. 따라서 통상적으론 parameter를 기술한 파일에서 읽는 것이 편리하다.</p>
</blockquote>
<h2 id="flashback-mode를-지정한다">Flashback Mode를 지정한다</h2>
<ul>
<li>지정된 특정 시점 또는 특정 SCN에서의 데이터 상태를 유지한 채로 내보내는 기능</li>
<li>일관된 데이터 백업을 생성할 때 유용</li>
</ul>
<h3 id="flashback_time-특정-시점-기준">FLASHBACK_TIME: 특정 시점 기준</h3>
<ul>
<li>특정 날짜 및 시간을 기준으로 데이터 내보내기</li>
<li>이스케이프(&quot;) 문자가 필요하므로, 파라미터 파일에서 설정하는 것이 권장됨<pre><code class="language-shell">COMMAND &gt; cat parfile.txt
FLASHBACK_TIME=&quot;TO_TIMESTAMP('2004/03/20 10:00','YYYY/MM/DD HH:MI')&quot;
</code></pre>
</li>
</ul>
<p>COMMAND &gt; expdp scott/tiger parfile=parfile.txt</p>
<pre><code>- parfile.txt 파일에 FLASHBACK_TIME 설정
- 2004년 3월 20일 오전 10시 기준으로 데이터 내보내기
- 이후 expdp 실행 시 해당 시점의 데이터를 백업

### FLASHBACK_SCN 사용: SCN 기준
- 특정 SCN에서의 데이터 상태를 유지한 채 내보내기
- SCN은 Oracle에서 트랜잭션을 추적하는 고유한 번호
- SCN을 알고 있다면 더 정확한 시점의 데이터를 내보낼 수 있다.
- 특정 트랜잭션이 완료된 직후의 상태로 데이터를 덤프할 때 유용하다.
```shell
COMMAND &gt; expdp scott/tiger flashback_scn=364909
---&gt; scn 번호 기준으로 데이터를 내보내는 명령어</code></pre><h2 id="parallel-export를-지정한다">Parallel Export를 지정한다</h2>
<h3 id="parallel">PARALLEL</h3>
<ul>
<li>Export 처리를 Parallel로 수행하는 것이 가능하다.</li>
<li>병렬도를 PARALLEL 파라미터로 지정한다.</li>
<li>출력할 디렉토리를 각기 지정하는 것도 가능하다.</li>
</ul>
<pre><code class="language-shell"># 병렬도의 지정
COMMAND &gt; expdp scott/tiger parallel=3 dumpfile=dpump_dir1:expdat%U.dmp,
dpump_dir2%U.dmp 
--- %U(치환변수)를 지정하지 않는 경우, dumpfile 파일 수는 parallel 수에 맞출 필요가 있다. 
--- 지정되어 있는 경우, 지정된 파일이 round robin으로 사용된다.

COMMAND &gt; ls –lR
dpump_dir1: --- 생성된 dump file set 확인
…….expdat01.dmp
…….expdat02.dmp
dpump_dir2:
…….expdat01.dmp</code></pre>
<h2 id="dump-file-size를-예측한다">Dump File Size를 예측한다.</h2>
<h3 id="estimate">ESTIMATE</h3>
<ul>
<li>덤프파일을 생성하지 않고, 생성되는 덤프 파일 사이즈를 예상하는 것이 가능하다.</li>
<li>추측모드?를 ESTIMATE 파라미터로 지정한다.</li>
<li><code>BLOCKS 모드</code> --- 블록 사이즈에 오브젝트의 블록 수를 곱해 예상한다. (정확도는 높지 않음)</li>
<li><code>STATISTICS 모드</code> --- 기존의 통계정보를 기반으로 크기를 추정한다. DBMS_STATS에서 수집한 정보를 활용한다. 일반적으로 STATISTICS 방식이 더 정확하다.</li>
</ul>
<pre><code class="language-shell"># 덤프 파일을 생성하지 않고 크기만 출력: ESTIMATE_ONLY=y를 지정한다.
COMMAND&gt; expdp scott/tiger tables=emp,dept estimate=blocks
estimate_only=y 
</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/3cfd7d27-78dd-4c53-89ec-23bc2462e42d/image.png" /></p>
<h1 id="impdp">IMPDP</h1>
<ul>
<li>expdp에서 사용할 수 있던 파라미터와 대부분 이용할 수 있다.</li>
<li>IMPDP에서 파라미터를 지정함에 따라, EXPDP에서 생성한 덤프 파일로부터 더욱이 대상 데이터를 (필요한 것들을 조합해) IMPORT 가능하다.<pre><code class="language-shell">COMMAND&gt; impdp scott/tiger tables=emp,dept -- dumpfile로부터 emp 테이블과 dept 테이블만을 import
COMMAND&gt; impdp scott/tiger include=index -- dumpfile로부터 index만 import</code></pre>
</li>
</ul>
<h2 id="network-link를-사용한다">Network link를 사용한다.</h2>
<h3 id="network_link">NETWORK_LINK</h3>
<ul>
<li>10g 이후 버전에서만 수행 가능 (network link import)</li>
<li>데이터베이스 링크를 사용해서, 원격 데이터베이스로부터 직접 로컬 데이터베이스에 import를 수행할 수 있다.</li>
</ul>
<blockquote>
<p>참고: export의 네트워크 링크 지정은, 원격 데이터베이스의 데이터를 로컬로 export하는 기능이다. import 경우에는 직접 로컬 데이터베이스에 쓰므로, dumpfile을 생성하지 않는다.</p>
</blockquote>
<h3 id="export-네트워크-링크로-데이터-내보내기">Export (네트워크 링크로 데이터 내보내기)</h3>
<ul>
<li><p>expdp 명령에서 NETWORK_LINK를 사용하면 원격 데이터베이스의 데이터를 로컬 시스템에 export(내보내기)하는 작업을 수행할 수 있다.</p>
</li>
<li><p>예를 들어, 원격 데이터베이스에서 데이터를 추출하여 로컬 데이터베이스의 dump 파일로 저장하는 방식</p>
</li>
<li><p>이때 dump 파일이 로컬에 저장되며, 네트워크를 통해 원격 데이터베이스와 연결하여 데이터를 가져온다.</p>
</li>
</ul>
<blockquote>
<p>expdp scott/tiger network_link=remote_db_link directory=DATA_PUMP_DIR dumpfile=remote_data.dmp</p>
</blockquote>
<ul>
<li>위의 예시는 원격 데이터베이스와 연결된 <strong>remote_db_link</strong>를 사용하여, 
원격 데이터베이스에서 데이터를 로컬 dump 파일에 내보내는(export) 작업을 수행하는 명령어</li>
</ul>
<h3 id="import-네트워크-링크로-데이터-가져오기">Import (네트워크 링크로 데이터 가져오기)</h3>
<ul>
<li><p>impdp 명령에서 <strong>NETWORK_LINK</strong>를 사용하면 원격 데이터베이스의 데이터를 직접 로컬 데이터베이스로 가져오는(import) 작업을 할 수 있다. 이때 dump 파일을 생성하지 않는다.</p>
</li>
<li><p>원격 데이터베이스에서 직접 데이터를 로컬 데이터베이스로 삽입하므로, 중간에 dump 파일을 생성할 필요가 없습니다.</p>
<blockquote>
<p>impdp scott/tiger network_link=remote_db_link directory=DATA_PUMP_DIR tables=emp</p>
</blockquote>
</li>
<li><p>위의 예시는 원격 데이터베이스에서 emp 테이블을 로컬 데이터베이스로 직접 가져오는(import) 작업을 수행하는 명령어</p>
</li>
</ul>
<h3 id="핵심-차이점">핵심 차이점</h3>
<ul>
<li><strong>Export</strong>: NETWORK_LINK를 사용하여 원격 데이터베이스에서 데이터를 로컬 시스템에 dump 파일로 내보낼 수 있다. <ul>
<li><code>즉, 원격 데이터베이스의 데이터를 로컬에 덤프 파일로 저장한다.</code></li>
</ul>
</li>
<li><strong>Import</strong>: NETWORK_LINK를 사용하여 원격 데이터베이스에서 데이터를 로컬 데이터베이스로 바로 삽입한다. <ul>
<li>이때 덤프 파일이 생성되지 않으며, 네트워크 링크를 통해 원격 데이터베이스에서 직접 데이터를 가져와 로컬 데이터베이스에 기록한다.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="여러-개의-테이블을-export하여-데이터만-import하고-싶을-때">여러 개의 테이블을 export하여 데이터만 import하고 싶을 때</h2>
<ul>
<li>여러 개의 테이블을 Export해서 데이터만을 Import하고 싶은데, FK가 많이 있어서 정합성 제약에 위반하게 돼.....</li>
<li>다음과 같이 관련된 참조정합성(pk-fk)을 disable하고, import 후에 참조정합성제약을 enable로 하면, error를 해소할 수 있다.</li>
</ul>
<blockquote>
<p>외래 키 제약조건을 일시적으로 비활성화 한 후, 데이터만 import한 후 다시 활성화한다.</p>
</blockquote>
<pre><code class="language-sql">COMMAND&gt; expdp system/manager ;
SQL&gt; alter table emp disable constraint emp_no_fk ; -- 관련된 모든 외래 키 제약조건을 disable로 설정
COMMAND&gt; impdp system/manager ;
SQL&gt; alter table emp enable constraints emp_no_fk ; -- 관련된 모든 외래 키 제약조건을 enable로 설정</code></pre>
<hr />
<h1 id="tip">Tip</h1>
<h2 id="export-덤프로부터-일부-데이터를-제외하는-방법">Export 덤프로부터 일부 데이터를 제외하는 방법</h2>
<ul>
<li>실수로 일부 데이터를 delete해서, commit 해버렸어!<ul>
<li>export의 dumpfile로부터 추출하고 싶어.. (제외하고 싶어)<pre><code class="language-sql">command&gt; impdp system/manager remap_schema=oradirect:dummy
SQL&gt; insert into oradirect.emp select * from dummy.emp where emp_id=100;
SQL&gt; drop table dummy.emp</code></pre>
<blockquote>
<ul>
<li>주의: export한 시점의 데이터와 삭제한 데이터가 일치하는지는 불명확하기 때문에, 이 예시의 경우 emp_id=100의 데이터에 관해 export할 때랑 실수해서 삭제한 시점이 동일했다는 것을 전제로 한다.</li>
</ul>
</blockquote>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="export-file-size을-지정하는-방법">Export File Size을 지정하는 방법</h2>
<h3 id="filesize">FILESIZE</h3>
<ul>
<li><p>기본값: 데이터는 최대 사이즈에 도달할 때까지 1개 파일로 쓰여진다.</p>
</li>
<li><p>용도: FILESIZE 파라미터값(BYTE제한)을 지정하면, EXPORT utility 에 의해 각각의 덤프파일에 지정한 byte값만을 쓰게 된다.</p>
</li>
<li><p>예) exp scott/tiger TABLES=emp FILESIZE=2048👉KB, MB, GB를 붙여 지정할 수도 있다.</p>
</li>
<li><p>** FILESIZE=5MB를 지정한 경우** 
<img alt="" src="https://velog.velcdn.com/images/greendev/post/1e36f934-56f8-4719-8397-57911f64b6a7/image.png" /></p>
</li>
</ul>
<hr />
<h2 id="where절을-지정하여-export-범위를-제한하는-방법">WHERE절을 지정하여 EXPORT 범위를 제한하는 방법</h2>
<h3 id="query">QUERY</h3>
<ul>
<li>기본값: 없음</li>
<li>용도: export 실행 시에 일련의 테이블로부터 행의 subset을 선택할 수 있도록 한다.<ul>
<li>query 파라미터 값은 select문의 where절을 포함하는 문자열이다.</li>
</ul>
</li>
</ul>
<p>예: 직종이 SALESMAN, 급여가 1600보다 적은 종업원만을 export할 경우</p>
<pre><code class="language-shell">exp scott/tiger TABLES=emp QUERY=&quot;WHERE job='SALESMAN' and sal &lt;1600&quot;</code></pre>
<hr />
<h2 id="sqlfile">SQLFILE</h2>
<ul>
<li>기본값: 없음</li>
<li>용도: impdp가 실행할 ddl(테이블 생성, 인덱스 생성 등)의 SQL문을 파일로 저장</li>
<li>즉, 실제 import를 수행하지 않고, 어떤 SQL문이 실행될지를 미리 확인할 수 있다.</li>
<li>사용 예: <code>impdp scott/tiger TABLES=(wendy.emp) 👉SQLFILE='index.txt'</code></li>
</ul>
<blockquote>
<p><strong>주의</strong></p>
</blockquote>
<ul>
<li><p>password는 SQL File에 포함되지 않는 점에 주의할 것</p>
</li>
<li><p>예를 들면, (CREATE USER 등) 실행한 ddl에 connect 문이 포함되어 있는 경우, </p>
</li>
<li><p>그 문장은 주석처리 되어, schema 명만 표시된다.</p>
</li>
<li><p><em>TEST_TABLE테이블을 import할 때 SQLFILE을 사용하는 경우*</em></p>
</li>
<li><p><code>impdp oradirect/oradirect dumpfile=test_table.dmp tables=test_table 
👉sqlfile=sqlfile.txt</code></p>
<ul>
<li>실제 데이터를 import하지 않고, 테이블을 생성하는 SQL문을 미리 확인 가능하다.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/5d371341-704e-4cc3-9e2e-4aca0f43f2b6/image.png" /></p>
<hr />
<h2 id="data-pump-압축">Data Pump 압축</h2>
<ul>
<li><code>COMPRESSION={ALL|DATA_ONLY|METADATA_ONLY|NONE}</code></li>
<li>NONE: export 전체에 대해 압축이 무효</li>
<li>METADATA_ONLY(default): 전체의 메타데이터가 압축 형식으로 덤프 파일로 생성</li>
</ul>
<p>** 여기서부터는 Advanced Compression 필수**</p>
<ul>
<li>DATA_ONLY: 모든 데이터가 압축형태로 데이터파일로 생성</li>
<li>ALL: 데이터, 메타데이터가 같이 압축</li>
</ul>
<blockquote>
<p>스키마를 지정하고, 메타데이터, 데이터와 같이 압축해서 덤프 파일 scott.dmp로 export</p>
</blockquote>
<ul>
<li>expdp scott/tiger DIRECTORY=dpump_dir DUMPFILE=scott.dmp COMPRESSION=ALL SCHEMAS=scott</li>
</ul>
<hr />
<h2 id="data-pump-암호화">Data Pump 암호화</h2>
<ul>
<li><code>ENCRYPTION = {ALL | DATA_ONLY | ENCRYPTED_COLUMNS_ONLY | METADATA_ONLY| NONE}</code></li>
<li>ALL: 모든 데이터 및 메타데이터에 대해 암호화가 유효</li>
<li>DATA_ONLY: 데이터만</li>
<li>ENCRYPTED_COLUMNS_ONLY: 암호화된 열만 암호화됨</li>
<li>METADATA_ONLY: 메타데이터만이 암호화됨</li>
<li>NONE: 데이터는 암호화되지 않음</li>
</ul>
<blockquote>
<p>** Dump File에서 데이터만 암호화되는 export 구문**</p>
</blockquote>
<ul>
<li><code>$ expdp scott/tiger DIRECTORY=dpump_dir DUMPFILE=scott_enc.dmp
SCHEMAS=scott ENCRYPTION=data_only ENCRYPTION_PASSWORD=tiger</code></li>
</ul>
<hr />
<h2 id="direct-path">Direct Path</h2>