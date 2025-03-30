<blockquote>
<p>백지로 rac 설치에 필요한 요건들 전부 적어보라 했을 때 제대로 못적어서.. 하지만 pdf에 오답노트에 필요한 내용이 있어 정리해본다!🤩</p>
</blockquote>
<h1 id="카테고리">카테고리</h1>
<ul>
<li>HW 요건 확인</li>
<li>Network 요건 식별 확인</li>
<li>Install 된 OS System과 SW 요건 검증</li>
</ul>
<h1 id="hw-요건">HW 요건</h1>
<ul>
<li>물리 메모리 (1gb RAM)</li>
<li>swap 영역 (2gb이상의 사용가능한 스왑 영역)</li>
<li>TEMP 영역(400mb 이상)</li>
<li>Install 하는 Oracle SW 버전에서 동작이 보증된 프로세서 타입(CPU)</li>
<li>ORACLE_HOME 디렉토리에 3.5GB이상의 사용 가능한 Disk 영역<ul>
<li>혹은 ASM HOME디렉토리에 3.3gb이상의 사용 가능한 Disk 공간이 필요</li>
</ul>
</li>
<li>OCW(Oracle Clusterware) 설치에는 600mb 사용가능한 영역이 필요하다.</li>
<li>여러 개의 디스크가 필요하며, 각 디스크가 다른 disk controller를 사용할 필요가 있다.</li>
<li>Shared Everything 형태의 데이터베이스이다. <ul>
<li>Oracle RAC에서 사용되는 모든 Datafile, Control file, REDO Log file 및 Server parameter file(spfile)은 모든 RAC 데이터베이스 인스턴스가 access 가능한 shared disk 영역에 할당할 필요가 있다.</li>
</ul>
</li>
</ul>
<h3 id="voting-disk">Voting Disk</h3>
<ul>
<li>클러스터 멤버십을 관리하고, 네트워크 장애 경우에 노드간 클러스터 소유권을 조정한다.</li>
<li>voting disk는 shared disk에 존재하는 파일이다. 가용성을 높이기 위해, 여러 개 voting disk를 갖는 것 및 홀수 개의 voting disk를 갖는 것을 권장한다. </li>
<li>1개의 voting disk를 정의하는 경우에는 redundancy 때문에 File System Level에서 mirror화를 사용한다.</li>
</ul>
<h3 id="ocroracle-cluster-registry">OCR(Oracle Cluster Registry)</h3>
<ul>
<li>Cluster 구성 정보 및 클러스터 내 임의의 클러스터 데이터베이스에 관한 구성정보를 갖는다.</li>
<li>OCR에는 어느 데이터베이스 인스턴스를 어느 노드 위에서 실행할지, 어느 서비스를 어느 데이터베이스 위에서 실행하는지 등의 정보가 포함되어 있다.</li>
<li>오라클 클러스터웨어가 제어하는 프로세스에 관한 정보도 저장되어 있다.</li>
<li>OCR은 클러스터 내 모든 노드가 access 가능한 shared disk 에 존재한다.</li>
<li>OCR를 다중화(copy)할 수 있기 때문에 이 기능을 사용하여 고가용성을 확보하는 것을 권장한다.</li>
<li><code>주의</code>: Oracle Clusterware 및 Oracle RAC를 Install하기 전에, voting disk와 ocr 둘다, 구성하는 shared device에 존재할 필요가 있다. </li>
</ul>
<h1 id="네트워크-요건">네트워크 요건</h1>
<ul>
<li>Oracle RAC Cluster는 private interconnect로 연결되어 있는 2개 이상의 Node로 구성된다.</li>
<li>Interconnect는 Cluster에 있는 노드간 통신 path로서 기능한다.</li>
<li>각 인스턴스에서는 각 인스턴스의 공유 리소스의 사용을 동기화 하기 위해 메시지 기능에서 Interconnect를 사용한다.</li>
<li>여러 인스턴스에서 공유되는 Data Block 전송에도 inter connect를 사용한다.</li>
<li>Oracle Clusterware에서는 Cluster내 보드가 private interconnect를 사용해서 private network에 접속되어 있을 필요가 있다. </li>
<li>private inter connect는 cluster node에서 구성하는 개별 네트워크이다(priv?)</li>
<li>Oracle RAC에서 사용하는 인터커넥트는 Oracle Clusterware에서 사용하는 인터커넥트와 동일하다. </li>
<li>이 인터커넥트는 클러스터 멤버 이외 노드로부터 access 불가능해야한다.<h3 id="cluster-내-각-노드-조건을-충족해야함">cluster 내 각 노드 조건을 충족해야함</h3>
</li>
<li>각 노드에 2개 이상의 네트워크 인터페이스 카드(NIC)가 있고 한쪽 adapter에는 public network용, 다른 한 쪽은 interconnect로 사용되는 private network용이다. </li>
<li>노드가 각 조건에 해당되는 경우, 추가로 네트워크 어댑터를 추가로 설치한다.<ul>
<li>2개 이상의 네트워크 adapter가 준비되어있지 않은 경우</li>
<li>2개 네트워크 인터페이스가 갖춰졌지만 NAS가 사용되는 경우, NAS용으로 네트워크 adapter 장비를 준비해야 한다.<h3 id="3개-이상의-ip가-사용가능">3개 이상의 IP가 사용가능</h3>
</li>
</ul>
</li>
<li>Public Interface에 대응하는 host명(혹은 네트워크명)을 갖는 IP address</li>
<li>각 Private Interface에 대응하는 호스트명을 갖는 Private IP address<ul>
<li>주의: Private interface- priavte network ip address (10.<em>.</em>.<em>, 192.168.</em>.* 등) 사용을 권장한다.</li>
</ul>
</li>
<li>1개의 VIP 가상 ip address(아래 조건 충족)<ul>
<li>VIP Address 및 대응하는 네트워크명이 현재 사용되지 않음</li>
<li>VIP가 pulbic interface와 같은 subnet 상에 있다</li>
</ul>
</li>
<li>모든 노드의 public interface명이 동일해야 한다.<ul>
<li>node의 public interface가 network adapter eth0을 사용하고 있는 경우에는, eth0을 모든 노드에서 public interface로서 구성할 필요가 있다.</li>
<li>eth1가 1번째 노드의 priavte inteface명인 경우, 2번째 노드의 private interface도 eh1여야 한다.</li>
<li>모든 노드에 같은 private inteface명을 구성해야한다.<h3 id="sbinifconfig">/sbin/ifconfig</h3>
</li>
</ul>
</li>
<li>ifconfig</li>
</ul>
<pre><code>[root@cowjin1 sbin]# file ifconfig
ifconfig: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=5342baeaf80b35252d03e461af33849bf991bea1, stripped
[root@cowjin1 sbin]# cd ~
[root@cowjin1 ~]# file .bash_profile
.bash_profile: ASCII text
</code></pre><h2 id="install된-os와-sw-요건-검증">Install된 OS와 S/W 요건 검증</h2>
<ul>
<li>OS Version</li>
<li>OS Kernel Version</li>
<li>Install된 Package, Patch, Patch Set</li>
<li>Install된 Compiler 및 Driver</li>
<li>Web browser type 및 version</li>
<li>그 외 Application S/W 요건</li>
</ul>
<h2 id="red-hat-linux-os요건이-충족되었는지-절차">Red Hat Linux OS요건이 충족되었는지 절차</h2>
<ol>
<li>install된 Linux 배포판 및 버전 확인
<code># cat /etc/issue</code><pre><code>[root@cowjin1 ~]# cat /etc/issue
\S
Kernel \r on an \m
</code></pre></li>
</ol>
<pre><code>
2. 필요한 error level이 install 되어 있는지 판단하기 위해서는 root에서 
`# uname -r`</code></pre><p>[root@cowjin1 ~]# uname -r
5.15.0-304.171.4.3.el8uek.x86_64</p>
<pre><code>&gt;- 5.15.0: 커널 버전(메이저5, 마이너 15, 패치0)
- -304.171.4.3: 패치 및 빌드 정보
- el8uek: Oracle Linux의 Unbreakable Enterprise Kernel(UEK) 8버전
- x86_64: CPU 아키텍처

