<blockquote>
<p>D+14 240923월 </p>
</blockquote>
<ul>
<li>일본어 공부하던 때가 생각난다. 공부 방식이 비슷한 것 같은 느낌이 든다.</li>
</ul>
<h2 id="dbca">DBCA</h2>
<ul>
<li>Database Configuration Assistant로, Oracle DB를 생성, 삭제 또는 구성 시 사용하는 GUI 도구를 의미한다.<ul>
<li>흔한 GUI창..!
<img alt="" src="https://velog.velcdn.com/images/greendev/post/6cfca131-7700-418e-b225-0137f942b295/image.png" /> </li>
</ul>
</li>
</ul>
<hr />
<h2 id="bcv-business-continuance-volume">BCV (Business Continuance Volume)</h2>
<ul>
<li>스토리지 시스템에서 사용하는 용어</li>
<li>특정 시점의 데이터를 빠르게 복사, 비즈니스 연속성을 보장</li>
<li>스토리지 레벨에서 데이터를 실시간으로 또는 주기적으로 복사하여 백업하는 방식
&lt;- 운영 데이터에 영향 주지 않고, 데이터를 복구할 수 있는 복사본을 유지 </li>
</ul>
<h3 id="내가-이해한-bcv">내가 이해한 BCV</h3>
<ul>
<li><p>ASM 구성으로 땅덩어리를 만들어놓고, RAC로 구성된 데이터베이스에 BCV로 구성해서 미러링할 수 있도록 한다.</p>
<ul>
<li>+a로 SAN(전용망이라고 생각하면 된다) SRDF에도 BCV로 복제를 해둔다.</li>
</ul>
</li>
<li><p>ex1) 00시 시점의 데이터를 불러와! 한다면, </p>
<ul>
<li>BCV에서 split하여 00시 시점에 운영 DB와 연결을 분리한 다음, 운영 DB에서 떨어지는 아카이브 파일을 보면서 변경분을 찾거나, 반영해간다고 생각했다.</li>
</ul>
</li>
<li><p>ex2) 운영중인 DB에 손상이 생겼을 경우</p>
<ul>
<li>BCV로 구성된 DB를 운영중이던 DB와 분리(split)한다.</li>
<li>운영 DB 가동을 못하게 되니까 SRDF에 있는 db로 운영하게 된다.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="보완">보완</h2>
<h3 id="1-bcv의-역할">1. BCV의 역할</h3>
<ul>
<li>BCV는 특정 시점의 데이터 복제본을 생성하여 운영 데이터베이스에 영향을 주지 않고 백업 및 복구에 활용하는 데 사용된다. 이를 통해 비즈니스 연속성을 보장한다.</li>
</ul>
<h3 id="2-asm과-rac-환경에서의-bcv">2. ASM과 RAC 환경에서의 BCV</h3>
<ul>
<li>ASM: Automatic Storage Management</li>
<li>RAC: Real Application Clusters</li>
<li>ASM 구성: BCV 볼륨을 ASM 디스크 그룹에 할당하면 복제본이 ASM 환경에서 관리될 수 있다.</li>
<li>RAC 구성: RAC 환경에서 BCV를 구성하면 노드 간 데이터 동기화에 BCV 복제본을 활용하여 고가용성 및 데이터 보호를 유지할 수 있다.</li>
</ul>
<h3 id="3-srdf-와-bcv">3. SRDF 와 BCV</h3>
<ul>
<li>SRDF(Symmetrix Remote Data Facility)</li>
<li>SRDF는 SAN 환경에서 스토리지 간 데이터 복제를 수행하는 EMC의 솔루션</li>
<li>BCV와 SRDF를 함께 사용하면 한 스토리지 장비에서 다른 스토리지로 데이터 복제를 수행하며, 재해 복구 시에도 빠른 전환이 가능</li>
</ul>
<p><br /><br /><br /></p>
<blockquote>
<p>비즈니스에서 가장 중요한 것은 고객</p>
</blockquote>
<ul>
<li>수요가 있어야 제품이 만들어지고, 쓰인다.</li>
</ul>