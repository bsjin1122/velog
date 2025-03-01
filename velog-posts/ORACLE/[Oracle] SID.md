<h3 id="상황">상황</h3>
<blockquote>
<p>SID가 안맞아서 어디서 문제가 있는지 못찾고 헤맸다... . 그럼 나는 개념을 잘 모르고 있었다는 것,,,,,</p>
</blockquote>
<ul>
<li>참고: MOS Difference between DB name, DB global name, DBID and SID (Doc ID 1277854.1)</li>
</ul>
<h2 id="dbid">DBID</h2>
<ul>
<li>DBID는 데이터베이스를 구분하는, 내부에서 고유하게 생성된 숫자.</li>
<li>Oracle은 데이터베이스를 만들 때, 숫자를 자동으로 만든다.</li>
<li>파일이 속해있는 데이터베이스를 식별하는 데 사용</li>
<li>복구 작업에 사용되어 특정 Redo Log/Archived Redo Log가 실제로 복구 중인 데이터베이스에 속한다고 결정한다.</li>
<li>따라서, DBID를 변경하려면 RESETLOGS 옵션으로 데이터베이스를 열어야 한다. 그리고 이전의 모든 Archive Logs를 무효화한다.</li>
</ul>
<h2 id="db_name">DB_NAME</h2>
<ul>
<li>DB_NAME은 서버에서 데이터베이스를 고유하게 식별한 이름</li>
<li>데이터베이스 생성 시점에 정의되어 control file에 작성이 된다.</li>
<li>동일한 DB_NAME을 가진 두 개의 데이터베이스를 가질 수 없다.</li>
</ul>
<h1 id="sid">SID</h1>
<ul>
<li>Database가 아닌, 인스턴스를 고유하게 식별</li>
<li>인스터스는 데이터베이스에 엑세스하는 Oracle 실행 파일과 결합된 메모리 구조 셋</li>
</ul>
<h2 id="database-global-name">Database Global Name</h2>
<ul>
<li>데이터베이스의 고유한 이름이다.</li>
<li>분산데이터베이스 시스템에서, 일반적으로 single database로 응용 프로그램에 나타나는 여러 컴퓨터에 저장된 데이터베이스 셋이다.</li>
<li>글로벌 데이터베이스 이름은 각 데이터베이스가 시스템의 다른 모든 데이터베이스와 구별되도록 한다.</li>
<li>Oracle은 데이터베이스 네트워크 도메인을 개별 데이터베이스 이름으로 prefix하여 데이터베이스의 글로벌 데이터베이스 이름을 형성한다.<ul>
<li>Oracle Net Services(네트워크 통신)에서 데이터베이스를 식별할 때 활용된다.</li>
</ul>
</li>
<li><code>DB_NAME.DB_DOMAIN</code>: 개별데이터베이스이름(필수).네트워크도메인이름(선택)</li>
</ul>
<pre><code class="language-sql">SQL&gt; show parameter _name
NAME                   TYPE    VALUE
---------------------- ------- -------
cdb_cluster_name       string
cell_offloadgroup_name string
db_file_name_convert   string
db_name                string  EVIL13
db_unique_name         string  EVIL13
global_names           boolean FALSE
instance_name          string  EVIL131
lock_name_space        string
log_file_name_convert  string
pdb_file_name_convert  string
processor_group_name   string
service_names          string  EVIL13</code></pre>
<h2 id="db_name-변경하지-않고-dbid만-변경할-수-있는가">DB_NAME 변경하지 않고 DBID만 변경할 수 있는가?</h2>
<ul>
<li>DBID 및 DB NAME은 NID 유틸리티에 의해 변경될 수 있으나, DB NAME을 변경할 때 새로운 DBID를 자동으로 생성할 수는 없다.</li>
<li>DBID는 고객이 조작해서는 안되며, 데이터베이스에 의해 내부적으로 처리된다. 또한 변경하면 모든 archive redo logs가 무효화된다.</li>
<li>이를 수행하려는 유일한 방법은 NID 유틸리티를 사용해 데이터베이스 이름을 변경하는 것이다. DBID도 암시적으로 바꾼다.</li>
<li>DB NAME을 동일한 이름으로 변경하기 위해 NID를 사용하면 오류가 발생한다.<ul>
<li>DB NAME을 임시 이름으로 변경하고, 나중에 다시 원래 이름으로 변경한다.</li>
</ul>
</li>
<li>그렇게하면 dbid가 변경되고, DB 이름은 동일하게 유지된다.</li>
</ul>
<h3 id="nid-유틸리티">NID 유틸리티</h3>
<ul>
<li>New Databases Identifier 유틸리티는 Oracle Database의 DBID(Identifier)및 DBNAME을 변경할 수 있는 도구이다.</li>
</ul>
<h3 id="db_unique_name과-database-global-name의-차이점은">DB_UNIQUE_NAME과 database global name의 차이점은?</h3>
<ul>
<li>db_unique_name은 globally하게 고유한 이름을 지정한다. </li>
<li>동일한 db domain 내에서 동일한 db_name을 가진 database에는 고유한 DB_UNIQUE_NAME이 있어야 한다.</li>
<li>Global Name은 일반적으로 Global Name이 true로 설정된 경우에만 활성화되며, 데이터베이스의 링크 보안에 영향을 미친다. <ul>
<li>db_link는 원격 데이터베이스의 global name과 동일해야 한다.</li>
</ul>
</li>
</ul>
<h2 id="sid-변경-테스트-single일-때">SID 변경 테스트 (Single일 때)</h2>
<ul>
<li>export ORACLE_SID=CUBJIN 변경<pre><code></code></pre></li>
</ul>
<p>$ echo $ORACLE_SID
CUBJIN</p>
<pre><code>
- $ORACLE_HOME/dbs에서 pfile 생성</code></pre><p>$ ls -al
total 41800
drwxr-xr-x.  2 oracle dba     4096 Feb 28 20:28 .
drwxr-xr-x. 71 oracle dba     4096 Jan  8 23:26 ..
-rw-r-----   1 oracle dba 10715136 Jan 30 12:50 c-1372511915-20250130-00
-rw-r-----   1 oracle dba 10715136 Jan 30 13:15 c-1372511915-20250130-01
-rw-r-----   1 oracle dba 10715136 Jan 30 14:07 c-1372511915-20250130-02
-rw-rw----   1 oracle dba     1544 Feb 28 20:28 hc_CUBJIN.dat
-rw-rw----.  1 oracle dba     1544 Feb 28 20:24 hc_ORACUB.dat
-rw-r--r--   1 oracle dba     1141 Feb 28 20:27 initCUBJIN.ora👈
-rw-r--r--.  1 oracle dba     3079 May 14  2015 init.ora
-rw-r--r--   1 oracle dba     1080 Jan 29 14:08 initORACUB_250129.ora
-rw-r--r--   1 oracle dba     1141 Feb 27 21:51 initORACUB.ora
-rw-r--r--   1 oracle dba    12288 Feb 27 21:52 .initORACUB.ora.swp
-rw-r-----.  1 oracle dba       24 Jan  7 23:21 lkORACUB
-rw-r-----.  1 oracle dba     2048 Jan  8 00:12 orapwORACUB
-rw-r-----   1 oracle dba 10600448 Jan 30 14:07 snapcf_ORACUB.f
-rw-r-----   1 oracle dba     3584 Feb 27 21:55 spfileORACUB.ora</p>
<p>```</p>
<ul>
<li><p>sqlplus&gt; startup;</p>
</li>
<li><p>ps -ef | grep pmon으로 확인</p>
</li>
</ul>