- 일반적인 Software처럼, Linux kernel 역시 OS System의 부정합을 수정하기 위해 갱신된다.
- 이러한 커널값의 변경을 alert kernel 혹은 alert level이라고 한다. 
- 이 Alert Level이 최소한으로 필요한 alert level보다도 낮은 경우 OS에 최신 커널 갱신을 install해야 한다.

3. Oracle Clusterware 및 RAC install guide에 기재된 OS Patch 변경 및 Package가 모두 install되어 있는지 확인해야 한다.
- root 유저로 아래 명령어를 실행하면, 필요한 package의 설치 여부를 판별할 수 있다.
`# rpm -q package_name`

## Server 준비
### OS User 및 Group
- dba 그룹 설정 (groupadd dba)
- oracle user
- (ASM 경우 - group dba)
### Secure Shell 구성
- UNIX 및 Linux Platform에 RAC 설치할 때 Software는 하나의 노드에 install된다. Oracle은 보안적인 통신을 사용해서 **software binary file을 다른 클러스터 노드에 복사**한다.
- ssh를 사용한다. ssh를 구성하는 데 처음으로 RSA(Rivest Shamir Adleman) KEY와 DSA KEY를 각 클러스터 노드에 생성해야한다.
  - 비밀키와 공개키를 생성한 후, 모든 cluster node member key를 , 각 노드에 동일한 인증키 파일에 복사한다. 완료되면, ssh agent를 기동해서 key를 memory에 로드한다.

