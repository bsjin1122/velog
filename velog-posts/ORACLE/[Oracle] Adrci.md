<h2 id="adrci">ADRCI</h2>
<ul>
<li>자동 진단 리포지토리 AutoDiagnostic Repository</li>
<li>상태 모니터 report 표시</li>
<li>Oracle support service에 전달하기 위해 incident 및 문제 정보를 zip파일로 packaging</li>
<li>진단 데이터에는 incident 및 문제에 대한 설명, trace file, dump, 상태 모니터 report, alert*.log entry 등이 포함되어 있다.</li>
</ul>
<h2 id="용어">용어</h2>
<ul>
<li><p>problem: database에서 발생되는 critical error</p>
</li>
<li><p>incident: 문제가 1회 발생된 것을 말함.</p>
</li>
<li><p>problem_key: 모든 trouble에는 key가 할당되어 있다. error code 등을 포함하는 텍스트 문자열로, 1개 이상 파라메터를 포함하기도 한다. </p>
</li>
<li><p>incident package: 1개 이상의 문제에 대한 incident data 집합. package를 생성한 후에, package에 외부파일을 추가하거나, package 안에 file을 선택해서 삭제하거나 package 안에서 선택한 파일을 수정하여 기밀 데이터를 삭제하는 것도 가능하다.</p>
</li>
<li><p>finalize: adrci로 논리 package로부터 물리 package를 생성하기 전에, package를 finalize할 필요가 있다.</p>
</li>
<li><p>home path: hoem path에 의해 adr home이 결정된다. adr home path가 계층 내 adr home directory level에 의해 디렉토리를 유일하게 나타내는 경우에는 이 디렉토리 보다 하위의 모든 adrci home이 current가 된다.</p>
</li>
<li><p>ADRCI EXEC=&quot;SHOW HOMES; SHOW INCIDENT&quot;
배치 모드로 명령어를 사용할 때, 위와 같이 사용할 수 있다.</p>
<ul>
<li>show tracefile </li>
</ul>
</li>
<li><p>해당 디렉토리 안에서 파일명이 mmon을 포함한 모든 trace file을 표시한다.</p>
<ul>
<li><code>SHOW TRACEFILE %mmon% -PATH /home/steve/temp</code></li>
</ul>
</li>
<li><p>SHOW INCIDENT -MODE BRIEF</p>
</li>
<li><p>SHOW INCIDENT -MODE DETAIL</p>
</li>
</ul>
<pre><code class="language-shell">[oracle@ora19cn1 20250101-21:10:23]:ORABSJ:[/oramedia/RU24]
$ adrci -help
Syntax:
   adrci [-help] | [script=script_filename]
         | [exec = &quot;one_command [;one_command;...]&quot;]

Options      Description                     (Default)
-----------------------------------------------------------------
script       script file name                (None)
help         help on the command options     (None)
exec         exec a set of commands          (None)
-----------------------------------------------------------------
</code></pre>
<hr />
<pre><code class="language-sql">ADR base = &quot;/u01/app/oracle&quot;
adrci&gt; help

 HELP [topic]
   Available Topics:
        CREATE REPORT
        ECHO
        ESTIMATE
        EXIT
        HELP
        HOST
        IPS
        PURGE
        RUN
        SELECT
        SET BASE
        SET BROWSER
        SET CONTROL
        SET ECHO
        SET EDITOR
        SET HOMES | HOME | HOMEPATH
        SET TERMOUT
        SHOW ALERT
        SHOW BASE
        SHOW CONTROL
        SHOW HM_RUN
        SHOW HOMES | HOME | HOMEPATH
        SHOW INCDIR
        SHOW INCIDENT
        SHOW LOG
        SHOW PROBLEM
        SHOW REPORT
        SHOW TRACEFILE
        SPOOL

 There are other commands intended to be used directly by Oracle, type
 &quot;HELP EXTENDED&quot; to see the list

