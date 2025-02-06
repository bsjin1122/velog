<ul>
<li>asmlib 사용하기 전 개념을 모르고 있기에 먼저 정리할 겸 적어둔다. </li>
<li>ASM은 클러스터를 지원하는 논리 볼륨 관리자(LVM)이며, 오라클의 물리적 데이터베이스 구조를 저장하기 위해 사용된다.</li>
</ul>
<h3 id="lvmlogical-volume-manager">LVM(Logical Volume Manager)</h3>
<ul>
<li>기본적으로 논리 볼륨(Logical Volume, LV)을 사용하여 디스크 공간을 유연하게 관리할 수 있도록 구성된다.</li>
</ul>
<h3 id="주요-구성-요소">주요 구성 요소</h3>
<ol>
<li>Physical Volume(PV, 물리 볼륨)</li>
</ol>
<ul>
<li>실제 물리적 디스크(/dev/sdb, /dev/sdc 등) 또는 기존 파티션을 LVM이 사용할 수 있도록 초기화한 것이다.
<code>pvcreate /dev/sdb /dev/sdc</code></li>
</ul>
<ol start="2">
<li>Volume Group (VG, 볼륨 그룹)</li>
</ol>
<ul>
<li>여러 개의 PV를 묶어 하나의 논리적 저장소처럼 사용하도록 만드는 그룹
<code>vgcreate my_vg /dev/sdb /dev/sdc</code></li>
</ul>
<ol start="3">
<li>Logical Volume (LV, 논리 볼륨)</li>
</ol>
<ul>
<li>VG에서 필요한 만큼 할당하여 생성된 가상 디스크 파티션</li>
</ul>
<ol start="4">
<li>Filesystem (파일 시스템)</li>
</ol>
<ul>
<li>LV 위에 파일 시스템을 생성하여 마운트해서 사용
<code>mkfs.ext4 /dev/my_vg/my_lv</code></li>
<li><strong>/etc/fstab 이란?</strong></li>
<li>Linux에서 파일 시스템을 자동으로 마운트하는 설정 파일</li>
<li>역할: 시스템이 부팅될 때 자동으로 특정 파일 시스템(디스크, LVM, 네트워크 스토리지 등)을 마운트하도록 설정</li>
<li>UUID 또는 디바이스 이름을 기반으로 파일 시스템을 마운트 가능</li>
</ul>
<h2 id="lvm을-사용하는-이유">LVM을 사용하는 이유</h2>
<ol>
<li>디스크 크기 동적 조정 가능</li>
</ol>
<ul>
<li>기존 파티션 시스템 (ext4, xfs 등)에서는 디스크 크기를 변경하려면 데이터 백업 -&gt; 파티션 재설정-&gt; 데이터 복구 과정이 필요</li>
<li>LVM을 사용하면 논리 볼륨 크기를 쉽게 확장/축소 가능</li>
</ul>
<ol start="2">
<li>여러 개의 디스크를 하나로 합칠 수 있다.</li>
</ol>
<ul>
<li>RAID처럼 여러 개의 물리적 디스크를 하나의 논리적 볼륨으로 묶을 수 있음</li>
<li>디스크를 추가하면서 용량을 확장할 수 있기 때문에, 대형 저장소 관리에 유리</li>
</ul>
<ol start="3">
<li>스냅샷(Snapshot) 기능 제공</li>
</ol>
<ul>
<li>특정 시점의 데이터를 유지하는 스냅샷 기능 지원 -&gt; 백업 및 복구에 유리</li>
</ul>