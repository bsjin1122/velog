<blockquote>
<p>시스템의 성능과 응답 시간에 직접적인 영향을 주는 대기 이벤트로, 
실제로 작업을 수행하는 동안 발생하는 대기 현상을 의미한다.</p>
</blockquote>
<h2 id="1-db-file-sequential-read">1. db file sequential read</h2>
<ul>
<li>인덱스를 통해, 테이블의 특정 행을 읽을 때 발생</li>
<li>주로 인덱스 스캔이나, ROWID를 통한 액세스 시 발생, 하나의 블록을 읽는 작업이다.</li>
</ul>
<h2 id="2-db-file-scattered-read">2. db file scattered read</h2>
<ul>
<li>여러 개의 연속된 블록을 동시에 읽을 때 발생하는 대기 이벤트로, 주로 테이블 풀 스캔 시 발생한다.</li>
<li>원인: 테이블의 대용량 데이터 스캔이나, 적절한 인덱스가 없을 때</li>
</ul>
<h2 id="3-buffer-busy-waits">3. buffer busy waits</h2>
<ul>
<li>프로세스가 필요한 버퍼를 다른 프로세스가 사용 중이거나, 버퍼가 디스크에서 아직 읽혀오지 않은 경우 발생하는 대기 이벤트이다.</li>
<li>원인: 동시에 같은 데이터 블록에 접근하려는 프로세스가 많을 때 발생</li>
</ul>
<h2 id="4-log-file-sync">4. log file sync</h2>
<ul>
<li>트랜잭션이 커밋될 때, 로그 버퍼의 내용을 로그 파일에 기록하는 작업을 기다릴 때 발생하는 대기 이벤트이다.</li>
<li>원인: 많은 커밋 또는 롤백 작업이 동시에 발생, 로그 파일에 대한 I/O 성능이 낮을 때 발생</li>
</ul>
<h2 id="5-latch-free">5. latch free</h2>
<ul>
<li>래치가 사용 중일 때 다른 프로세스가 해당 래치를 사용하려 대기하는 경우, 발생하는 대기 이벤트</li>
<li>원인: 래치 경합이 심할 때 또는 래치 사용이 빈번할 때 발생</li>
</ul>
<h2 id="6-enq-tx---row-lock-contention">6. enq: TX - row lock contention</h2>
<ul>
<li>두 트랜잭션이 동일한 데이터 행에 대한 변경을 시도할 때 발생하는 대기 이벤트</li>
<li>원인: 데이터 잠금 경합이 발생할 때 나타나며, 특히 동시 업데이트가 많을 때 발생한다.</li>
</ul>
<h2 id="7-log-file-parallel-write">7. log file parallel write</h2>
<ul>
<li>로그 파일에 대한 병렬 쓰기 작업을 기다릴 때 발생하는 대기 이벤트이다.</li>
<li>원인: 많은 양의 데이터 변경 작업이 발생하거나, 로그 파일에 대한 I/P 성능이 낮을 때 발생</li>
</ul>
<h2 id="8-free-buffer-waits">8. free buffer waits</h2>
<ul>
<li>데이터 블록을 읽기 위해, 사용 가능한 빈 버퍼를 찾는 데 시간이 걸릴 때 발생하는 대기 이벤트</li>
<li>원인: 많은 양의 데이터 변경 작업이 발생하거나, 로그 파일에 대한 I/O 성능이 낮아 데이터 변경 내용의 체크 포인트 처리가 지연되는 경우 발생</li>
<li>DBWR(DB Writer) 프로세스가 적시에 변경된 블록을 디스크에 기록하지 못하는 경우도 있다.</li>
</ul>
<blockquote>
<p>해결방안</p>
</blockquote>
<ul>
<li>DB_CACHE_SIZE 파라미터를 증가시켜 버퍼 캐시의 크기를 늘립니다.</li>
<li>I/O 성능을 개선하여 로그 파일 쓰기 속도를 높입니다.</li>
<li>데이터베이스에서 체크포인트 발생 빈도를 조절하거나, DBWR 프로세스의 수를 늘려주면 도움이 될 수 있습니다.</li>
</ul>