**Red Hat Linux 상에서 RSA키 및 DSA 키를 구성하는 절차**
1. 한번 logout한 후, oracle 유저(rac node1계정)로 다시 로그인한다. 
- 여기서 root 유저로부터 oracle 유저로 변경하는 데 su 명령어를 사용하면 안된다. 정상적으로 수행하기 위해서는 root유저에서 os session을 완전히 종료 후, oracle user로 새로운 세션을 시작해야한다.

2. oracle user 홈디렉토리에서 .ssh 디렉토리가 존재하는지 확인해야한다.</code></pre><p>$ ls -a $HOME
$ mkdir ~/.ssh
$ chmod 700 ~/.ssh</p>
<pre><code>
3. RSA 타입의 공개 암호화 키와 비밀암호화키를 생성한다. 
`/usr/bin/ssh-keygen -t rsa`
- Enter Key를 눌러, Key File의 Default 디렉토리를 넣는다.
- passphrase를 입력할 때는 oracle 유저 패스워드와 다른 passphrase를 입력해서 확인한다.
- 이 명령어에 의해서, `/home/oracle/.ssh/id_rsa.pub` 파일에 공개키가 생성되고, /home/oracle/.ssh/id_rsa 파일에 비밀키가 생성된다.
- 주의: System Security를 보호하기 위해, 다른 유저에게 비밀키를 배포하지 말 것

4. oracle 각 노드 계정에 DSA 타입의 공개키 및 비밀키를 생성한다. 
- /usr/bin/ssh-keygen -t dsa
- Enter, key file default 디렉토리를 넣는다.
- passphrase를 입력할 때는 oracle 유저 패스워드와 다른 passphrase를 입력해서 확인한다.
- /home/oracle/.ssh/id_dsa.pub 파일에 공개키가 생성되고, /home/oracle/.ssh/id_dsa 파일에 비밀키가 생성된다.

5. 클러스터에 추가할 각 노드에서 순서 1부터 순서 4까지 반복한다.

### authorized_keys 추가
- SSH 에서 authorized_keys에 공개키(id_rsa.pub)를 추가하면 비밀번호 없이 SSH 접속이 가능하다.
- SSH 키 기반 인증을 설정하기 위한 과정

1. oracle user에서 디렉토리에 이동한다.
- cd ~/.ssh
2. RSA키 및 DSA키를 authorized_keys 파일에 추가한 후, .ssh 디렉토리에 내용을 조회한다.</code></pre><p>$ cat id_rsa.pub &gt;&gt;authorized_keys
$ cat id_dsa.pub &gt;&gt;authorized_kyes
$ ls</p>
<pre><code>- authorized_keys 파일에 추가해서 생성한 키인 id_dsa.pub 및 id_rsa.pub과 공개키인 id_dsa 및 id_rsa가 표시된다.
3. scp 혹은 sftp를 통해 authorized_keys 파일을 remote node 상의 oracle user의 .ssh directory에 copy한다.
- scp 명령어를 통해 node1-&gt; node2에 복사한다. (이때  각 노드의 oracle user 패스워드가 동일해야한다)
4. ssh를 사용해서 생성한 passphrase 사용해서 authorized_keys 파일을 복사한 노드에 로그인한다.
5. 클러스터에 노드가 3개 이상 있는 경우, 3, 4번을 반복한다.
- 마지막으로 변경한 authorized_keys 파일을 다음 노드에 복사하여, 



