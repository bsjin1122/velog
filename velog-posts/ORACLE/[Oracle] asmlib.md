<blockquote>
<p>참고: </p>
</blockquote>
<ul>
<li><a href="https://docs.oracle.com/en/database/oracle/oracle-database/23/ladbi/installing-and-configuring-oracle-asmlib-software.html">Installing and Configuring Oracle ASMLIB Software</a></li>
<li><a href="https://silight.tistory.com/9">oracle RAC ASMLib 설정(12cR2)</a></li>
</ul>
<h2 id="구성-요소-패키지">구성 요소 (패키지)</h2>
<ul>
<li>oracleasmlib    <ul>
<li>(Closed Source) Oracle이 제공하는 프로프라이어터리 라이브러리 패키지</li>
<li><code>wget https://public-yum.oracle.com/repo/OracleLinux/OL8/addons/x86_64/getPackage/oracleasm-support-2.1.12-1.el8.x86_64.rpm</code></li>
</ul>
</li>
<li>oracleasm-support    <ul>
<li>(Open Source, GPL) ASMLib을 관리하는 유틸리티 패키지</li>
<li><code>wget https://public-yum.oracle.com/repo/OracleLinux/OL8/addons/x86_64/getPackage/oracleasm-support-2.1.12-1.el8.x86_64.rpm</code></li>
</ul>
</li>
<li>kmod-oracleasm 또는 kmod-redhat-oracleasm    <ul>
<li>(Open Source, GPL) ASMLib의 커널 모듈 패키지</li>
<li>kmod-oracleasm은 Oracle Linux의 UEK(Unbreakable Enterprise Kernel)에는 기본 포함됨.</li>
</ul>
</li>
</ul>
<h3 id="oracle-asmlib를-사용하도록-디스크-장치-구성">Oracle ASMLIB를 사용하도록 디스크 장치 구성</h3>
<pre><code class="language-shell">[root@cowjin1 ~]# lsblk
NAME         MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda            8:0    0  320G  0 disk
├─sda1         8:1    0   16G  0 part  [SWAP]
└─sda2         8:2    0  304G  0 part  /
sdb            8:16   0   10G  0 disk
└─mpath1     252:0    0   10G  0 mpath
sdc            8:32   0   10G  0 disk
├─sdc1         8:33   0   10G  0 part
└─mpath3     252:2    0   10G  0 mpath
  └─mpath3p1 252:5    0   10G  0 part
sdd            8:48   0   32G  0 disk
└─mpath4     252:3    0   32G  0 mpath
sde            8:64   0   32G  0 disk
└─mpath5     252:4    0   32G  0 mpath
sdf            8:80   0   10G  0 disk
└─mpath2     252:1    0   10G  0 mpath
sdg            8:96   0   32G  0 disk
└─mpath8     252:8    0   32G  0 mpath
sdh            8:112  0   32G  0 disk
├─sdh1         8:113  0   32G  0 part
└─mpath6     252:6    0   32G  0 mpath
  └─mpath6p1 252:9    0   32G  0 part
sdi            8:128  0   32G  0 disk
└─mpath9     252:10   0   32G  0 mpath
sdj            8:144  0   32G  0 disk
└─mpath7     252:7    0   32G  0 mpath
sdk            8:160  0   32G  0 disk
└─mpath12    252:13   0   32G  0 mpath
sdl            8:176  0   32G  0 disk
└─mpath10    252:11   0   32G  0 mpath
sdm            8:192  0   32G  0 disk
└─mpath11    252:12   0   32G  0 mpath
sdn            8:208  0   32G  0 disk
└─mpath13    252:14   0   32G  0 mpath
sr0           11:0    1 13.2G  0 rom


sdd, sde, sdf --&gt; ocr votingdisk용
sdg, sdi, sdj, sdk, sdl, sdm, sdn --&gt; datafile용</code></pre>
<ul>
<li>시스템에 연결된 블록 디바이스(디스크, 파티션, 논리 볼륨 등) 정보를 출력하는 명령어</li>
<li>물리 디스크, 파티션, 멀티 패스 장치 등이 어떻게 구성되어 있는지 확인할 수 있다.</li>
</ul>
<h3 id="멀티-패스multipath">멀티 패스(multipath)</h3>
<ul>
<li>스토리지가 여러 경로(Path)로 연결될 때, 하나의 논리 디스크(mpath)로 묶어 관리하는 기술</li>
<li>즉, sdb 디스크는 mpath1이라는 멀티패스 장치로 관리되고 있다.</li>
</ul>
<hr />
<p><img src="https://velog.velcdn.com/images/greendev/post/07b9b670-a7d0-4fb8-a656-3569230dd0ed/image.png" style="width: 40%;" /></p>
<h2 id="안됐던-이유"><a href="https://docs.oracle.com/en/database/oracle/oracle-database/23/ladbi/installing-and-configuring-oracle-asmlib-software.html#GUID-6C3F9E52-4E28-4912-B3A0-4E52570778C7">안됐던 이유</a></h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/20e03296-a576-45f8-bea9-874aceabc669/image.png" /></p>
<pre><code class="language-shell">[root@cowjin1 ~]# rpm -qa | grep oracleasm
oracleasm-support-2.1.12-1.el8.x86_64
oracleasmlib-2.0.17-1.el8.x86_64
kmod-redhat-oracleasm-2.0.8-18.1.0.1.el8_10.x86_64
-- OEL8버전 이상을 사용할 때는 관련 패키지를 Oracle ASMLib v3 혹은 그 이상을 설치해야 한다.

