<blockquote>
<p>오늘은 오라클 선생님이 거의 교수님 강의해주신 날...
DBA입장에서 단순히 오라클뿐만이 아니라, 아키텍처, 디스크, 네트워크, 스토리지 등등 전체를 다 고려할 수 있는 사람이 되어야 한다고 해주셨다.</p>
</blockquote>
<h1 id="lun-logical-unit-number">LUN (Logical Unit Number)</h1>
<ul>
<li><p><a href="https://jack-of-all-trades.tistory.com/367">참고한 사이트: ASM 구성 시 LUN 크기, 갯수가 성능에 미치는 영향</a></p>
</li>
<li><p>논리 단위 번호, 논리적인 디스크 단위를 말한다.</p>
</li>
<li><p>논리적인 단위이기 때문에, 물리적인 디스크 1개가 하나의 LUN이 될 수도 있고, 여러 개의 디스크가 하나의 LUN이 될 수도 있다.</p>
</li>
<li><p>구성하기 나름이다. </p>
</li>
<li><p>Oracle ASM에서 DG(Disk Group) 구성 시, 물리적인 디스크 파티션을 사용하는 경우, 별로 신경쓸 게 없지만 LUN을 사용하는 경우, ASM DG 구성을 위해 LUN 크기는 얼마로 잡아야 할지, LUN 개수는 얼마로 잡아야 할지 고민이 된다.</p>
</li>
<li><p>LUN 개수가 너무 많아지지 않도록 하라는 정도이다. </p>
</li>
<li><p>원래 ASM에서는 DG를 구성하는 모든 디스크 유닛에 대해 스트라이핑(Striping, I/O 분산)을 하기 때문에 디스크 개수가 많을 수록 Disk I/O 성능이 좋아지는 장점이 있다.</p>
</li>
<li><p>하지만, LUN을 사용하게 되면 LUN은 논리적인 단위이고, 물리적인 디스크와 1:1 매핑이 되지 않기 때문에 LUN 개수와 성능의 인과관계를 찾는게 어려워진다.</p>
</li>
<li><p>ASM이 데이터분산하는 기준은 디스크 용량을 기준으로 한다.</p>
<ul>
<li>DG를 구성하는 LUN들의 크기들은 모두 같은 용량으로 구성하도록 권고하고 있다.</li>
</ul>
<hr />
</li>
</ul>
<h1 id="코어core와-소켓socket의-차이">코어(Core)와 소켓(Socket)의 차이</h1>
<h2 id="코어core">코어(Core)</h2>
<ul>
<li>CPU 내부에 있는 작업 처리 단위이다. 코어가 많을수록 동시에 여러 작업(스레드)을 처리할 수 있는 능력이 커집니다.</li>
<li>코어 1개이면 싱글 코어, 2개이면 듀얼 코어, 4개이면 쿼드 코어, 6개이면 헥사코어, 8개이면 옥타코어 등으로 불린다.<h2 id="소켓socket-또는-슬롯cpu-slot">소켓(Socket) 또는 슬롯(CPU Slot)</h2>
<ul>
<li><a href="https://youtu.be/MObHfGvMLnI?si=mYREzUTGk_7lzB9d">Youtube - CPU 소켓의 종류</a>
<img alt="" src="https://velog.velcdn.com/images/greendev/post/499b2dcb-9a52-4fb0-b943-7495d36d94a7/image.png" /></li>
</ul>
</li>
</ul>
<ul>
<li><p>CPU를 장착하는 물리적인 슬롯을 말한다.</p>
</li>
<li><p>하나의 서버 메인보드에 여러 개의 소켓이 있을 수 있으며, 각각의 소켓에 하나의 CPU가 장착된다.</p>
</li>
<li><p>예를 들어, 2소켓 서버는 2개의 CPU를 장착할 수 있어 각 CPU가 8코어라면, 총 16코어의 성능을 발휘하게 된다.</p>
</li>
</ul>
<hr />
<h1 id="numanon-uniform-memory-access">NUMA(Non-Uniform Memory Access)</h1>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/1846eb59-ac96-4443-a773-ec5876291c90/image.png" /></p>
<ul>
<li><a href="https://bluemoon-1st.tistory.com/85">NUMA 메모리 관리 기법</a></li>
<li>CPU가 메모리를 사용하는 방식 중 하나. </li>
<li>메모리를 관리하는 방법 중 하나이다.<ul>
<li>CPU도 클러스터링으로 되어있을 것임</li>
<li>가장 기본적으로 메모리를 관리하는 방법은, 하나의 512GB 메모리에 대해 여러 CPU가 선점유 방식을 통해 접근하는 방법이 있다.</li>
<li>ex) 4개의 CPU core가 존재한다고 했을 때, 하나의 CPU가 메모리에 접근하여 사용 중에 있다면 남은 3개의 core는 메모리에 접근할 수 없고 대기해야 하는 병목현상이 발생한다.</li>
</ul>
</li>
<li>NUMA 노드의 경우, 메모리를 주소별 구간으로 나눈 뒤 각각의 CPU에 할당하는 방식이다. <ul>
<li>예를 들어, 512GB 메모리가 존재한다면, 0<del>128까지는 CPU1, 128</del>256은 CPU2, 256<del>384 -&gt; CPU3, 384</del>512-&gt; CPU4 로 CPU별로 접근하는 메모리를 나누어서 진행한다.</li>
<li>이 경우, 하나의 메모리라도 구간이 나누어져 있기에 (H/W, S/W적으로 나눌 수 있다) 각 메모리 구간에 대하여 동시에 접근이 가능하다. 즉, 병목현상 문제를 해결할 수 있다.</li>
</ul>
</li>
<li>다만 오라클에선 이걸 안좋아한다. 이렇게 했을 때 다른 그룹에 있는 것들은 그쪽에서 사용하게 된다면 정합성이 맞지 않게된다.. 뭐 이런 입장이라고 한다.</li>
</ul>
<hr />
<h1 id="l2-switch">L2 Switch</h1>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/346f0e84-88f1-44ef-90bf-e131d286ccdd/image.png" /></p>
<ul>
<li><p>L2 스위치는 데이터 링크 계층(Layer 2)에서 동작하는 장비로, MAC 주소를 기반으로 네트워크 트래픽을 전달한다.</p>
</li>
<li><p>주로 LAN(Local Area Network) 내에서 장비 간의 통신을 관리하며, VLAN(가상 LAN) 구성을 통해 트래픽을 분리하고 관리할 수 있다.</p>
</li>
<li><p>** 서버 간의 빠른 통신 보장**</p>
<ul>
<li>L2 스위치는 서버가 같은 네트워크 세그먼트에 있을 때, 빠른 데이터 전송을 보장한다.</li>
<li>이는 클러스터 노드 간의 데이터 동기화나 고가용성 구성에서 매우 중요</li>
</ul>
</li>
<li><p><strong>VLAN을 통한 네트워크 분리 및 보안 강화</strong></p>
<ul>
<li>데이터베이스 서버가 다른 애플리케이션이나 서버들과 같은 물리적 네트워크를 공유하더라도, L2 스위치를 통해 VLAN을 설정하여 논리적으로 네트워크를 분리할 수 있다.</li>
</ul>
</li>
<li><p><strong>데이터베이스 클러스터 구성 시의 중요성</strong></p>
<ul>
<li>Oracle RAC(Real Application Clusters)와 같은 클러스터 구성에서 각 노드 간의 통신은 매우 중요하다. L2 스위치를 통해, 각 노드가 같은 네트워크 내에서 빠르고 효율적으로 통신할 수 있게 한다.</li>
<li>스위치의 QoS(Quality of Service) 기능을 활용하여 클러스터 노드 간의 트래픽을 우선 처리할 수 있다.</li>
</ul>
</li>
</ul>
<hr />
<h1 id="pciperipheral-component-interconnect">PCI(Peripheral Component Interconnect)</h1>
<ul>
<li><p>컴퓨터의 <strong>확장 카드 슬롯</strong>에 장치를 연결할 수 있도록 설계된 하드웨어 인터페이스</p>
<ul>
<li><p>주변 장치 연결, 줄여서 PCI</p>
</li>
<li><p>HDML 같은 그래픽이나, USB 포트를 추가로 장착할 경우에, 메인보드에 기능 확장을 위한 장치들을 연결할 때 사용되는 데이터 전송 규격을 PCI라고 합니다.</p>
</li>
</ul>
</li>
</ul>
<blockquote>
<p>주로 네트워크 카드, 그래픽 카드, 사운드 카드, RAID 컨트롤러 등 다양한 장치를 메인보드에 연결하는 데 사용됩니다.</p>
</blockquote>
<hr />
<h1 id="gbicgigabit-interface-converter">GBIC(Gigabit Interface Converter)</h1>
<ul>
<li><p>네트워크 장비에 연결할 수 있는 광섬유 모듈이다.</p>
<ul>
<li>주로 스위치, 라우터와 같은 네트워크 장비에 설치하여 광섬유 케이블을 통해 기가비트 속도의 데이터 전송을 가능하게 한다.</li>
</ul>
</li>
<li><p>특히, 데이터센터나 대규모 서버 클러스터에서 서버 간의 고속 연결이 필수적일 때 유용하다.</p>
</li>
<li><p>GBIC 모듈을 활용해 데이터베이스 서버가 스위치와 안정적으로 연결되도록 구성하여 네트워크 병목현상을 줄이고, 성능을 높일 수 있다.</p>
</li>
</ul>
<hr />
<h1 id="nmonnigels-monitor">Nmon(Nigel's Monitor)</h1>
<ul>
<li><p>IBM에서 개발한 시스템 성능 모니터링 도구</p>
<ul>
<li><p>주로 AIX와 Linux 시스템에서 사용됩니다.</p>
</li>
<li><p>CPU, 메모리, 네트워크, 디스크 I/O, 프로세스 상태 등 다양한 성능 지표를 실시간으로 모니터링 할 수 있다.</p>
</li>
<li><p>Nmon은 간편한 인터페이스로 시스템 상태를 즉시 확인하거나, 데이터를 수집하여 분석하는 데 유용하다.</p>
</li>
</ul>
</li>
</ul>
<h2 id="개념-및-특징">개념 및 특징</h2>
<blockquote>
<ul>
<li>오픈소스</li>
</ul>
</blockquote>
<ul>
<li>실시간 모니터링</li>
<li>경량 도구</li>
<li>데이터 수집 및 로그 파일 생성</li>
</ul>
<h2 id="nmon의-주요-기능">Nmon의 주요 기능</h2>
<ul>
<li>CPU 모니터링<ul>
<li>CPU 사용률, 각 코어별 사용률, CPU 대기 시간 등을 실시간으로 확인합니다.</li>
</ul>
</li>
<li>메모리 모니터링<ul>
<li>메모리 사용량, 스왑 사용량, 캐시 상태 등을 확인할 수 있다.</li>
</ul>
</li>
<li>네트워크 트래픽 모니터링<ul>
<li>네트워크 인터페이스별 트래픽 정보를 보여준다.</li>
</ul>
</li>
<li>디스크 I/O 모니터링<ul>
<li>디스크 읽기/쓰기 속도와 I/O 대기 시간 등을 실시간으로 확인합니다.</li>
</ul>
</li>
<li>프로세스 모니터링<ul>
<li>가장 많은 CPU와 메모리를 사용하는 프로세스를 확인하여 시스템 자원 관리에 도움이 된다.</li>
</ul>
</li>
</ul>
<h2 id="nmon-사용-방법">Nmon 사용 방법</h2>
<ul>
<li><p>인터랙티브 모드 : <code>nmon</code></p>
</li>
<li><p>데이터 수집 모드: 특정 시간동안 데이터를 수집하고, 로그파일로 저장하는 모드. </p>
<ul>
<li><p><code>nmon -f -s 30 -c 120</code></p>
</li>
<li><p>-f: 로그 파일 형식으로 저장</p>
</li>
<li><p>-s 30: 30초 간격으로 데이터 수집</p>
</li>
<li><p>-c 120: 총 120번 데이터 수집(총 1시간 동안 수집)</p>
<pre><code class="language-bash">#!/bin/bash
</code></pre>
</li>
</ul>
</li>
</ul>
<h1 id="날짜와-시간을-형식에-맞게-저장">날짜와 시간을 형식에 맞게 저장</h1>
<p>DATE=$(date +&quot;%Y%m%d_%H%M%S&quot;)</p>
<h1 id="로그-파일을-저장할-디렉토리-설정">로그 파일을 저장할 디렉토리 설정</h1>
<p>LOG_DIR=&quot;/var/log/nmon_logs&quot;</p>
<h1 id="로그-파일-이름-설정">로그 파일 이름 설정</h1>
<p>LOG_FILE=&quot;${LOG_DIR}/nmon_${DATE}.nmon&quot;</p>
<h1 id="로그-디렉토리가-없으면-생성">로그 디렉토리가 없으면 생성</h1>
<p>if [ ! -d &quot;$LOG_DIR&quot; ]; then
    mkdir -p &quot;$LOG_DIR&quot;
fi</p>
<h1 id="nmon을-실행하여-데이터를-수집">Nmon을 실행하여 데이터를 수집</h1>
<h1 id="-f-파일로-저장--s-60-60초-간격으로-수집--c-60-60번-수집-즉-1시간-동안-수집">-f: 파일로 저장, -s 60: 60초 간격으로 수집, -c 60: 60번 수집 (즉, 1시간 동안 수집)</h1>
<p>nmon -f -s 60 -c 60 -m &quot;$LOG_DIR&quot; -F &quot;$LOG_FILE&quot;</p>
<p>echo &quot;Nmon data collected and saved to $LOG_FILE&quot;</p>
<pre><code>- 이 스크립트를 크론(cron)에 등록하여 주기적으로 실행하면, 서버의 성능 데이터를 정기적으로 수집할 수 있습니다. 
  - 이렇게 수집된 데이터를 바탕으로, 성능 추세를 분석하거나 문제가 발생하였을 때 원인을 파악하는 데 유용합니다.</code></pre>