### OS 환경 구성 개요
- linux umask를 022로 설정
- $ORACLE_BASE: oracle software install할 디렉토리로 지정
- /tmp 디렉토리에서 사용가능한 디스크 공간이 400mb 미만인 경우에서도 별도 파일 시스템에는 400mb이상 사용공간이 있는 경우, file system에 대체해서 일시적으로 디렉토리를 지정할 수 있도록 TEMP 및 TMPDIR 환경변수를 사용할 수 있다.
- Oracle Clusterware를 install하기 전에, Oracle Clusterware 홈(CRS HOME)디렉토리에 ORACLE_HOME이라는 변수를 설정가능하다. 
- Oracle Clusterware가 install된 후에, 환경변수 ORACLE_HOME은 Oracle Database 홈 디렉토리 값을 반영해서 변경된다.

## 네트워크 구성
- **네트워크를 구성하고, 클러스터 내 각 노드가 클러스터 내 다른 노드와 통신하기 위한 절차**
1. cluster명 결정. 
- host domain내에서 global하게 유일해야할 것
- 1글자 이상, 15글자 미만
- 3rd party 벤더 클러스터웨어를 사용하는 경우에는, 벤터 클러스터명을 사용하는 것을 권장한다
2. 클러스터 노드명에는 각 노드 primary host명을 사용한다. 즉, hostname 명령어에 의해 표시되는 이름을 사용한다. 
  - 숫자로 시작하면 안된다. 대문자/소문자로 시작한다. -(dash)가 유일
  - FQDN 혹은 short hostname 둘 중 하나로 구성
  - 각 노드 private node명 혹은 private ip address를 결정한다. priavte ip address는 이 클러스터 내 다른 노드만이 access가능한 address
    - 오라클 database에서는 node간 혹은 instance간 cache fusion 통신에 private ip address를 사용한다. 
    - public_hostname-priv 형식의 이름을 지정할 것을 권장한다.
  - Oracle Database는 client와 database간 접속에 VIP address를 사용하기 위해서, vip address는 public하게 access 가능해야 한다. (public_hostname-vip 형식으로 지정)
  - vip host명은 public node명에서 node가 정지되어 있을 때에 노드에 전송되는 client request를 재루팅하기 위해 사용된다.
4. 클러스터 각 노드에서, 대응하는 네트워크명을 갖는 public ip address를 1개의 network adapter에 할당하고, 대응하는 network명을 갖는 private ip address를 1개의 network adapter에 할당한다. (nmtui)
- 각 노드의 public명은, 사용하는 DNS에 등록되어 있어야 한다. 사용 가능한 DNS가 없는 경우, /etc/hosts 파일에 네트워크명과 ip address를 등록한다.
  - ping 명령어를 사용해 interconnect interface가 접속가능한지 테스트 가능하다.
