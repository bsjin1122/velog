<blockquote>
<h2 id="mos">MOS</h2>
</blockquote>
<ul>
<li>Configuring HugePages (Doc ID 1479908.1)    </li>
<li>Oracle Linux: Shell Script to Calculate Values Recommended Linux HugePages / HugeTLB Configuration (Doc ID 401749.1)    </li>
</ul>
<h1 id="docs-hugepages">Docs Hugepages</h1>
<ul>
<li><a href="https://docs.oracle.com/cd/F19136_01/unxar/administering-oracle-database-on-linux.html#GUID-CC72CEDC-58AA-4065-AC7D-FD4735E14416">docs.oracle.com/jp: Hugepages의 개요</a><h2 id="hugepages-개요">Hugepages 개요</h2>
</li>
<li>HugePages size는 2MB~256MB</li>
<li>Oracle Database의 경우, HugePages를 사용하면 Pages 상태의 OS Maintenance가 경감되어 Translation Lookaside Buffer(TLB) 히트율이 향상된다.</li>
</ul>
<p><strong>HugePages 메모리 할당 확인</strong></p>
<pre><code class="language-shell">[root@kidjin5 20250331-23:13:03]::[/root]
$ grep Huge /proc/meminfo
AnonHugePages:    223232 kB
ShmemHugePages:        0 kB
FileHugePages:    167936 kB
HugePages_Total:       0 👈 설정된 Hugepages 총개수
HugePages_Free:        0 👈 아직 사용되지 않은 수
HugePages_Rsvd:        0 
HugePages_Surp:        0
Hugepagesize:       2048 kB 👈 한 페이지 크기 (2MB)
Hugetlb:               0 kB
</code></pre>
<ul>
<li></li>
<li><p><em>Linux에서의 Hugepages구성*</em></p>
</li>
<li><p><code>$ grep Huge /proc/meminfo</code></p>
</li>
<li><p><code>/etc/security/limits.conf</code> 파일의 memlock 설정을 변경한다. </p>
<ul>
<li>이 파일은 리눅스에서 사용자(ex: oracle)가 잠글 수 있는 메모리 양의 상한선을 지정하는 설정이다.<ul>
<li>soft: 경고 없이 사용 가능한 최대 메모리</li>
<li>hard: 절대 초과할 수 없는 최대 메모리 </li>
</ul>
</li>
</ul>
</li>
<li><p>memlock 설정은 <code>KB 단위</code>로 지정하고, </p>
</li>
<li><p>Lock되는 memory 상한선을 HugePages 메모리가 유효한 경우엔 현행의 RAM 90% 이상으로 설정하고, 무효한 경우엔 145728KB (3GB)이상으로 설정해야 한다.</p>
</li>
</ul>
<pre><code class="language-bash">64GB × 90% = 57.6GB
57.6GB = 57600MB = 57600 × 1024 = **58982400 KB**

→ memlock 설정:
oracle soft memlock 58982400 
oracle hard memlock 58982400</code></pre>
<pre><code class="language-shell">*   soft   memlock    60397977
*   hard   memlock    60397977
-- ex) 6291456KB = 6GB → HugePages로 할당할 수 있는 메모리 한도</code></pre>
<h3 id="memlock을-설정해야-하는-이유">memlock을 설정해야 하는 이유</h3>
<ul>
<li>HugePages로 메모리를 할당하려면, 해당 메모리를 잠글(lock)수 있어야 하기 때문이다.</li>
<li>리눅스는 기본적으로 프로세스가 사용하는 메모리를 swap하거나 이동할 수 있게 설계되어 있는데, <strong>HugePages는 이동 불가능, 고정된 메모리</strong>이기 때문에, 잠글 수 있는 크기를 먼저 지정해줘야한다.<ul>
<li>memlock 값이 낮으면 HugePages가 충분히 설정돼 있어도 사용하지 못할 수 있다. </li>
</ul>
</li>
<li>memlock 값을 SGA 요건보다도 크게 설정하는 것도 가능하다.</li>
<li>oracle User로서 재로그인 한 후, <code>ulimit -l</code> 명령어로 새로운 memlock 설정을 확인한다.</li>
<li><code>$ grep Hugepagesize /proc/meminfo</code> 값을 확인한다.</li>
<li>현행의 Shared Memory Segment의 hugepages구성의 권장값을 계산하는 script 실행 방법<ul>
<li><a href="https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=273574277070798&amp;id=401749.1&amp;_adf.ctrl-state=1c5pqymcb4_52#CODE">hugepages_settings.sh 파일</a></li>
<li><code>$ chmod +x hugepages_settings.sh</code></li>
<li><code>$ ./hugepages_settings.sh</code></li>
</ul>
</li>
</ul>
<h2 id="hugepages-개념">HugePages 개념</h2>
<ul>
<li>Linux에서 메모리 페이지를 효율적으로 관리하기 위한 기능</li>
<li>기본적으로 Linux는 메모리를 <code>작은 단위의 페이지 (보통4kb)</code>로 나눠서 관리</li>
<li>시스템 메모리가 클수록, 작은 페이지를 엄청 많이 관리해야 하므로, <code>페이지 테이블이 커지고, 오버헤드가 커진다.</code></li>
<li>그래서 고성능 시스템에서는 **큰 페이지(HugePages, 보통 2MB 또는 1GB)를 사용해 성능을 개선한다.</li>
</ul>
<hr />
<h2 id="use_large_pages-파라미터">USE_LARGE_PAGES 파라미터</h2>
<ul>
<li>Oracle 11.2.0.2부터 추가된 파라미터로, HugePages 사용 여부를 설정하는 데 사용된다.<h3 id="true">TRUE</h3>
</li>
<li>HugePages가 있으면 사용, 없으면 Small Pages(4kb) 사용</li>
</ul>
<h3 id="false">FALSE</h3>
<ul>
<li>HugePages를 전혀 사용하지 않음</li>
</ul>
<h3 id="only">ONLY</h3>
<ul>
<li>HugePages가 충분하지 않으면 DB를 시작하지 않음 (엄격한 모드)</li>
<li>전체 메모리에 대해 hugepages를 사용할 수 없는 경우 인스턴스를 시작하지 않음을 의미한다. (메모리 부족 방지 위해)</li>
</ul>
<h3 id="메모리-관리-방식">메모리 관리 방식</h3>
<ul>
<li><strong>ASMM</strong>: SGA_TARGET: O</li>
<li><strong>AMM</strong>: MEMORY_TARGET: X (Hugepages 사용 못함)<ul>
<li>이 둘도 조금 정리가 필요하다**</li>
</ul>
</li>
</ul>