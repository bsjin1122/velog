<ul>
<li>데이터베이스에서 파일 관리의 자동화를 제공하는 기능</li>
<li>OMF를 활성화하면, 데이터베이스 파일 (데이터 파일, 리두 로그, 컨트롤 파일 등)의 생성, 이름 지정, 삭제를 Oracle이 자동으로 처리한다. </li>
</ul>
<h3 id="parameter">parameter</h3>
<ul>
<li><p><code>DB_CREATE_FILE_DEST</code>
: 데이터 파일, TEMP, UNDO 테이블스페이스 파일의 기본 경로를 지정</p>
</li>
<li><p><code>DB_CREATE_ONLINE_LOG_DEST_n</code>
: 리두 로그 파일과 컨트롤 파일의 기본 경로를 지정</p>
</li>
</ul>
<pre><code class="language-sql">SQL&gt; SHOW PARAMETER DB_CREATE_FILE_DEST;
NAME                TYPE   VALUE
------------------- ------ ------------
db_create_file_dest string /u02/oradata
SQL&gt; SHOW PARAMETER DB_CREATE_ONLINE_LOG_DEST;
NAME                        TYPE   VALUE
--------------------------- ------ -----
db_create_online_log_dest_1 string
db_create_online_log_dest_2 string
db_create_online_log_dest_3 string
db_create_online_log_dest_4 string
db_create_online_log_dest_5 string
</code></pre>
<h3 id="omf를-사용하는-작업-예제">OMF를 사용하는 작업 예제</h3>
<ol>
<li>테이블스페이스 생성<ul>
<li><code>CREATE TABLESPACE my_tbs;</code></li>
<li>/u01/app/oracle/oradata/ORCL/datafile/o1_mf_my_tbs_gv8j9txk_.dbf
로 파일이 생성될 수 있다.</li>
</ul>
</li>
<li>테이블스페이스 삭제</li>
</ol>
<ul>
<li><code>DROP TABLESPACE my_tbs INCLUDING CONTENTS AND DATAFILES;</code><ul>
<li>OMF가 활성화된 상태에서 테이블스페이스로 삭제하면, 관련 데이터파일도 자동으로 삭제된다.</li>
</ul>
</li>
</ul>
<ol start="3">
<li>리두 로그 추가</li>
</ol>
<ul>
<li><code>ALTER DATABASE ADD LOGFILE;</code></li>
<li>지정된 DB_CREATE_ONLINE_LOG_DEST_n 경로에 로그 파일을 자동으로 생성한다.</li>
</ul>
<h3 id="omf-파일-이름-규칙">OMF 파일 이름 규칙</h3>
<ul>
<li>데이터 파일: <code>o1_mf_users_gv8j9txk_.dbf</code></li>
<li>리두 로그 파일: <code>o1_mf_redo1_gv8j9txk_.log</code></li>
<li>ol: Oracle Managed Files의 접두사</li>
<li>mf: Managed File</li>
<li>users: 테이블스페이스 이름</li>
<li>고유 식별자: 고유한 문자열</li>
</ul>
<h3 id="omf와-asm-automatic-storage-management">OMF와 ASM (Automatic Storage Management)</h3>
<ul>
<li>ASM은 디스크 스토리지를 관리하고, OMF는 데이터파일 관리를 자동화하여 스토리지 관리와 데이터 관리가 모두 단순화된다.</li>
</ul>