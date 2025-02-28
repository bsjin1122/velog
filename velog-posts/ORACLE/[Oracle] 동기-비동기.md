<h1 id="동기synchronous와-비동기asynchronous">동기(Synchronous)와 비동기(Asynchronous)</h1>
<h2 id="동기">동기</h2>
<ul>
<li>작업 요청 후, 해당 작업이 완료될 때까지 기다리는 방식</li>
<li>작업이 끝난 후에야 다음 작업이 진행됨</li>
<li>작업 순서가 엄격히 보장되며, 요청과 응답이 한 번에 이루어지며, 작업 완료 여부를 즉시 확인할 수 있다.</li>
<li>Redo Log 쓰기: Oracle의 트랜잭션이 커밋될 때 Redo Log가 디스크에 기록되는 작업은 동기적으로 처리된다. 데이터 무결성과 장애 발생 시 복구를 보장하기 위해 반드시 디스크에 기록이 완료된 후, 커밋이 성공적으로 반환된다.</li>
<li>Data Guard(SYNC 모드): 주(Primary) 데이터베이스의 트랜잭션이 커밋되기 전에, 복제 데이터(Standby)로 해당 트랜잭션 데이터가 전송 및 적용될 때까지 기다린다.</li>
</ul>
<h2 id="비동기asynchronous">비동기(Asynchronous)</h2>
<ul>
<li>작업 요청 후, 작업이 완료되기 전에 다음 작업으로 진행할 수 있는 방식.</li>
<li>작업 완료 여부는 별도로 확인하거나 콜백 방식으로 알림을 받는다.</li>
<li>작업 순서가 엄격히 보장되지 않을 수 있다.</li>
<li>병렬 처리가 가능하며, 처리 속도가 빠르다.</li>
<li>비동기 I/O: 오라클은 데이터를 디스크에서 읽거나 쓸 때, 비동기 I/O를 사용하여 I/O 요청이 완료되기를 기다리지 않고 다음 작업을 처리한다.</li>
<li>Data Guard(ASYNC 모드): 주 데이터베이스의 트랜잭션이 커밋될 때, 복제 데이터베이스로 데이터를 전송하지만, 트랜잭션 커밋이 복제 데이터베이스에 의존하지 않는다.</li>
<li>SQL*Net: 클라이언트와 서버 간 통신에서 비동기 방식으로 네트워크 작업을 처리</li>
</ul>
<h2 id="redo-log와-동기--비동기">Redo Log와 동기 / 비동기</h2>
<ul>
<li><p>동기 쓰기: 트랜잭션이 커밋되기 전에 Redo Log 버퍼의 데이터가 디스크에 완전히 기록될 때까지 기다린다.</p>
</li>
<li><p>비동기 쓰기: 커밋 작업과, Redo Log 쓰기를 독립적으로 처리한다. LGWR 프로세스가 데이터를 디스크에 쓸 때 커밋 시점과 독립적으로 처리한다.</p>
</li>
</ul>