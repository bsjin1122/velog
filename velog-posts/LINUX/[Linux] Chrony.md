<h2 id="chrony란">Chrony란</h2>
<ul>
<li>네트워크 시간 동기화(Network Time Synchronization)을 위한 소프트웨어</li>
<li>Linux 시스템에서 NTP(Network Time Protocol)을 사용하여 시스템 시간을 동기화하는 역할 </li>
<li>오프라인에서도 동작 가능, 빠르게 시간 동기화 가능, 가상머신이나 컨테이너 환경에서도 높은 정확도를 유지</li>
</ul>
<h3 id="1-chrony-설치">1. Chrony 설치</h3>
<pre><code class="language-shell"># Red Hat / CentOS / Rocky Linux / Oracle Linux
sudo yum install -y chrony

# Ubuntu / Debian
sudo apt install -y chrony</code></pre>
<h3 id="2-chrony-서비스-활성화-및-시작">2. Chrony 서비스 활성화 및 시작</h3>
<pre><code class="language-shell">sudo systemctl enable chronyd    # 부팅 시 자동 실행
sudo systemctl start chronyd     # 서비스 시작
- chronyd: daemon process</code></pre>
<h3 id="3-동기화-상태-확인">3. 동기화 상태 확인</h3>
<pre><code class="language-shell">chronyc tracking


===
Reference ID    : 1A2B3C4D (time.google.com)
Stratum         : 2
Ref time (UTC)  : Mon Feb 17 12:34:56 2025
System time     : 0.0000321 seconds fast of NTP time
Last offset     : -0.0000021 seconds
RMS offset      : 0.0000017 seconds
</code></pre>
<ul>
<li>Reference ID: 동기화된 NTP 서버 주소</li>
<li>Stratum: 시간 계층 (1이면 원본 서버, 2 이상이면 NTP 서버를 거친 시간)</li>
<li>System time: 현재 시스템 시간이 NTP 시간과 얼마나 차이나는지</li>
<li>Last offset: 마지막 시간 오차 값</li>
<li>RMS offset: 오차의 평균값 (작을수록 정확)</li>
</ul>
<h3 id="4-현재-사용중인-ntp-서버-목록-확인">4. 현재 사용중인 NTP 서버 목록 확인</h3>
<pre><code>chronyc sources -v</code></pre><h3 id="5-ntp-서버-설정-변경">5. NTP 서버 설정 변경</h3>
<pre><code class="language-shell">sudo vi /etc/chrony.conf



server time.google.com iburst
server ntp.ubuntu.com iburst

- iburst: 부팅 후 빠르게 동기화하도록 설정하는 옵션

설정 변경 후 Chrony 재시작
sudo systemctl restart chronyd</code></pre>
<h3 id="6-강제-동기화">6. 강제 동기화</h3>
<pre><code>sudo chronyc makestep
- 즉시 시스템 시간을 NTP서버와 동기화한다.</code></pre>