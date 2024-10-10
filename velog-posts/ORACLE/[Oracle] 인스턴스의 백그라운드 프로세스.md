<ul>
<li>출처: <a href="https://t1.daumcdn.net/cfile/tistory/1145DB344FF5B5193C">오라클 구조 pdf</a>
<img alt="" src="https://velog.velcdn.com/images/greendev/post/5fe593df-9c9b-4b51-b3d3-fb671f8d43a6/image.png" /></li>
</ul>
<h2 id="dbwr-database-writer">DBWR (Database Writer)</h2>
<ul>
<li><p>DBWR 프로세스는 SGA 내에 존재하는 데이터베이스 버퍼 캐시로부터 
데이터베이스 블록을 디스크 상의 데이터파일에 쓴다.</p>
</li>
<li><p>오라클 인스턴스는 <code>DBW0~DBW9까지 최대 10개의 DBWR 프로세스를 가질 수 있고</code>, 이 프로세스들은 여러 개의 데이터파일에 I/O 작업을 수행한다.</p>
</li>
<li><p>대부분의 인스턴스는 하나의 DBWR를 사용한다.</p>
</li>
<li><p>대부분의 인스턴스는 하나의 DBWR를 사용한다. </p>
</li>
</ul>
<h3 id="데이터베이스-버퍼-캐시로부터-데이터베이스-블록을-데이터파일에-쓰는-2가지-경우">데이터베이스 버퍼 캐시로부터 데이터베이스 블록을 데이터파일에 쓰는 2가지 경우</h3>
<p>** 1. 오라클이 체크포인트를 수행할 필요가 있는 경우 **</p>
<ul>
<li><p>데이터 파일의 블록을 변경하여 리두 로그와 일치하도록 하기 위해</p>
</li>
<li><p>트랜잭션이 커밋될 때 트랜잭션에 대한 리두를 기록한 다음, 실제 블록을 쓴다.</p>
</li>
<li><p>정기적으로 오라클은 데이터파일의 내용을 커밋된 트랜잭션에 대해 기록된 리두와 일치시키기 위해 체크포인트를 수행한다. </p>
</li>
</ul>
<p><strong>2. 오라클이 사용자가 요청한 블록을 캐시로 읽어들이고자 하는데, 버퍼 캐시 내에 충분한 공간이 없는 경우</strong></p>
<ul>
<li><p>데이터파일에 쓰여지는 블록은 가장 이전에 사용된(LRU, Least recently used)블록이다.</p>
<ul>
<li>이러한 순서로 블록을 쓰는 이유: 버퍼 캐시에서 해당 블록을 사용하지 못해서 생기는 성능상의 영향을 최소화하기 위함</li>
</ul>
</li>
</ul>
<h2 id="lgwrlog-writer">LGWR(Log Writer)</h2>
<ul>
<li><p>SGA 내에 존재하는 로그 버퍼로부터 리두 정보를 디스크 상의 현재 리두로그 파일의 모든 복사본에 쓴다. </p>
</li>
<li><p>트랜잭션이 진행됨에 따라 관련 리두 정보는 SGA 내의 리두 로그 버퍼에 저장된다.</p>
</li>
<li><p>트랜잭션이 커밋될 때, 오라클은 리두 정보를 디스크에 쓰기 위해 LGWR 프로세스를 호출함으로써 리두 정보를 영구적으로 기록한다.</p>
</li>
</ul>
<h2 id="smonsystem-monitor">SMON(System Monitor)</h2>
<ul>
<li><p>오라클의 상태와 안전을 안정적으로 유지한다.</p>
</li>
<li><p>장애 후에 인스턴스가 시작될 때, 장애 복구를 수행한다.</p>
</li>
<li><p>또한 Oracle Parallel Server/Real Application Clusters의 경우와 같이 하나 이상의 인스턴스가 동일한 데이터베이스를 액세스할 경우, 인스턴스 장애가 발생하면 이에 대한 복구를 수행한다.</p>
</li>
<li><p>SMON은 사용하지 않는 여러 조각의 공간을 하나로 합침으로써 데이터파일 내의 공간을 정리하고, 행 정렬에 사용된 공간이 더 이상 필요없는 경우에 이를 제거한다.</p>
</li>
</ul>
<h2 id="pmon-process-monitor">PMON (Process Monitor)</h2>
<ul>
<li>데이터베이스를 액세스하는 사용자 프로세스를 감시한다.</li>
<li>사용자 프로세스가 비정상적으로 종료한 경우, PMON은 해당 사용자 프로세스가 불필요하게 할당하고 있는 (메모리 등과 같은) 자원과 잠금(lock)을 해제한다.</li>
</ul>
<h2 id="archarchiver">ARCH(Archiver)</h2>
<ul>
<li><p>오라클이 리두로그 파일을 채우면, 해당 리두로그 파일을 채우면 해당 리두 로그 파일을 읽고, 사용된 리두 로그 파일의 복사본을 지정된 아카이브 로그 위치(들)에 쓴다.</p>
</li>
<li><p>오라클 8i는 ARCn형태로 표시되며, 최대 ARCH 프로세스를 지원한다.</p>
</li>
<li><p>LGWR는 업무량에 따라, 초기화 매개변수 LOG_ARCHIVE_MAX_PROCESS 가 지정한 한도까지 필요에 따라 ARCH 프로세스를 띄운다.</p>
</li>
</ul>
<h2 id="ckptcheckpoint">CKPT(Checkpoint)</h2>
<ul>
<li>DBWR와 함께 체크포인트를 수행한다.</li>
<li>CKPT는 체크포인트가 완료되면, 체크포인트 데이터의 갱신을 위해 제어 파일과 데이터벵이스 파일 헤더를 갱신한다.</li>
</ul>
<h2 id="recorecover">RECO(Recover)</h2>
<ul>
<li>RECO 프로세스는 자동으로 장애가 발생한 트랜잭션이나, 일시중지된 트랜잭션을 복구한다.</li>
</ul>
<h1 id="데이터-딕셔너리">데이터 딕셔너리</h1>
<ul>
<li><p>오라클 데이터베이스는 메타 데이터, 혹은 데이터 구조를 표현하는 데이터의 집합을 갖고있다. </p>
</li>
<li><p>이러한 메타데이터를 저장하는 테이블과 뷰를 Oracle Data Ditctionary라고 일컫는다.</p>
</li>
<li><p><code>동적 테이블</code>: V$, GV$ 접두어가 붙은 데이터 딕셔너리 테이블은 오라클 데이터베이스의 현 상태를 반영하기 위해 지속적으로 변경되는 동적 테이블이다. </p>
</li>
<li><p><code>정적 테이블</code>: DBA_, ALL_, USER_</p>
<ul>
<li>뷰에 열거된 객체의 범주를 표시하기 위해</li>
</ul>
</li>
</ul>
<br />

