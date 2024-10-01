<h1 id="대기대기-이벤트">대기/대기 이벤트</h1>
<table>
<thead>
<tr>
<th><strong>구분</strong></th>
<th><strong>대기 (Wait)</strong></th>
<th><strong>대기 이벤트 (Wait Event)</strong></th>
</tr>
</thead>
<tbody><tr>
<td><strong>정의</strong></td>
<td>프로세스가 자원을 사용하기 위해 기다리는 상태</td>
<td>프로세스가 대기하는 동안의 특정한 이유 또는 상황</td>
</tr>
<tr>
<td><strong>목적</strong></td>
<td>필요한 자원을 얻기 위해 대기하는 시간의 누적</td>
<td>어떤 자원 때문에 대기하는지 분석하기 위한 정보 제공</td>
</tr>
<tr>
<td><strong>종류</strong></td>
<td>CPU 대기, I/O 대기 등 다양한 형태</td>
<td><code>db file sequential read</code>, <code>latch free</code> 등 세부 이벤트</td>
</tr>
<tr>
<td><strong>특징</strong></td>
<td>자원을 기다리는 시간 자체를 의미</td>
<td>대기가 발생한 구체적인 원인을 파악하는 데 사용</td>
</tr>
<tr>
<td><strong>분석 방법</strong></td>
<td>전체적인 대기 시간의 파악</td>
<td>특정 대기 이벤트를 통해 성능 문제를 진단 및 해결</td>
</tr>
<tr>
<td><strong>예시</strong></td>
<td>디스크 I/O 대기 시간, CPU 대기 시간 등</td>
<td><code>buffer busy waits</code>, <code>log file sync</code> 등 특정 이벤트</td>
</tr>
</tbody></table>
<br />

<ul>
<li><code>대기</code>: 기다린다를 표시하는 것 뿐이다.</li>
<li><code>대기 이벤트</code>: 기다리게 만든 작업</li>
</ul>
<hr />
<h1 id="syssystem">SYS/SYSTEM</h1>
<ul>
<li>오라클 기본 계정<h2 id="sys">SYS</h2>
</li>
<li>오라클 슈퍼 유저(super user)계정으로, 데이터베이스에서 발생하는 모든 문제를 처리할 수 있는 계정이다.<h2 id="system">SYSTEM</h2>
</li>
<li>오라클 데이터베이스 관리 및 유지보수(maintenance)를 위한 DBA(Database Administrator)계정으로 SYS 사용자와의 차이는, 데이터베이스 생성 권한이 없고 불완전 복구를 할 수 없다는 것</li>
</ul>
<hr />
<h1 id="locklatch">Lock/Latch</h1>
<ul>
<li>래치와 락은 데이터베이스에서 동시성 제어를 위해 사용되는 메커니즘이지만, 그 목적과 동작 방식에 차이가 있다.<h2 id="lock">Lock</h2>
</li>
<li><code>비유</code>: 건물의 출입문을 잠그는 것과 비슷하다. 건물 전체를 사용하는 사람들을 위해 문을 잠그고, 그 문을 열기 전까지는 다른 사람이 들어올 수 없다.</li>
<li>이 과정은 시간이 오래 걸리고, 여러 사람이 기다려야 할 수 있다.</li>
</ul>
<blockquote>
<ul>
<li><code>락(Lock)</code>: 락은 데이터 무결성을 보장하기 위해 트랜잭션이 데이터에 액세스할 때 사용됩니다. 데이터의 일관성을 유지하고 여러 트랜잭션이 동시에 데이터에 접근하는 것을 제어하는 데 사용되며, 트랜잭션 단위에서 장기간 유지되는 경우가 많습니다. 락은 데이터 레코드, 테이블, 데이터블록 등 디스크에 저장된 데이터에 대한 동시성 제어에 주로 사용됩니다.</li>
</ul>
</blockquote>
<h2 id="latch">Latch</h2>
<ul>
<li><p><code>비유</code>: 건물의 회전문이나 엘리베이터 문 같은 역할이다. 문을 사용할 때 잠깐 다른 사람이 들어오지 못하게 잠그는 것으로, 짧은 시간만 잠그고 바로 해제된다. 한 번에 한 사람만 통과할 수 있지만, 잠금 해제 속도가 매우 빠르다.</p>
</li>
<li><p>오버헤드가 매우 작고, 성능에 미치는 영향이 거의 없다.</p>
</li>
<li><p>래치는 데이터베이스의 내부 구조를 보호하기 위한 잠금</p>
</li>
<li><p>시스템의 빠른 동작을 유지하기 위해 설계되었다.</p>
</li>
</ul>
<blockquote>
<ul>
<li>래치(Latch): 래치는 짧은 기간 동안의 메모리 또는 데이터 구조를 보호하기 위해 사용됩니다. 주로 메모리 내에서 발생하는 동시 액세스 문제를 해결하기 위해 사용되며, 빠른 속도로 잠금 및 해제 작업이 이루어집니다. 래치는 데이터베이스의 버퍼 캐시, 메모리 블록, 내부 데이터 구조 등을 보호하는 데 사용됩니다.</li>
</ul>
</blockquote>