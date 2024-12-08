<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/75fc2664-82dc-4d7b-8af0-46367b89e8bd/image.png" /></p>
<blockquote>
<p>그림을 보고 설명할 수 있을 정도로... 글로 풀면서 정리를 시작해볼 예정.. ✍️</p>
</blockquote>
<h1 id="필수-프로세스">필수 프로세스</h1>
<h2 id="dbwr-database-writer">DBWR (Database Writer)</h2>
<ul>
<li>Database Buffer Cache에서 변경 완료 후, Dirty Block을 데이터 파일로 저장하는 역할 </li>
<li>SQL&gt; show parameter processes;
<code>db_writer_process</code> 개수 확인</li>
</ul>
<blockquote>
<h3 id="🤔-dbwr가-db-buffer-cache의-dirty-buffer의-내용을-파일에-내려쓰는-경우">🤔 DBWR가 DB Buffer Cache의 Dirty Buffer의 내용을 파일에 내려쓰는 경우</h3>
</blockquote>
<ol>
<li>Checkpoint 신호가 발생했을 때</li>
<li>Dirty Buffer가 임계값을 지날 때 </li>
<li>Time out이 발생했을 때</li>
<li>RAC Ping이 발생했을 때<ul>
<li>노드 간 통신 점검(서로의 상태를 주기적으로 확인)<ul>
<li>클러스터 간 네트워크(LAN)과 디스크 기반 네트워크(Shared Disk)를 통해 이루어짐</li>
</ul>
</li>
<li>Cache Fusion은 RAC에서 각 노드의 버퍼 캐시를 통합하여 공유 데이터베이스를 운영할 수 있게 하는 메커니즘</li>
</ul>
</li>
<li>Tablespace가 Read only 상태로 변경될 때</li>
<li>Tablespace가 offline될 때</li>
<li>Tablespace가 begin backup 상태가 될 때</li>
<li>Drop table이나 , Truncate Table 될 때</li>
<li>Direct Path Read/Write 가 진행될 때 </li>
<li>일부 Parallel Query 작업이 진행될 때</li>
</ol>
<h2 id="lgwr-log-writer">LGWR (Log Writer)</h2>
<ul>
<li>데이터가 변경되면, Server Process가 변경 내역(Change Vector)를 Redo Log Buffer에 기록</li>
<li>LGWR는 Redo Log Buffer에 있는 내용을 디스크의 Redo Log File로 저장한다.</li>
</ul>
<blockquote>
<h3 id="🎨-lgwr가-수행될-때">🎨 LGWR가 수행될 때</h3>
</blockquote>
<ol>
<li>Commit이 발생했을 때</li>
<li>1/3이 찼을 때</li>
<li>변경량이 1M가 되었을 때</li>
<li>3초 마다</li>
<li>DBWR가 내려쓰기 전에</li>
</ol>
<p style="color: red;">※ Commit을 수행하면 디스크로 데이터를 저장하는 게 아니라, Redo Log를 저장하는 것이다.</p>

<h2 id="pmon-process-monitor">PMON (Process Monitor)</h2>
<ul>
<li>모든 서버 프로세스들을 감시하고, 비정상적으로 종료된 프로세스가 있다면 관련 복구작업 등을 하는 역할 </li>
</ul>