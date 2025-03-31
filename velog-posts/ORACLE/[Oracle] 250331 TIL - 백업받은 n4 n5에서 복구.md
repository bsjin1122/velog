<blockquote>
<ul>
<li>select sum(bytes)/1024/1024 from dba_data_files; 로 확인</li>
</ul>
</blockquote>
<ul>
<li>df -h 로 백업받을 공간 확인</li>
<li>불필요한 백업 삭제 </li>
<li>n4: level 0 백업 받기<ul>
<li>SID 맞춰주기</li>
</ul>
</li>
<li>n5: export ORACLE_SID로 맞춰주기<ul>
<li>backup spfile</li>
<li>rman&gt; set dbid=n4의dbid</li>
<li>rman&gt; restore spfile</li>
<li>startup force (open된 상태에서 abort하고 재startup)</li>
<li>create pfile 생성 후 spfile은 백업으로 파일명 바꾸기 </li>
<li>restore spfile from 'directory'</li>
<li>startup mount pfile='directory';</li>
<li>(restore datafile &lt;&lt; ASM에서<del>~</del>)</li>
</ul>
</li>
</ul>
<h3 id="n4-level-0-백업-받기">n4: level 0 백업 받기</h3>
<pre><code class="language-shell">#!/bin/bash

$ORACLE_HOME/bin/rman target / nocatalog &lt;&lt; EOF

run {
allocate channel c1 device type disk;
allocate channel c2 device type disk;
allocate channel c3 device type disk;
allocate channel c4 device type disk;

# level 0
backup
incremental level 0
database
not backed up 1 times
format '/BSJ/BACKUP/dbf.%t_%s_%d_%U'
section size 10g
filesperset 2;

# archivelog
sql 'alter system archive log current';
backup (archivelog all format '/BSJ/BACKUP/arc.%t_%s_%d' DELETE ALL INPUT);

# controlfile
backup format '/BSJ/BACKUP/ctl.%t_%s_%d_%U'(current controlfile);

release channel c1;
release channel c2;
release channel c3;
release channel c4;
}

exit
EOF

find /u01/app/oracle/product/19c/dbhome_1/dbs -type f -daystart -mtime 0 -exec rm -f {} \;</code></pre>
<hr />
<h3 id="오늘-날짜로-된-것-rm-삭제"><a href="https://freewing.tistory.com/120#google_vignette">오늘 날짜로 된 것 rm 삭제</a></h3>
<ul>
<li><code>find /u01/app/oracle/product/19c/dbhome_1/dbs -type f -daystart -mtime 0 -exec rm -f {} \;</code></li>
</ul>
<h2 id="파괴왕-일지">파괴왕 일지</h2>
<ol>
<li><p>SID ps -ef 로 확인했을 때 잘못된 거 못찾고 변경 못하고 있던 것 </p>
</li>
<li><p>OS 메모리와 sga_target 메모리 사이즈 변경 </p>
<ul>
<li><code>cat /proc/meminfo</code></li>
<li><code>free -h</code></li>
<li>OS에서의 메모리 사이즈는 약 7g인데, pfile 파라미터의 sga_target은 10g를 할당하려 하고 있었다.</li>
</ul>
</li>
</ol>
<ul>
<li><a href="https://support.oracle.com/knowledge/Oracle%20Database%20Products/1922934_1.html">ORA-27104</a><pre><code class="language-shell">[BasicStep.handleNonIgnorableError:470]  ORA-27104: system-defined limits for
shared memory was misconfigured</code></pre>
</li>
</ul>
<ol start="3">
<li><a href="https://api.velog.io/rss/@greendev">Hugepage, 파라미터 USE_LARGE_PAGES</a></li>
</ol>
<h2 id="궁금한-점">궁금한 점</h2>
<ul>
<li>initCUBJIN.ora 관련 에러메시지가 있었는데, 꼭 pfile로 실행해야 하나...?</li>
<li></li>
</ul>