oracleasmlib는 filezilla 통해서 받았고, 
oracleasm-support는 버전 3.0 이상으로 rpm -ivh로 직접 받았다.

[root@cowjin1 oramedia]# rpm -qa | grep oracleasm
oracleasm-support-3.0.0-6.el8.x86_64
oracleasmlib-3.0.0-13.el8.x86_64
kmod-redhat-oracleasm-2.0.8-18.1.0.1.el8_10.x86_64
</code></pre>
<p>다시 하기..!</p>
<h2 id="asmlib-구성-초기화">ASMLIB 구성 초기화</h2>
<ul>
<li><a href="https://docs.oracle.com/en/operating-systems/oracle-linux/asmlib/asmlib-ConfiguringASMLib.html">https://docs.oracle.com/en/operating-systems/oracle-linux/asmlib/asmlib-ConfiguringASMLib.html</a></li>
</ul>
<pre><code class="language-shell">[root@cowjin1 ~]# /usr/sbin/oracleasm configure -i
Configuring the Oracle ASM library driver.

This will configure the on-boot properties of the Oracle ASM library
driver.  The following questions will determine whether the driver is
loaded on boot and what permissions it will have.  The current values
will be shown in brackets ('[]').  Hitting &lt;ENTER&gt; without typing an
answer will keep that current value.  Ctrl-C will abort.

Default user to own the driver interface []: grid
Default group to own the driver interface []: dba
Start Oracle ASM library driver on boot (y/n) [n]: y
Scan for Oracle ASM disks on boot (y/n) [y]: y
Maximum number of disks that may be used in ASM system [2048]:
Enable iofilter if kernel supports it (y/n) [y]: y
Writing Oracle ASM library driver configuration: done

## ASMLIB 구성을 마친 후 oracleasm 서비스를 활성화하고 시작
[root@cowjin1 ~]# systemctl enable --now oracleasm
Synchronizing state of oracleasm.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
Executing: /usr/lib/systemd/systemd-sysv-install enable oracleasm
</code></pre>
<h3 id="등록된-asm-디스크-확인">등록된 ASM 디스크 확인</h3>
<p><code>/usr/sbin/oracleasm listdisks</code></p>
<pre><code class="language-shell">[root@cowjin1 ~]# ls -al /dev/mapper
total 0
drwxr-xr-x  2 root root     360 Feb  6 20:30 .
drwxr-xr-x 20 root root    4120 Feb  9 18:07 ..
crw-------  1 root root 10, 236 Feb  6 20:30 control
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath1 -&gt; ../dm-0
lrwxrwxrwx  1 root root       8 Feb  6 20:30 mpath10 -&gt; ../dm-11
lrwxrwxrwx  1 root root       8 Feb  6 20:30 mpath11 -&gt; ../dm-12
lrwxrwxrwx  1 root root       8 Feb  6 20:30 mpath12 -&gt; ../dm-13
lrwxrwxrwx  1 root root       8 Feb  6 20:30 mpath13 -&gt; ../dm-14
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath2 -&gt; ../dm-1
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath3 -&gt; ../dm-2
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath3p1 -&gt; ../dm-5
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath4 -&gt; ../dm-3
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath5 -&gt; ../dm-4
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath6 -&gt; ../dm-6
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath6p1 -&gt; ../dm-9
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath7 -&gt; ../dm-7
lrwxrwxrwx  1 root root       7 Feb  6 20:30 mpath8 -&gt; ../dm-8
lrwxrwxrwx  1 root root       8 Feb  6 20:30 mpath9 -&gt; ../dm-10
[root@cowjin1 ~]#
[root@cowjin1 ~]#
[root@cowjin1 ~]# multipath -ll
mpath1 (0QEMU_QEMU_HARDDISK_drive-scsi1) dm-0 QEMU,QEMU HARDDISK
size=10G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 3:0:0:1   sdb 8:16  active ready running
mpath10 (0QEMU_QEMU_HARDDISK_drive-scsi10) dm-11 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 12:0:0:10 sdl 8:176 active ready running
mpath11 (0QEMU_QEMU_HARDDISK_drive-scsi11) dm-12 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 13:0:0:11 sdm 8:192 active ready running
mpath12 (0QEMU_QEMU_HARDDISK_drive-scsi12) dm-13 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 14:0:0:12 sdk 8:160 active ready running
mpath13 (0QEMU_QEMU_HARDDISK_drive-scsi13) dm-14 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 15:0:0:13 sdn 8:208 active ready running
mpath2 (0QEMU_QEMU_HARDDISK_drive-scsi2) dm-1 QEMU,QEMU HARDDISK
size=10G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 4:0:0:2   sdf 8:80  active ready running
mpath3 (0QEMU_QEMU_HARDDISK_drive-scsi3) dm-2 QEMU,QEMU HARDDISK
size=10G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 5:0:0:3   sdc 8:32  active ready running
mpath4 (0QEMU_QEMU_HARDDISK_drive-scsi4) dm-3 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 6:0:0:4   sdd 8:48  active ready running
mpath5 (0QEMU_QEMU_HARDDISK_drive-scsi5) dm-4 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 7:0:0:5   sde 8:64  active ready running
mpath6 (0QEMU_QEMU_HARDDISK_drive-scsi6) dm-6 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 8:0:0:6   sdh 8:112 active ready running
mpath7 (0QEMU_QEMU_HARDDISK_drive-scsi7) dm-7 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 9:0:0:7   sdj 8:144 active ready running
mpath8 (0QEMU_QEMU_HARDDISK_drive-scsi8) dm-8 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 10:0:0:8  sdg 8:96  active ready running
mpath9 (0QEMU_QEMU_HARDDISK_drive-scsi9) dm-10 QEMU,QEMU HARDDISK
size=32G features='0' hwhandler='0' wp=rw
`-+- policy='service-time 0' prio=1 status=active
  `- 11:0:0:9  sdi 8:128 active ready running