adrci&gt;
</code></pre>
<h3 id="명령어">명령어</h3>
<ul>
<li>CREATE REPORT<ul>
<li>지정한 report type과 실행id의 report를 생성해 그 report를 adr로 저장한다.</li>
</ul>
</li>
<li>HOST<ul>
<li>os 명령어 사용이 가능하다.</li>
<li>host &quot;ls -al&quot;</li>
</ul>
</li>
<li>IPS<ul>
<li>incident package service를 호출한다. </li>
<li>ips add</li>
<li>ips add file</li>
<li>ips add new incidents</li>
<li>ips copy in file</li>
<li>ips copy out file</li>
<li>ips create package</li>
<li>ips get manifest</li>
<li>ips pack</li>
<li>ips remove</li>
<li>ips set configuration </li>
<li>ips show configuration</li>
<li>ips show package</li>
<li>ips unpack file</li>
</ul>
</li>
<li>PURGE : 현재 리포지토리에 따라 CURRENT adr hoem 내 진단 데이터를 삭제한다.<ul>
<li>purge [-i {id | start_id end_id} | </li>
<li>age mins [-type {ALERT|INCIDENT|TRACE|CDUMP|HM|UTSCDMP}]]</li>
</ul>
</li>
<li>QUIT</li>
<li>RUN</li>
<li>SCRIPT</li>
<li>SELECT<ul>
<li>관련된 필드</li>
<li>ex) select incident_id, create_time from incident where incident_id &gt; 1</li>
</ul>
</li>
<li>SHOW REPORT<ul>
<li>지정한 report type 및 실행명의 report를 표시한다. </li>
<li>현재는 hm_run(상태 모니터 레포트) type만이 xml 형식으로 support 되어있다. </li>
</ul>
</li>
<li>SPOOL<ul>
<li>SPOOL filename [[APPEND]|[OFF]]</li>
<li>filename: 출력이 보내지는 파일명 path가 없을 경우, current adrci 작업 디렉토리에 생성되어진다. </li>
<li>set home 할 필요가 없다.</li>
<li>파일 확장자가 지정되지 않은 경우, default 확장자ㅁ여은 .ado로 지정된다. </li>
</ul>
</li>
</ul>
<pre><code class="language-shell">adrci&gt; spool myfile
adrci&gt; spool myfile.ado append
Currently spooling to myfile
adrci&gt; spool off
adrci&gt; spool'
DIA-48415: Syntax error found in string [spool'] at column [6]

adrci&gt; spool
Not spooling
adrci&gt; exit
[oracle@ora19cn1 20250101-21:54:51]:ORABSJ:[/oramedia/RU24]
$ ls
36582781  myfile.ado  PatchSearch.xml
[oracle@ora19cn1 20250101-21:54:52]:ORABSJ:[/oramedia/RU24]
$ vi myfile.ado
[oracle@ora19cn1 20250101-21:54:57]:ORABSJ:[/oramedia/RU24]
$ cat myfile.ado
Currently spooling to myfile
[oracle@ora19cn1 20250101-21:55:02]:ORABSJ:[/oramedia/RU24]
$
</code></pre>
<ul>
<li>SHOW HM_RUN 상태 모니터 실행에 관한 모든 정보를 표시한다.</li>
</ul>
<h3 id="incident-package">incident package</h3>
<h4 id="1-논리-incident-package-생성">1. 논리 incident package 생성</h4>
<ul>
<li><p>adr 내 메타데이터로서만 존재하기 위한 논리 패키지</p>
</li>
<li><p>논리패키지로부터 물리 패키지를 생성하기까지는 내용이 포함되지 않는다.</p>
</li>
<li><p>논리 패키지는 패키지 번호가 할다오디기 때문에, 이후의 명령어에서 이 번호를 사용해서 패키지를 참조한다.</p>
<h4 id="2-incident-package-로의-진단정보의-추가">2. incident package 로의 진단정보의 추가</h4>
</li>
<li><p>incident 번호, 에러 번호, 에러 키 또는 시간 간격에 기반한 논리 패키지를 생성한 경우, 이 순서는 옵션이 도니다. </p>
</li>
<li><p>package에 incident 를 추가하거나, adr내 파일을 package에 추가하는 것이 가능하다.</p>
<h4 id="3-물리-incident-package-생성">3. 물리 incident package 생성</h4>
</li>
<li><p>지정한 디렉토리 내 zip 파일로 추가된다. </p>
</li>
<li><p><code>IPS GENERATE PACKAGE package_number IN path</code></p>
</li>
<li><p>IPS GENERATE PACKAGE package_number IN path INCREMENTAL</p>
</li>
<li><p>증분 파일에는 같은 논리 패키지에 대해 zip 파일이 마지막으로 생성된 이후에 추가 혹은 변경된 진단 파일 모두가 포함된다.</p>
</li>
<li><p>zip 파일 </p>
<ul>
<li>packageName_mode_sequence.zip</li>
<li>packageName: error key 일부와 타임스탬프로 구성</li>
<li>mode: com, inc (완전, 증분)</li>
<li>sequence: 정수</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>기존 package에 adr 내 파일을 추가할 때 <ul>
<li><code>IPS ADD FILE filespec PACKAGE package_number</code></li>
</ul>
</li>
</ul>
<h2 id="ips-creategenerate-package">ips {create/generate} package</h2>
<h3 id="ips-create-package">IPS CREATE PACKAGE</h3>
<ul>
<li>새로운 IPS 패키지<h3 id="ips-generate-package">IPS GENERATE PACKAGE</h3>
</li>
<li>기존에 생성된 IPS 패키지를 기반으로 최종 패키지를 생성</li>
</ul>