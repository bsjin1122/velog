<blockquote>
<p>Clusterware 기동 절차 그림 보다가 헷갈려서... 기록겸 정리한다.</p>
<ul>
<li><strong>출처</strong></li>
</ul>
</blockquote>
<ul>
<li><a href="https://docs.oracle.com/cd/E57425_01/121/OSTMG/GUID-B7A61F3B-C22A-4021-A846-F5EA749E79FF.htm">Oracle ADVM Volume Manager 개요</a></li>
<li><a href="https://docs.oracle.com/cd/E57425_01/121/OSTMG/GUID-545C311D-24C6-421A-ACBE-CA29E1FDA0A6.htm">Oracle Flex ASM 개요</a></li>
</ul>
<h1 id="advm-asm-dynamic-volume-manager">ADVM (ASM Dynamic Volume Manager)</h1>
<ul>
<li><p>ASM 위에서 동작하는 볼륨 매니저 </p>
<ul>
<li><p>ASM 디스크 그룹을 마치 일반적인 파일 시스템처럼 사용할 수 있도록 지원하는 기능이다.</p>
</li>
<li><p>비데이터베이스 파일(예: 로그 파일, 애플리케이션 파일 등)도 ASM 스토리지를 활용할 수 있다.</p>
</li>
</ul>
</li>
<li><p>볼륨 관리 서비스와, Client와의 표준 Disk Driver Interface를 제공한다.</p>
</li>
<li><p>File System과 그 외 Diskbase Application으로부터는  벤더사의 OS상의 Storage Device(ex: SAN, DAS, NAS와 같은 OS에서 직접 마운트하는 스토리지)인 경우와 마찬가지로, I/O Request가 Oracle ADVM Volume Device로 송신된다. </p>
<ul>
<li>일반적인 스토리지처럼 인식되어 사용 가능하다.</li>
<li>Oracle ADVM이 기본적인 스토리지 역할을 수행하며, I/O 요청을 받아 처리한다는 뜻.</li>
</ul>
</li>
</ul>
<h2 id="설명">설명</h2>
<ul>
<li><p>Oracle ADVM은 ASM 동적 볼륨으로부터 구성된다.</p>
</li>
<li><p>각 Oracle ASM Disk Group 내에서는 1개 이상의 Oracle ADVM Volume Divice를 구성할 수 있다.</p>
</li>
<li><p>ADVM 드라이버는, Oracle ADVM Volume Device에 대한 I/O Request를 Oracle Disk Group 내 대응하는 Oracle ASM 동적 볼륨 및 Disk Set 내 블록에 Map한다.</p>
</li>
<li><p>ASM Volume Manager 기능을 Export해서, 비정상적인 System정지, Oracle ASM Instance 장애 혹은 System 장애가 발생한 경우에도 Volume Mirror 일관성이 유지되는 것을 보증한다.</p>
</li>
<li><p>Oracle ADVM Volume File로서 할당하고 있는 Oracle ASM 기억 장소에 Disk Driver Interface를 제공하는 것으로, Oracle ASM 을 확장시킨다.</p>
</li>
<li><p>File System을 포함하는 가상 디스크 생성에 사용할 수 있다. Oracle ADVM볼륨에 포함된 이러한 파일 시스템은, Oracle Database File의 범위를 초과하는 File(실행 가능한 File, Report File, Trace File, Alert.log, 그 밖의 Application Datafile등) 지원이 가능하다.</p>
</li>
<li><p>실제로는 Oracle ASM 파일이기 때문에, Oracle ASM 파일과 같은 관리 권한이 필요하다.</p>
</li>
</ul>
<h3 id="acfs">ACFS</h3>
<ul>
<li><p>Oracle Automatic Storage Management Cluster File System (Oracle ACFS)는 ADVM Interface를 통해 Oracle ASM과 통신한다. </p>
</li>
<li><p>Oracle ADVM을 추가하는 것에 의해, Oracle ASM은 Database File과 데이터베이스 파일 이외의 파일 양쪽 요건을 충족하는 User Data의 완전한 Storage Solution이 된다.</p>
</li>
<li><p>출처 사이트 제공 기준 12.1여서.. </p>
<ul>
<li>Oracle ASM디스크 그룹에 볼륨을 추가하기 위해서는, Disk Group 속성 COMPATIBLE.ASM 및 COMPATIBLE.ADVM을 '11.2'로 설정할 필요가 있다.</li>
<li><code>ALTER DISKGROUP my_diskgroup SET ATTRIBUTE 'COMPATIBLE.ASM' = '11.2';</code></li>
</ul>
</li>
</ul>
<blockquote>
<h3 id="주의">주의</h3>
</blockquote>
<ul>
<li>동적 볼륨은, 기존의 Device Partitioning을 대체하며, 각 볼륨은 각각 이름이 부여되어, 단일 파일 시스템용으로 구성될 수 있다. Oracle ADVM 볼륨은 필요에 따라 동적으로 생성 및 크기 조정이 가능하며, 물리적 디바이스 및 관련 파티셔닝 방식보다 유연하다.</li>
</ul>
<h3 id="advm을-관리하는-구문">ADVM을 관리하는 구문</h3>
<ul>
<li>ALTER DISKGROUP ADD | RESIZE |DROP | ENABLE | DISABLE | MODIFY VOLUME SQL。</li>
</ul>
<ol>
<li>볼륨 추가 (ADD VOLUME)<pre><code class="language-sql">ALTER DISKGROUP my_diskgroup(ASM 디스크 그룹이름) ADD VOLUME my_volume(새로 생성할 볼륨 이름) SIZE 100G(볼륨 크기);</code></pre>
</li>
<li>볼륨 크기 조정 (RESIZE VOLUME)</li>
</ol>
<ul>
<li><code>ALTER DISKGROUP my_diskgroup RESIZE VOLUME my_volume SIZE 200G;</code></li>
</ul>
<ol start="3">
<li>볼륨 삭제 (DROP VOLUME)</li>
</ol>
<ul>
<li><code>ALTER DISKGROUP my_diskgroup DROP VOLUME my_volume;</code></li>
</ul>
<ol start="4">
<li>볼륨 활성화 (ENABLE VOLUME)</li>
</ol>
<ul>
<li><code>ALTER DISKGROUP my_diskgroup ENABLE VOLUME my_volume;</code></li>
</ul>
<ol start="5">
<li>볼륨 비활성화 (DISABLE VOLUME)</li>
</ol>
<ul>
<li><code>ALTER DISKGROUP my_diskgroup DISABLE VOLUME my_volume;</code></li>
</ul>
<ol start="6">
<li>볼륨 속성 수정 (MODIFY VOLUME)</li>
</ol>
<ul>
<li><code>ALTER DISKGROUP my_diskgroup MODIFY VOLUME my_volume NAME new_volume_name;</code></li>
</ul>
<hr />
<h2 id="차이">차이</h2>
<table>
<thead>
<tr>
<th>비교 항목</th>
<th>ASM (Automatic Storage Management)</th>
<th>ADVM (ASM Dynamic Volume Manager)</th>
</tr>
</thead>
<tbody><tr>
<td><strong>기능</strong></td>
<td>데이터베이스 파일 저장 및 관리</td>
<td>일반적인 파일 저장 가능 (비DB 파일)</td>
</tr>
<tr>
<td><strong>파일 시스템 지원 여부</strong></td>
<td>X (ASM 자체로는 파일 시스템 없음)</td>
<td>O (ACFS와 함께 파일 시스템 제공)</td>
</tr>
<tr>
<td><strong>데이터 저장 범위</strong></td>
<td>오라클 데이터베이스 전용 파일 (Datafile, Redo Log 등)</td>
<td>OS에서 마운트 가능, 애플리케이션 파일 저장 가능</td>
</tr>
<tr>
<td><strong>볼륨 관리</strong></td>
<td>디스크 그룹을 자동으로 관리</td>
<td>ASM 디스크 그룹 위에서 논리 볼륨 생성 가능</td>
</tr>
<tr>
<td><strong>운영체제 접근성</strong></td>
<td>OS에서 직접 접근 불가 (Oracle Instance 필요)</td>
<td>OS에서 파일 시스템으로 마운트 가능</td>
</tr>
<tr>
<td><strong>사용 예시</strong></td>
<td>데이터베이스 저장</td>
<td>애플리케이션 로그, 바이너리 파일, 일반 데이터 파일 저장</td>
</tr>
</tbody></table>
<h3 id="oracle-asm">Oracle ASM</h3>
<ul>
<li>Oracle이 제공하는 파일 시스템 + 볼륨 관리자 역할을 하는 자동 스토리지 관리 시스템</li>
<li>데이터베이스 파일 (예: 데이터 파일, 로그 파일, 컨트롤 파일 등) 전용</li>
<li>일반적인 파일 시스템처럼 파일을 직접 다룰 수 없다.<ul>
<li>데이터베이스 전용 스토리지 관리 시스템으로 파일 시스템 없이 동작한다.</li>
<li>이때문에 OS에서 직접 접근할 수 없으며, 일반적인 파일(로그 파일, 애플리케이션 파일 등) 저장할 수 없다.<ul>
<li>이를 해결하려면, ADVM(ASM Dynamic Volume Manager) + 파일 시스템이 필요하다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="advm">ADVM</h3>
<ul>
<li>ASM 디스크 그룹 위에서 동적 볼륨(Dynamic Volume) 생성 가능<ul>
<li>ASM 디스크 위에 볼륨을 생성하고, 이를 파일 시스템으로 마운트 가능하게 해줌<ul>
<li>파일 시스템: 마운트 후 접근 가능하다. 파일시스템을 사용하려면, ADVM + ACFS를 적용해야 한다.</li>
</ul>
</li>
</ul>
</li>
<li>일반 파일 저장 가능 -&gt; 실행 파일, 로그 파일, 애플리케이션 데이터 등 </li>
<li>기존 파일 시스템(Linux EXT4, Windows NTFS)처럼 파일을 관리할 수 있음</li>
<li>데이터베이스뿐만 아니라, 애플리케이션도 ASM  스토리지를 활용할 수 있도록 지원</li>
</ul>
<blockquote>
<p>둘을 함께 사용하면 데이터베이스와 애플리케이션 모두 ASM을 활용할 수 있다.</p>
</blockquote>
<ul>
<li>ASM은 데이터베이스 파일 전용, ADVM은 ASM을 일반 파일 저장용으로 확장하는 기능</li>
</ul>