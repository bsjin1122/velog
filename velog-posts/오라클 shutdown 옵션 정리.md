<h2 id="1-기본-옵션-shutdown">1. 기본 옵션 (shutdown)</h2>
<ul>
<li>가장 일반적인 종료 방법</li>
<li>특별한 옵션을 지정하지 않으면, 이 방법으로 데이터베이스가 종료된다.<h3 id="동작-방식">동작 방식</h3>
</li>
<li>현재 연결된 <strong>모든 세션이 종료될 때까지 기다린다.</strong></li>
<li><strong>데이터 파일과 컨트롤 파일에 변경된 내용</strong>을 모두 기록하고, 안전하게 닫는다.</li>
</ul>
<p>** 사용 시기**</p>
<ul>
<li>정상적인 종료를 원할 때, 데이터베이스에 연결된 모든 세션이 안전하게 종료될 때까지 기다릴 수 있는 상황에서 사용한다.</li>
</ul>
<hr />
<h2 id="2-transactional-shutdown-transactional">2. TRANSACTIONAL (shutdown transactional)</h2>
<ul>
<li>현재 진행중인 <strong>트랜잭션이 완료될 때까지 기다리고 종료</strong></li>
</ul>
<h3 id="-동작-방식">** 동작 방식**</h3>
<ul>
<li>현재 연결된 세션 중 트랜잭션이 완료될 때까지 기다린 후에 커넥션을 끊는다.</li>
<li>트랜잭션이 없는 세션은 즉시 종료된다.<ul>
<li>트랜잭션이 완료된 후, 데이터 파일과 컨트롤 파일에 변경된 내용을 모두 기록하고, 데이터베이스를 종료한다.</li>
</ul>
</li>
</ul>
<p>** 사용 시기**</p>
<ul>
<li>중요한 트랜잭션이 실행중일 때, 그 트랜잭션이 끝날 때까지 기다리고 싶을 때 사용</li>
<li>ex) 대규모 데이터 처리 작업이 끝날 때까지 기다릴 때 유용</li>
</ul>
<hr />
<h2 id="3-immediate-shutdown-immediate">3. IMMEDIATE (shutdown immediate)</h2>
<ul>
<li><strong>즉시 종료</strong><ul>
<li>현재 세션에 있는 트랜잭션이 더 이상 기다리지 않고, 종료<h3 id="동작-방식-1">동작 방식</h3>
</li>
</ul>
</li>
<li>현재 실행 중인 트랜잭션을 중단하고, <strong>세션을 즉시 종료</strong></li>
<li>아직 커밋되지 않은 트랜잭션은 롤백된다.<ul>
<li>데이터베이스의 상태는 안전하게 유지되며, 데이터 파일과 컨트롤 파일에 변경된 내용이 기록된 후 종료된다.</li>
</ul>
</li>
</ul>
<p>** 사용 시기**</p>
<ul>
<li>빠르게 데이터베이스를 종료해야 하거나, 더 이상 진행중인 트랜잭션이 필요 없을 때 사용</li>
<li>데이터베이스를 즉시 닫아야 할 때 많이 사용된다.</li>
</ul>
<hr />
<h2 id="4-abort-shutdown-abort">4. ABORT (shutdown abort)</h2>
<ul>
<li><strong>강제 종료</strong><ul>
<li>데이터베이스를 즉시 종료하지만, <strong>데이터 파일에 변경된 내용이 기록되지 않고 종료</strong><h3 id="동작-방식-2">동작 방식</h3>
</li>
</ul>
</li>
<li>데이터베이스가 바로 종료되며, <strong>모든 트랜잭션이 중단</strong></li>
<li>커밋되지 않은 모든 트랜잭션은 사라진다.</li>
<li>데이터베이스는 다시 시작할 때 복구 과정이 필요할 수 있다.</li>
</ul>
<p>** 사용 시기**</p>
<ul>
<li>긴급하게 데이터베이스를 종료해야 하는 상황에서 사용한다.</li>
<li>ex) 데이터베이스가 멈추거나 응답하지 않을 때 강제로 종료할 수 있다.<ul>
<li>But, 이후 데이터베이스를 시작 시 복구가 필요하므로 주의</li>
</ul>
</li>
</ul>
<hr />
<table>
<thead>
<tr>
<th>옵션</th>
<th>커넥션의 종료를 기다리는가?</th>
<th>변경된 데이터를 데이터 파일에 기록하는가?</th>
</tr>
</thead>
<tbody><tr>
<td>없음(기본)</td>
<td>커넥션의 종료를 기다린다.</td>
<td>YES</td>
</tr>
<tr>
<td>transactional</td>
<td>트랜잭션이 끝나는 것을 기다린다. 트랜잭션이 끝나면 커넥션을 끊어 버린다.</td>
<td>YES</td>
</tr>
<tr>
<td>immediate</td>
<td>NO. 커밋하지 않은 데이터는 없어지지 않는다.</td>
<td>YES</td>
</tr>
<tr>
<td>abort</td>
<td>NO. 커밋하지 않은 데이터는 없어지지 않는다.</td>
<td>NO</td>
</tr>
</tbody></table>
<p><strong>참고:</strong>  </p>
<ul>
<li>데이터베이스의 커넥션 풀을 유지하기 위해 커넥션 풀(connection pool)을 사용하는 경우에는 애플리케이션이 종료할 때까지 커넥션을 종료하지 않습니다. 따라서 커넥션 풀을 사용 중인 오라클을 정지하기 위해서는 필수적으로 옵션을 지정해야 할 때가 있습니다.</li>
</ul>