/usr/sbin/oracleasm createdisk OCRVOTING01 /dev/dm-0
/usr/sbin/oracleasm createdisk OCRVOTING02 /dev/dm-1
/usr/sbin/oracleasm createdisk OCRVOTING03 /dev/dm-2

=========================================================</code></pre>
<pre><code class="language-shell">


[root@cowjin1 ~]# /usr/sbin/oracleasm createdisk OCRVOTING01 /dev/mapper/mpath1
Device &quot;/dev/mapper/mpath1&quot; is already labeled for ASM disk &quot;&quot;
[root@cowjin1 ~]# /usr/sbin/oracleasm createdisk OCRVOTING02 /dev/mapper/mpath2
Device &quot;/dev/mapper/mpath2&quot; is already labeled for ASM disk &quot;&quot;
[root@cowjin1 ~]# /usr/sbin/oracleasm createdisk OCRVOTING03 /dev/mapper/mpath3
Unable to open device &quot;/dev/mapper/mpath3&quot;: Device or resource busy


dd if=/dev/zero of=/dev/dm-0 bs=1M count=1
dd if=/dev/zero of=/dev/dm-1 bs=1M count=1
dd if=/dev/zero of=/dev/dm-2 bs=1M count=1


[root@cowjin1 mapper]# dd if=/dev/zero of=/dev/dm-0 bs=1M count=1
1+0 records in
1+0 records out
1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.00216171 s, 485 MB/s
[root@cowjin1 mapper]# dd if=/dev/zero of=/dev/dm-1 bs=1M count=1
1+0 records in
1+0 records out
1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.00225873 s, 464 MB/s
[root@cowjin1 mapper]# dd if=/dev/zero of=/dev/dm-2 bs=1M count=1
1+0 records in
1+0 records out
1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.000659109 s, 1.6 GB/s




[root@cowjin1 ~]# /usr/sbin/oracleasm listdisks
OCRVOTING01
OCRVOTING02
[root@cowjin1 ~]#
[root@cowjin1 ~]#
[root@cowjin1 ~]# /usr/sbin/oracleasm createdisk OCRVOTING03 /dev/mapper/mpath3 -- dm-2fh 했어야..
Writing disk header: done
Instantiating disk: done
[root@cowjin1 ~]#
[root@cowjin1 ~]# /usr/sbin/oracleasm listdisks
OCRVOTING01
OCRVOTING02
OCRVOTING03





[root@cowjin1 ~]# dd if=/dev/zero of=/dev/dm-5 bs=1M count=1
1+0 records in
1+0 records out
1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.000753951 s, 1.4 GB/s
[root@cowjin1 ~]#
[root@cowjin1 ~]#
[root@cowjin1 ~]# /usr/sbin/oracleasm createdisk DATA02 /dev/dm-5
Unable to open device &quot;/dev/dm-5&quot;: Device or resource busy
[root@cowjin1 ~]#
[root@cowjin1 ~]#
[root@cowjin1 ~]#
[root@cowjin1 ~]#
[root@cowjin1 ~]# /usr/sbin/oracleasm createdisk DATA02 /dev/dm-11
Device &quot;/dev/dm-11&quot; is already labeled for ASM disk &quot;&quot;
[root@cowjin1 ~]#
[root@cowjin1 ~]# oracleasm listdisks
DATA01
DATA03
DATA04
DATA05
DATA06
DATA07
OCRVOTING01
OCRVOTING02
OCRVOTING03
[root@cowjin1 ~]#
[root@cowjin1 ~]#
[root@cowjin1 ~]# lsblk /dev/dm-5
NAME       MAJ:MIN RM SIZE RO TYPE  MOUNTPOINT
mpath6     252:5    0  32G  0 mpath
└─mpath6p1 252:6    0  32G  0 part
</code></pre>