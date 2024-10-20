<blockquote>
<p>OCI 오라클 클라우드에 서버 하나 만들고.... 
oracle 공홈에서 확인해서 다운 받았는데 .exe 파일로 떨어져서 아닌데.... 싶어서 일단 </p>
</blockquote>
<ul>
<li><a href="https://www.oracle.com/kr/database/technologies/oracle19c-linux-downloads.html">19c 설치 .rpm</a>에서 다운 받기로 했다.</li>
<li>혹시 몰라 filezilla에도 접속해두었다. --&gt; puttygen 통해서 private key를 .ppk 형식으로 바꿔주고 접속했다.</li>
</ul>
<ol>
<li><p>filezilla에서 rpm 파일 업로드</p>
</li>
<li><p><code>sudo rpm -ivh oracle-database-ee-19c-1.0-1.x86_64.rpm</code>으로 설치 진행</p>
</li>
<li><p>설정 스크립트 실행: <code>sudo /etc/init.d/oracledb_ORCLCDB-19c configure</code></p>
</li>
</ol>
<blockquote>
<pre><code class="language-shell">[opc@instance-20241017-2246 ~]$ sudo /etc/init.d/oracledb_ORCLCDB-19c configure
Configuring Oracle Database ORCLCDB.
Prepare for db operation
8% complete
Copying database files
31% complete
Creating and starting Oracle instance
32% complete
36% complete
..
40% complete
43% complete
46% complete
Completing Database Creation
51% complete
54% complete
Creating Pluggable Databases
58% complete
77% complete
Executing Post Configuration Actions
100% complete
Database creation complete. For details check the logfiles at:
 /opt/oracle/cfgtoollogs/dbca/ORCLCDB.
Database Information:
Global Database Name:ORCLCDB
System Identifier(SID):ORCLCDB
Look at the log file &quot;/opt/oracle/cfgtoollogs/dbca/ORCLCDB/ORCLCDB.log&quot; for further details.
</code></pre>
</blockquote>
<p>Database configuration completed successfully. The passwords were auto generated, you must change them by connecting to the database using 'sqlplus / as sysdba' as the oracle user.
...</p>
<pre><code>
4. oracle 사용자로 전환: `sudo su - oracle`


5. 환경변수 설정
```bash
export ORACLE_HOME=/opt/oracle/product/19c/dbhome_1
export PATH=$ORACLE_HOME/bin:$PATH
export ORACLE_SID=ORCLCDB</code></pre><ol start="6">
<li>sqlplus 접속 : <code>sqlplus / as sysdba</code></li>
</ol>
<blockquote>
<pre><code class="language-bash">[oracle@instance-20241017-2246 ~]$ sqlplus / as sysdba
</code></pre>
</blockquote>
<p>SQL*Plus: Release 19.0.0.0.0 - Production on Sun Oct 20 04:00:06 2024
Version 19.3.0.0.0</p>
<blockquote>
</blockquote>
<p>Copyright (c) 1982, 2019, Oracle.  All rights reserved.</p>
<blockquote>
</blockquote>
<p>Connected to:
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.3.0.0.0</p>
<pre><code>
7. 비밀번호 재설정

&gt;```sql
ALTER USER SYS IDENTIFIED BY 새로운비밀번호;
ALTER USER SYSTEM IDENTIFIED BY 새로운비밀번호;</code></pre><p>-- 버전 확인</p>
<pre><code class="language-sql">SQL&gt; select * from v$version;

BANNER
--------------------------------------------------------------------------------
BANNER_FULL
--------------------------------------------------------------------------------
BANNER_LEGACY
--------------------------------------------------------------------------------
    CON_ID
----------
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production
Version 19.3.0.0.0
Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production</code></pre>