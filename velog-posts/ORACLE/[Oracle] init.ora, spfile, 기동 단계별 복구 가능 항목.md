<h1 id="initora">init.ora</h1>
<ul>
<li>초기화 파라미터를 정의하는 텍스트 파일 </li>
<li>일반 텍스트 파일로, 사용자가 직접 읽고 편집할 수 있다.</li>
<li>위치: 보통 <code>$ORACLE_HOME/dbs/</code> 디렉터리에 저장되며, 파일명은 보통 <code>init&lt;SID&gt;.ora</code> 형태로 지정된다.</li>
</ul>
<h2 id="특징">특징</h2>
<ul>
<li>텍스트 기반, 직접 수정이 가능</li>
<li>변경 사항을 적용하려면 데이터베이스를 다시 시작해야 함</li>
</ul>
<h1 id="spfileora">spfile.ora</h1>
<ul>
<li>(SPFILE, Server Parameter File)</li>
<li>Oracle이 <code>이진(binary)형식</code>으로 저장하는 초기화 파라미터 파일</li>
<li>동적 매개변수 관리를 지원</li>
<li>형식: 바이너리 파일로, 사용자가 직접 읽거나 수정할 수 없다.<h2 id="특징-1">특징</h2>
</li>
<li>데이터베이스가 실행 중일 때 파라미터를 변경하고 저장할 수 있다.</li>
<li>Oracle이 권장하는 초기화 파라미터 관리 방식</li>
<li>변경한 파라미터를 즉시 적용하거나, 데이터베이스 재시작 후 적용하도록 선택할 수 있다.</li>
<li>수정 시 SQL 명령어를 사용한다. <code>ALTER SYSTEM</code></li>
</ul>
<hr />
<h3 id="spfile이-asm에-저장된-경우-확인">SPFILE이 ASM에 저장된 경우 확인</h3>
<blockquote>
<p><code>SHOW PARAMETER spfile;</code></p>
</blockquote>
<p>1) STARTUP 명령을 사용할 때 SPFILE 경로를 지정하거나</p>
<blockquote>
<pre><code class="language-sql">STARTUP PFILE='/u01/app/oracle/product/19c/dbs/init.ora';</code></pre>
</blockquote>
<pre><code>
2) PFILE에서 ASM에 저장된 SPFILE을 지정
&gt; 
```sql
SPFILE='+DATA/ORCL/spfileORCL.ora'</code></pre><h3 id="우선순위">우선순위</h3>
<ul>
<li>Oracle은 데이터베이스를 시작할 때 먼저 SPFILE을 찾는다. <ul>
<li><ol>
<li>ASM 디스크 그룹</li>
</ol>
</li>
</ul>
</li>
</ul>
<blockquote>
<pre><code class="language-text"> +DISKGROUP/&lt;DB_UNIQUE_NAME&gt;/spfile&lt;DB_UNIQUE_NAME&gt;.ora</code></pre>
</blockquote>
<pre><code>
- 2. 파일 시스템
&gt;```text
$ORACLE_HOME/dbs/spfile&lt;SID&gt;.ora (Linux/Unix)
%ORACLE_HOME%\database\spfile&lt;SID&gt;.ora (Windows)  </code></pre><ul>
<li><p>SPFILE이 존재하지 않거나, 지정되지 않으면 PFILE(init.ora)를 찾는다.</p>
</li>
<li><p>SPFILE이 ASM 디스크 그룹이나 파일 시스템에 존재하면 이를 사용한다.</p>
</li>
<li><p>SPFILE이 없을 경우, Oracle은 디폴트 PFILE(init.ora)을 찾는다.</p>
</li>
<li><p>사용자가 PFILE 경로를 명시적으로 지정하면, Oracle은 이를 우선적으로 사용한다.</p>
</li>
</ul>