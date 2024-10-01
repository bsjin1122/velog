<blockquote>
<ul>
<li>Lock(잠금) 종류를 나타내며, TX(트랜잭션), TM(테이블)에 대한 잠금을 나타낸다.</li>
</ul>
</blockquote>
<h2 id="tx-lock-transaction-lock">TX Lock (Transaction Lock)</h2>
<ul>
<li><p>트랜잭션 잠금(Transaction Lock)으로, 오라클의 가장 일반적인 행 수준(Row-level) 잠금이다.</p>
</li>
<li><p>주요 역할: 두 개 이상의 트랜잭션이 동일한 데이터에 동시에 액세스하고 변경하려 할 때 데이터 무결성을 보장한다.</p>
<h3 id="언제-발생하는가">언제 발생하는가?</h3>
</li>
<li><p>데이터 변경 작업 (INSERT, UPDATE, DELETE) 수행 시</p>
</li>
<li><p>행이 변경되었고, 해당 트랜잭션이 아직 커밋되지 않은 상태일 때</p>
</li>
<li><p>트랜잭션이 동일한 행에 대한 동시 액세스를 방지하여 충돌을 피하고 데이터의 일관성을 유지하기 위해 잠금이 발생한다.</p>
</li>
</ul>
<hr />
<h2 id="tm-locktable-lock">TM Lock(Table Lock)</h2>
<ul>
<li><p>테이블 잠금(Table Lock)으로, 테이블 수준의 데이터 변경을 보호한다.</p>
</li>
<li><p>주요 역할: 테이블에 대한 구조적 변경이나, DML(데이터 조작 언어) 작업 시 데이터 무결성을 보장하며, 데이터베이스 객체의 무결성 및 참조 무결성을 유지한다.</p>
</li>
</ul>
<h3 id="언제-발생하는가-1">언제 발생하는가?</h3>
<ul>
<li>INSERT, UPDATE, DELETE 작업 수행 시 잠금이 걸리며, 특히 외래 키 (FK)가 있는 테이블에 대해 작업할 때 TM Lock 이 중요하다.</li>
<li>테이블을 변경하는 DDL(CREATE, ALTER&lt; DROP) 작업을 수행할 때도 발생한다.<h3 id="잠금-모드">잠금 모드</h3>
</li>
<li>여러 잠금모드가 존재하며, 그 중 가장 일반적으로는 Share Lock, Exclusive Lock이 있다.</li>
<li>DML 작업 시에는 일반적으로 ROW Exclusive 또는, Row Share 잠금이 설정된다.<h3 id="예시">예시</h3>
</li>
<li>부모-자식 관계에 있는 테이블에서, 자식 테이블이 외래 키(FK) 제약이 설정되어 있을 경우, 부모 테이블에 대한 업데이트 작업이 수행되면, TM Lock이 발생하여 데이터 무결성을 유지한다.<h3 id="주요-대기-이벤트">주요 대기 이벤트</h3>
</li>
<li><code>enq: TM - contention</code>: 테이블 수준에서의 잠금 경합을 나타낸다.</li>
</ul>
<hr />
<h2 id="tx와-tm-lock-예시비유">TX와 TM Lock 예시/비유</h2>
<h3 id="예시-1">예시</h3>
<ul>
<li>만약 두 개의 트랜잭션이 부모 테이블과, 자식 테이블이 외래 키 제약 관계로 연결되어 있을 때, 
자식 테이블에 행을 삽입하려 한다면,</li>
</ul>
<blockquote>
<ul>
<li>TM Lock은 자식 테이블에 삽입되는 행에 대해 설정된다.</li>
</ul>
</blockquote>
<ul>
<li>동시에, 부모 테이블에 대해 TX Lock이 설정된다.</li>
</ul>
<h3 id="비유">비유</h3>
<ul>
<li><p><code>TX Lock</code>: 회사의 회의실에서, 각 직원이 잠시 앉아있는 상황. 직원들이 회의실을 점유하고 회의가 끝나기 전까지는 다른 사람이 들어올 수 없다. 회의실 점유 상태가 TX Lock</p>
</li>
<li><p><code>TM Lock</code>: 건물의 전체 층을 공사하기 위해 일부 지역을 막아둔 상황. 이때, 층 전체에 대한 접근을 통제하는 것이 TM Lock</p>
</li>
</ul>