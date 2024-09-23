<h2 id="ha-high-availability-고가용성">HA (High Availability) 고가용성</h2>
<ul>
<li><p>싱글로 사용되는 것!</p>
</li>
<li><p>RAC 개념이 HA(고가용성)에도 속한 것이지만, 한국에서는 개념을 다르게 사용한다. </p>
</li>
<li><p>OS Cluster(Oracle 기능 아님!!) 기능을 사용해서, OS를 2개 각각 구성한다.</p>
</li>
<li><p>각 OS에는 Public IP(고정; PIP), Virtual IP(VIP;가상이라는 뜻 아님! 미국에선 <code>실제</code>라는 뜻이라고 한다)를 설정한다. Virtual IP만이 다른 서버를 바라볼 수 있다고 한다.</p>
</li>
<li><p>평소에 싱글로 사용하다가, OS 1번째 것이 장애가 났을 경우, Virtual IP로 향하게 사용할 수 있는 것이라고 한다.</p>
</li>
<li><p>+a 로 또 다른 방식으로는 스토리지에 /ORACLE_HOME으로 설치해 사용하는 방법이 있을 수 있다고 한다. (라이선스 비용이 비쌀 경우에 사용되는 방법) </p>
</li>
</ul>
<h2 id="rac-real-application-clusters">RAC (Real Application Clusters)</h2>
<ul>
<li><p>오라클 개념 중 가장 어려운 방법</p>
</li>
<li><p>Active-Active로 구성</p>
</li>
<li><p>두 개의 인스턴스가 하나의 DB를 바라본다. </p>
<ul>
<li>두 개 이상의 노드가 될 수 있지만(초기의 컨셉으로, select문을 많이 쓰지만 DML 용량을 적게 가져가자는 취지였던 것 같음) 현재는 고성능의 RAC 구성을 유지하기 위해 two node를 사용한다고 한다.</li>
</ul>
</li>
<li><p>두 노드 중 하나가 장애가 났을 경우, voting disk라는 것이 두 노드 중간에 연결되어 있는데</p>
<ul>
<li>(Oracle Clusterware가 관리하는 공유 스토리지에 저장되며, ASM(Automatic Storage Management)을 통해 관리되거나 SAN(Storage Area Network) 등에 배치될 수 있습니다.)</li>
</ul>
</li>
<li><p>voting disk가 둘 중 누가 장애가 났어? 첫번째거? 그러면 분리할게! 해주는 역할이라고 한다.</p>
</li>
</ul>
<h2 id="ogg-oracle-golden-gate">OGG (Oracle Golden Gate)</h2>
<ul>
<li>이번에 U2L로 전환하는 프로젝트이므로, 엔디안이 다르기 때문에 한 번 XTTS로 변환해준 다음 통째로 옮기면 된다고 한다.<ul>
<li>XTTS: 엔디안이 다른 플랫폼 간에 테이블스페이스를 빠르게 전송할 수 있다. </li>
</ul>
</li>
<li>DB의 마이그일 경우엔, rowid의 주소값이 달라지게 되므로 이부분을 맞춰주는 작업? 이 필요한 것 같다. OGG말고 이부분은 좀 더 학습이 필요하다..</li>
</ul>