<table>
<thead>
<tr>
<th>구성요소</th>
<th>데이터 딕셔너리 테이블과 뷰</th>
</tr>
</thead>
<tbody><tr>
<td>데이터베이스</td>
<td>V$DATABASE</td>
</tr>
<tr>
<td>테이블스페이스</td>
<td>DBA_TABLESPACES, DBA_DATA_FILES, DBA_FREE_SPACE</td>
</tr>
<tr>
<td>제어 파일</td>
<td>V$CONTROLFILE, V$PARAMETER, V$CONTROLFILE_RECORD_SECTION</td>
</tr>
<tr>
<td>데이터파일</td>
<td>V$DATAFILE, V$DATAFILE_HEADER, V$FILESTAT, DBA_DATA_FILES</td>
</tr>
<tr>
<td>세그먼트</td>
<td>DBA_SEGMENTS</td>
</tr>
<tr>
<td>익스텐트</td>
<td>DBA_EXTENTS</td>
</tr>
<tr>
<td>리두 스레드, 그룹, 멤버</td>
<td>V$THREAD, V$LOG, V$LOGFILE</td>
</tr>
<tr>
<td>아카이빙 상태</td>
<td>V$DATABASE, V$LOG, V$ARCHIVED_LOG, V$ARCHIVE_DEST</td>
</tr>
<tr>
<td>데이터베이스 인스턴스</td>
<td>V$INSTANCE, V$PARAMETER, V$SYSTEM_PARAMETER</td>
</tr>
<tr>
<td>메모리 구조</td>
<td>V$SGA, V$SGASTAT, V$DB_OBJECT_CACHE, V$SQL, V$SQLTEXT, V$SQLAREA</td>
</tr>
<tr>
<td>백그라운드 프로세스</td>
<td>V$BGPROCESS, V$SESSION</td>
</tr>
</tbody></table>