<h2 id="data-block의-경합">Data Block의 경합</h2>
<ul>
<li><p>row수가 적은 table이나 row 길이가 짧은 table에 대해, 빈번하게 update나 select를 행하면, 전체 노드로부터 경합이 이루어진다.</p>
</li>
<li><p>application에서 사용하는 table예시</p>
<ul>
<li><p>queue에서 사용되는 table</p>
<ul>
<li>메시지 큐, 작업 대기열</li>
</ul>
</li>
<li><p>session이나 job의 상태관리 테이블</p>
<ul>
<li><p>session 상태 관리: 로그인 상태, 웹 애플리케이션의 세션 데이터</p>
</li>
<li><p>job 상태: 배치 작업의 실행 상태 </p>
</li>
</ul>
</li>
<li><p>마지막에 행한 처리를 확인하는 테이블</p>
<ul>
<li>ex) 최근 로그인 기록, 마지막 거래 내역 저장</li>
<li>최근 변경 내역이 빈번히 갱신됨</li>
</ul>
</li>
</ul>
</li>
<li><p>PCTFREE를 증가시키는 것으로, 1개 블록당 행 수를 감소시키는 것이 가능하다.</p>
</li>
</ul>
<hr />
<h2 id="pctfree-parameter">PCTFREE parameter</h2>
<ul>
<li><p>블록 내 기존의 행을 갱신할 경우에 대비하여 data block내에 빈 영역으로써 보관되는 비율을 최소치로 설정한다.</p>
</li>
<li><p>예를 들어, <code>CREATE TABLE문</code>에서 다음과 같이 parameter를 설정한다. <code>PCTFREE 20</code></p>
<pre><code class="language-sql">CREATE TABLE emp (
  emp_id NUMBER PRIMARY KEY,
  emp_name VARCHAR2(50),
  salary NUMBER
) PCTFREE 20;
</code></pre>
</li>
</ul>
<pre><code>- 이 값에 의해, 이 테이블의 Data segment 내 각 데이터, 블록의 20%가 빈 상태로 유지된다.
- 이 비어있는 영역은, 각 블록 내 기존 행이 갱신될 경우에 사용된다.
  - 만약 pctfree 공간이 부족하면, oracle은 행을 새로운 블록으로 이동(row migration)하거나, 블록을 분할(block split)하게 됨
- `즉, 한 블록이 완전히 꽉 차지 않도록 남겨둠으로써, update시 블록 분할(block split), 또는 row migration(행 마이그레이션)을 방지하는 역할을 한다.`

### PCTUSED (Percent Used)
- 데이터 블록이 다시 INSERT를 받을 수 있도록 허용되는 최소한의 사용률을 설정하는 파라미터
- PCTFREE+PCTUSED &lt;= 100%가 되어야 함

```sql
ex) PCTFREE 20, PCTUSED 40이면
- 블록이 80%까지 채워지면 insert 불가
- 데이터가 삭제되어 블록 사용률이 40% 미만이 되면 다시 insert 가능</code></pre><h3 id="freelist">FREELIST</h3>
<ul>
<li><p>새로운 데이터를 삽입할 때 사용할 수 있는 블록 목록</p>
</li>
<li><p>PCTFREE 설정이 높으면, 더 많은 블록이 FREELIST에 추가되어 새로운 데이터가 분산됨</p>
</li>
<li><p>DELETE가 발생하여 블록이 일정 수준 이하(PCTUSED미만)로 비워지면, 다시 FREELIST에 추가된다.</p>
<pre><code class="language-SQL">[ FREELIST에 추가 및 제거되는 과정 ]

  INSERT 가능 블록 목록 (FREELIST)
 ┌────────┬───────┬─────────┐
 │ BLK 1 │ BLK 2 │ BLK 3 │  ← INSERT 가능
 └────────┴───────┴─────────┘

  ↓ (INSERT 발생하여 BLK 1이 꽉 참 → FREELIST에서 제거됨)

 ┌────────┬───────┐
 │ BLK 2 │ BLK 3 │  ← INSERT 가능
 └────────┴───────┘

  ↓ (DELETE 발생하여 BLK 1이 일정 수준 이하로 비워짐)

 ┌─────────┬───────┬───────┐
 │ BLK 1  │ BLK 2 │ BLK 3│  ← INSERT 가능 (BLK 1 다시 추가)
 └─────────┴───────┴───────┘
</code></pre>
</li>
</ul>
<pre><code>### INITRANS (Initial Transactions)
- 하나의 데이터블록에서 동시에 실행할 수 있는 최소 트랜잭션 수를 정의하는 파라미터
- 다중 트랜잭션 환경에서 경합(Blocking)을 방지하는 역할을 함
- 테이블 생성 시 기본적으로 INITRANS = 1로 설정됨

** 동작 방식**
&gt; 1. 데이터블록에 트랜잭션 슬롯이 생성됨
2. 트랜잭션이 실행될 때마다 슬롯을 차지함
3. INITRANS를 초과하는 경우, 남은 공간을 사용하여 추가 슬롯 생성  (하지만 블록 내 공간이 부족하면 경합 발생이 가능)</code></pre>