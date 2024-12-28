<ul>
<li>apt update   # 최신 패키지 정보를 가져옴</li>
<li>dpkg --configure -a<ul>
<li>dpkg는 Debian 패키지 관리 시스템의 저수준 도구로, 직접 패키지를 설치하거나 설정하는 데 사용된다.</li>
<li><code>--configure -a</code>는 현재 설치된 패키지 중 설정(configure)이 완료되지 않은 패키지를 찾아 이를 다시 설정(configure)한다.<pre><code class="language-shell">root@sj:~# dpkg --configure -a
Setting up tzdata (2024a-0+deb12u1) ...
Current default time zone: 'Asia/Seoul'</code></pre>
</li>
</ul>
</li>
<li>apt upgrade # 최신 정보를 기반으로 패키지를 업그레이드</li>
</ul>