<h3 id="세마포어">세마포어</h3>
<ul>
<li>어떤 자원의 현재 사용 여부를 표현한다.</li>
<li>세마포어는 여러 개를 묶어 세트로 사용한다.</li>
<li>메모리 블록을 사용하기 전에, 사용중(set)이면 Process는 대기하고 있다 release되어 unset이 되는 순간 세마포어를 set으로 세팅하고 자원을 사용할 수 있게 된다.<ul>
<li>set/unset 두 가지 값을 갖는다.</li>
</ul>
</li>
</ul>
<h3 id="개념">개념</h3>
<p><strong>1. 공유 자원 보호</strong></p>
<ul>
<li>여러 개의 프로세스가 하나의 공유 자원(ex: 파일, 메모리, 데이터베이스 등) 에 접근할 때, 충돌을 방지하기 위해 사용된다.</li>
</ul>
<p><strong>2. 동기화(Synchronization)</strong></p>
<ul>
<li>한 프로세스가 공유 자원을 사용 중일 때, 다른 프로세스가 이를 방해하지 못하도록 동기화 역할을 한다.</li>
</ul>
<p><strong>3. 카운터 기반 제어</strong></p>
<ul>
<li>세마포어는 정수값(카운터)로 표현되며, 프로세스가 자원을 요청하면 값을 감소하고, 사용을 마치면 증가시키는 방식으로 동작한다.</li>
</ul>
<ul>
<li><p>Oracle Database에서는 백그라운드 프로세스 간 동기화를 위해 세마포어를 사용한다.</p>
</li>
<li><p>SGA 접근 제어에도 사용되며, 프로세스드이 동시에 공유 메모리를 안전하게 사용할 수 있도록 보장한다.</p>
</li>
<li><p>ipcs -ls :세마포어 시스템에 대한 상세 정보를 출력</p>
</li>
</ul>
<hr />
<pre><code>(oracle)$ ipcs -ls :세마포어 시스템에 대한 상세 정보를 출력
------ Semaphore Limits --------
max number of arrays = 128 👈SEMMNI
max semaphores per array = 250 👈SEMMSL
max semaphores system wide = 32000👈SEMMNS
max ops per semop call = 100👈SEMOPM
semaphore max value = 32767 : 각 세마포어가 가질 수 있는 최대 값(정수값)</code></pre><ul>
<li><strong>SEMMSL</strong>: (Maximum Semaphores per Array)<ul>
<li>세마포어 세트당 세마포어 최대 개수를 정의한다.</li>
</ul>
</li>
<li><strong>SEMMNI</strong>: (Maximum Number of Semaphore Arrays)<ul>
<li>리눅스 전체에서 설정 가능한 세마포어 세트의 최대 개수 </li>
</ul>
</li>
<li><strong>SEMMNS</strong>: (Maximum Semaphores System-Wide)<ul>
<li>리눅스 전체에서 사용 가능한 세마포어의 최대 개수</li>
<li>SEMMSL * SEMMNI 값보다 크거나 같아야 한다.</li>
</ul>
</li>
<li><strong>SEMOPM</strong>: (Maximum Operations per semop call)<ul>
<li>1call (1개의 시스템 호출)이 초당 호출 가능한 최대 세마포어 개수를 정의한다.</li>
<li>SEMOPM 값이 100이면, 한 번의 세마포어 연산에서 최대 100개의 <strong>세마포어에 대한 동작
(상태 변경)</strong>을 처리할 수 있다.</li>
<li>예를 들어, 세마포어 A, B, C에 대해 각각 P 연산(잠금)을 수행한다고 하면, 한 번의 semop 호출로 최대 100개까지 처리할 수 있다.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/08433218-79d8-4b5a-9cd4-533dc6efe547/image.png" /></p>
<hr />
<ul>
<li><strong>SHMMAX</strong><ul>
<li>Kernel이 Oracle에게 공유 메모리를 할당해줄 때 </li>
<li>메모리 세그먼트의 최대 크기(바이트 단위)를 정의하는 데 사용된다.<pre><code class="language-shell">$ cat /proc/sys/kernel/shmmax
4012533760 (약 3.74GB)</code></pre>
</li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li>SGA는 공유 메모리로 구성되어 여러 Server Process들이 공유해서 사용된다. 
많은 프로그램들이 동시에 공유 메모리를 사용, 공유 메모리의 용량 또한 아주 큰 경우가 많기에 kernel이 응용 프로그램들에게 메모리를 할당해 줄 때 작게 여러 번 할당하지 않고 큰  덩어리로 한꺼번에 주게 된다. 이를 <strong><span style="color: red;">세그먼트</span></strong>(큰 덩어리)라고 한다.</li>
</ul>
</blockquote>
<ul>
<li><strong>SHMMNI</strong>: (Maximum Number of Semaphore Arrays)<ul>
<li>공유 메모리 <code>세그먼트의 최대 개수</code>; default : 4096<pre><code class="language-shell"></code></pre>
</li>
</ul>
</li>
</ul>
<p>$ cat /proc/sys/kernel/shmmni
4096</p>
<pre><code>- **SHMALL**: 
  - 특정 시점에 시스템에서 사용 가능한 공유 메모리 최대 크기
  - `ceil(SHMMAX/PAGE_SIZE)`: 이 값보다 큰 값을 사용할 것을 권장
  - default: 2097152 bytes 
```shell
$ cat /proc/sys/kernel/shmall
1959245</code></pre><ul>
<li><p><strong>SHMMIN</strong></p>
<ul>
<li>단일 공유메모리 세그먼트 최소 크기(byte)를 의미</li>
</ul>
</li>
<li><p><strong>SHMSEG</strong></p>
<ul>
<li>1개의 프로세스에 부여될 수 있는 공유메모리 세그먼트의 최대 개수를 의미한다.</li>
<li>SHMMNI: 시스템 전체에서 사용 가능한 공유 메모리 세그먼트 최대 개수이고</li>
<li>SHMSEG: 1개의 프로세스가 사용할 수 있는 공유 메모리 세그먼트의 최대 개수 </li>
</ul>
</li>
<li><p><strong>SEMVMX</strong> : Semaphore Maximum Value</p>
</li>
<li><p>각 세마포어가 가질 수 있는 최대 값을 의미한다.</p>
</li>
</ul>
<h3 id="값-변경-후">값 변경 후</h3>
<ul>
<li><p>(일시적)<code>sysctl -w</code>: 커널 파라미터 값을 즉시 변경하지만, 재부팅 후에는 원래 값으로 복원됨.</p>
<ul>
<li>ex) # sysctl -w kernel.shmmax=4294967296</li>
</ul>
</li>
<li><p>(영구적)<code>sysctl -p</code>: 파일에서 설정값 로드, 영구적 적용 가능</p>
</li>
<li><p>/etc/sysctl.conf: 영구적인 커널 설정 저장</p>
</li>
<li><p>/proc/sys/kernel: 현재 실행 중인 커널 값 저장 ,즉시 반영되지만 재부팅 시 초기화된다.</p>
</li>
</ul>
<h2 id="sga-할당">SGA 할당</h2>
<ol>
<li>공유 메모리로 사용할 물리적 메모리가 충분할 경우, 하나의 segment에 전체 SGA가 할당될 수 있음</li>
<li>만약 하나의 segment에 다 할당할 수 없다면, 연속된 여러 segment 로 분산시켜 할당할 수도 있음</li>
<li>여러 segment에 분산시켜 할당할 수 있다.</li>
</ol>