5. Cluster내 각 노드에서 VIP address는 public ip address와 동일한 서브넷 상에 존재한다.
![](https://velog.velcdn.com/images/greendev/post/295b24ca-7dea-4c5e-8647-47eec033af55/image.png)
</code></pre><p>[root@cowjin1 ~]# cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.0.131 cowjin1
192.168.0.132 catjin2</p>
<p>192.168.0.133 cowjin1-vip
192.168.0.134 catjin2-vip</p>
<p>192.168.0.135 cowjin-cluster-scan</p>
<p>10.10.0.1   cowjin-priv1
10.10.0.2   catjin-priv1
20.20.0.1   cowjin-priv2
20.20.0.2   catjin-priv2
30.30.0.1   cowjin-priv3
30.30.0.2   catjin-priv3
40.40.40.1  cowjin-priv4
40.40.40.2  catjin-priv4</p>
<p>```</p>
<h3 id="fqdn-fully-qualified-domain-name-완전한-도메인-이름">FQDN (Fully QUalified Domain Name, 완전한 도메인 이름)</h3>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fully_qualified_domain_name">FQDN</a></li>
<li><a href="https://docs.redhat.com/ja/documentation/red_hat_enterprise_linux/7/html/installation_guide/sect-network-hostname-configuration-x86#sect-network-hostname-configuration-x86">네트워크와 호스트명</a></li>
<li>FQDN = hostname + domain name
<img alt="" src="https://velog.velcdn.com/images/greendev/post/81dca07d-6d8a-45a5-8263-698b45337000/image.png" /></li>
</ul>
<h3 id="short-hostname-단축-호스트명">Short Hostname (단축 호스트명)</h3>
<ul>
<li>도메인 정보를 포함하지 않는 짧은 호스트명</li>
<li>서버 내부에서 로컬 식별자로 사용</li>
<li>FQDN의 호스트명 부분만 포함하여, 도메인 없이 독립적으로 사용 가능 </li>
</ul>
<h2 id="os-시스템-및-software">OS 시스템 및 Software</h2>
<h3 id="시간-설정-ntp">시간 설정 (NTP)</h3>
<ul>
<li>양쪽 노드의 시간을 동일하게 설정하기 위해서 Network Time Protocol 기능을 사용</li>
<li>NTP: Network에서 접속된 서버 시간을 동기화하도록 설계된 protocol<ul>
<li>NTP 서버로 불리는 1개 이상의 서버에 대응해서 정기적으로 timing request를 수행한다.</li>
</ul>
</li>
</ul>
<h2 id="install-directory-및-shared-disk-구성">Install Directory 및 Shared Disk 구성</h2>
<ul>
<li>클러스터 내 각 노드에는 OCR 파일 및 database file을 저장하는 외부 공유 디스크가 필요하다. </li>
<li>지원되는 Cluster File System. OCFS, IBM platform의 GPFS(AIX서버) 등 </li>
<li>Block Device에서 구성되는 Shared Disk partition. Block Device는 Linux File System을 사용해서 mount되는 Disk Partition이다. <ul>
<li>Oracle Clusterware 및 Oracle RAC에 의해 직접 쓰여진다.</li>
<li>권장: Oracle Database 파일용의 ASM관리 (Oracle Clusterware File은 ASM에 저장할 수 없다.)</li>
</ul>
</li>
</ul>
<h3 id="block-device-구성">Block Device 구성</h3>
<ul>
<li>Oracle Clusterware release 10.2 이상에서는 RHEL 4.0을 사용할 경우에 RAW 디바이스가 아닌 Block Device가 사용가능하다.<ul>
<li>Oracle Clusterware 파일은 Default로 direct I/O를 사용하도록 구성되어 있기 때문에, Block Device에 직접 쓸 수 있다.<h3 id="oracle-clusterware-install하기-전-shared-disk-partition">Oracle Clusterware Install하기 전, shared disk partition</h3>
</li>
</ul>
</li>
<li>OCR 영역에 280MB 파티션 1</li>
<li>OCR Mirror: 280mb 파티션1</li>
<li>Voting Disk마다 하나씩 사용할 280MB 파티션 3개</li>
<li>normal 구성인 경우.. </li>
</ul>
<blockquote>
<p>주의: fdisk 를 사용해서 device size(256mb 등) 지정해서 partition을 생성하면 실제로 생성되는 device가 disk의 필요한 사이즈보다 작게 될 경우가 있다.
이는 현행의 fdisk 제한이 원인으로 발생한다.</p>
</blockquote>
<ul>
<li>Oracle 구성 software는 device에 256mb 이상의 사용가능한 disk 영역이 포함되는 것을 확인한다. (280mb 이상으로 설정 권장)</li>
<li>파티션 사이즈는 fdisk -s partition으로 확인이 가능하다.</li>
</ul>
<h3 id="block-device">Block Device</h3>
<ol>
<li>root 유저로 로그인</li>
<li>/sbin/fdisk -l : 사용할 디스크 디바이스명을 식별하기 위해서는 cluster 최초 노드(node1)에서 명령어를 수행한다.</li>
</ol>
<ul>
<li>추가된 신규 block device 혹은 partition되어 있지 않은 사용 가능영역이 있는 partition되어있는 device에 필요한 disk partition을 작성할 수 있다.<h2 id="oracle_base">ORACLE_BASE</h2>
</li>
<li>Oracle Software Install 최상위 디렉토리로서 동작한다. OFA(Optimal Flexible Architecture) 가이드라인에 따르면,  /mount_point/app/oracle 의 path를 사용하는 것을 권장한다.</li>
<li>ORACLE_BASE 디렉토리에 사용하는 파일 시스템에는 Oracle Database Software Install 때문에 7GB 이상의 사용 가능한 디스크 영역이 필요하다. <ul>
<li>ORACLE_BASE 디렉토리 PATH는 모든 노드상에서 동일해야 한다.</li>
</ul>
</li>
<li>df -h 명령어를 사용해서 마운트된 각 파일 시스템의 사용 가능한 디스크 영역을 조회할 수 있다.</li>
</ul>