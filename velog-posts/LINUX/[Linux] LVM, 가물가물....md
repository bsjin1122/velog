<h1 id="요약">요약</h1>
<blockquote>
<p><code>LVM</code>은 파티션을 유연하게 묶어서 디스크 그룹처럼 쓰는 시스템이고, 그 과정은</p>
</blockquote>
<ul>
<li>파티션 → PV → VG → LV → 포맷 &amp; 마운트 → fstab 등록 흐름으로 진행!</li>
</ul>
<ul>
<li>여러 개의 디스크(또는 파티션)을 하나로 묶어 사용하는 기술</li>
<li>공간을 유연하게 관리하기 위해</li>
<li>하드디스크를 추가하거나, 크기를 늘릴 때, 개별 디스크 단위가 아니라 하나의 그룹처럼 관리 가능</li>
</ul>
<blockquote>
<ul>
<li>하나의 큰 논리적 공간(VG: Volume Group)을 만들고, 이 안에서 필요한 만큼 LV(Logical Volume)를 나눠서 사용</li>
</ul>
</blockquote>
<h3 id="pvphysical-volume">PV(Physical Volume)</h3>
<ul>
<li>실제 물리 디스크 또는 파티션</li>
</ul>
<h3 id="vgvolume-group">VG(Volume Group)</h3>
<ul>
<li>여러 PV를 묶어 만든 디스크 그룹<h3 id="lvlogical-volume">LV(Logical Volume)</h3>
</li>
<li>VG에서 논리적으로 나눈 공간 <ul>
<li>이걸 포맷하고 마운트해서 사용</li>
</ul>
</li>
</ul>
<h2 id="디스크그룹lvm-만드는-절차">디스크그룹(LVM) 만드는 절차</h2>
<ul>
<li>ex) /dev/sdb, /dev/sdc 디스크 2개를 묶어 디스크 그룹 만들기</li>
</ul>
<pre><code class="language-bash"># 1. LVM용 PV 생성
sudo pvcreate /dev/sdb /dev/sdc

# 2. VG (Volume Group) 생성
sudo vgcreate my_vg /dev/sdb /dev/sdc

# 3. LV (Logical Volume) 생성 (예: 10GB)
sudo lvcreate -L 10G -n my_lv my_vg

# 4. 파일시스템 생성 (ext4 등)
sudo mkfs.ext4 /dev/my_vg/my_lv

# 5. 마운트 디렉토리 생성 후 마운트
sudo mkdir /mnt/mydata
sudo mount /dev/my_vg/my_lv /mnt/mydata

# 6. 영구 마운트를 위해 /etc/fstab에 등록
</code></pre>
<h3 id="마운트">마운트</h3>
<ul>
<li>리눅스에서 디스크(LV)를 생성한 후 실제로 마운트해서 사용하려면 아래 절차가 필요</li>
<li><code>/etc/fstab</code> 파일을 사용하면 재부팅 후에도 자동 마운트 되도록 설정할 수 있다.</li>
</ul>
<blockquote>
<p>디스크를 특정 폴더(디렉토리)에 연결해서 사용할 수 있게 만드는 작업</p>
</blockquote>
<ul>
<li>예를 들어, /dev/my_vg/my_lv라는 논리 볼륨을 /mnt/mydata라는 디렉토리에 연결하면,
이제부터 /mnt/mydata 폴더에 저장하는 모든 파일은 실제로 my_lv 디스크에 저장돼요.</li>
</ul>
<h2 id="마운트-절차-예시">마운트 절차 예시</h2>
<ul>
<li>디스크: /dev/my_vg/my_lv</li>
<li>마운트할 위치: /mnt/mydata</li>
</ul>
<pre><code class="language-bash"># 1. 마운트할 디렉토리 생성
sudo mkdir -p /mnt/mydata

# 2. 마운트 명령어 실행
sudo mount /dev/my_vg/my_lv /mnt/mydata

# 3. 정상 마운트 확인
df -h | grep mydata</code></pre>
<h3 id="마운트-확인-명령어">마운트 확인 명령어</h3>
<pre><code class="language-bash"># 현재 마운트 상태 보기
df -h

# fstab 내용 보기
cat /etc/fstab

# 현재 마운트된 LV만 보기
lsblk

# 특정 LV의 상세 정보 보기
lvdisplay /dev/my_vg/my_lv

# VG 정보 보기
vgdisplay

# PV 정보 보기
pvdisplay</code></pre>
<h4 id="etcfstab">/etc/fstab</h4>
<ul>
<li>시스템이 부팅할 때, 어떤 디스크를 어디에 자동으로 마운트할지 정의하는 파일이다.</li>
</ul>
<h2 id="파티션">파티션</h2>
<ul>
<li>하나의 물리 디스크를 논리적으로 나누는 것</li>
<li>/dev/sdb1, /dev/sdb2, /dev/sdb3 이렇게 디스크 /dev/sdb를 3개로 나눔<ul>
<li>각각의 파티션에 다른 파일 시스템(ext4, swap 등)을 넣을 수 있음</li>
</ul>
</li>
<li>하드디스크(책장)를 여러 칸(서랍)으로 나눈 것
→ 각 칸마다 다른 책을 보관하거나, 목적에 따라 사용</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/d5278846-d6c2-492d-b7d1-2917396834f6/image.png" /></p>
<h3 id="디스크-사용-전체-흐름">디스크 사용 전체 흐름</h3>
<pre><code class="language-scss">디스크 ➜ 파티션 ➜ (디스크 그룹) ➜ 파일시스템 ➜ 마운트 ➜ 사용자 접근</code></pre>
<ul>
<li>디스크: /dev/sdb, /dev/sdc (물리적인 장치)</li>
<li>파티션: /dev/sdb1, /dev/sdc1 (논리적으로 나눈 단위)</li>
<li>디스크 그룹: VG, PV, LV (LVM 또는 Oracle ASM에서)</li>
<li>파일시스템: ext4, xfs 등 (포맷)</li>
<li>마운트: /mnt/data, /home (디렉토리에 연결해서 사용)</li>
<li>/etc/fstab: 부팅 시 자동 마운트 설정</li>
</ul>
<h3 id="lsblk-디스크-구조-보기">lsblk: 디스크 구조 보기</h3>
<ul>
<li>디스크 -&gt; 파티션 -&gt; 마운트 포인트까지 시각적으로 보여줌<pre><code>lsblk
</code></pre></li>
</ul>
<p>NAME           MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb              8:16   0   50G  0 disk 
└─sdb1           8:17   0   50G  0 part /mnt/data</p>
<pre><code>
### blkid: UUID 및 파일 시스템 타입 확인
- sudo blkid
- 파티션의 UUID, 타입(ex: ext4, xfs, swap)확인
- fstab 설정할 때 UUID 기반으로 쓰는 경우 유용!

### mount -a: fstab 테스트
- /etc/fstab 에 설정된 마운트를 즉시 적용함
- 오타나 경로 오류 확인할 때 유용하다.

### /etc/fstab 필요한 이유
- 매번 수동 마운트 하지 않고, 부팅할 때 자동으로 마운트되게 하기 위해 필요하다. 


## NFS가 필요한 이유
&gt; 네트워크에 있는 디스크(폴더)를 마치 내 디스크처럼 마운트해서 사용하는 기술

- 서버가 디렉토리를 export하면, 
- 클라이언트는 그걸 `/mnt/nfs`처럼 마운트해서 사용이 가능
- NFS 어떻게 쓰는지 보지를 못해서 ...(물론 MIG 넣어둔건 알겠으나..)  이건 시간 되면  여쭤보고 싶다.. </code></pre>