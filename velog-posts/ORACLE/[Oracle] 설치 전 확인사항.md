<p><strong>1. 서버, O/S 확인</strong>
<strong>2. 3rd part Cluster</strong></p>
<ul>
<li>AIX -&gt; Power HA (구 HACMP)<ul>
<li>Shared LUN</li>
<li>Cluster Filesystem</li>
<li>gpfs</li>
</ul>
</li>
<li>HP -&gt; Serviceguard</li>
<li>Solaris -&gt; Sun cluster</li>
<li>LINUX -&gt; Veritas Cluster Server (VCS)</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/edcdc0f3-ee1e-4e08-af02-2e2d8a67162a/image.png" />
Certifications 탭에 들어가서, 
Product/ Release/Platform 선택 후 검색
<img alt="" src="https://velog.velcdn.com/images/greendev/post/d8e92d9e-73ba-4b65-9920-474399a9fb4b/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/4c518d0d-1f7a-4243-af9d-84ca15e6b470/image.png" /></p>
<ul>
<li>호환되는 버전을 확인한다.</li>
</ul>
<hr />
<p><strong>3. 설치 미디어 파일 전달 + pre requirement word파일. 파일도 같이 전달</strong></p>
<blockquote>
<p>** RAC 구성할 때 필요한 것 **</p>
</blockquote>
<ul>
<li>서버 2대, Shared Storage, L2 Switch</li>
<li>IP Public 5개(r:2, v:2, s:1), Private (2개(각각))</li>
</ul>
<p>*<em>4. 미디어파일 업로드 *</em></p>
<p><strong>4.1 하면서 설치전 확인 사항, crosscheck</strong></p>
<p><strong>5. GRID Install</strong></p>
<p><strong>6. DB Install</strong></p>
<p><strong>7. patch</strong></p>
<p><strong>8. DBCA</strong></p>
<h2 id="설치">설치</h2>
<ul>
<li>압축을 풀 때 $ORACLE_HOME에 풂</li>
<li>opatch를 안 함 </li>
<li>RU 24 + Interim </li>
<li>19.24 RU <ul>
<li>1년에 4번 오라클 발표 </li>
<li>1, 4, 7, 10월</li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li>MBP: 매달 주요 패치 / 몇십개~몇 백개 패치</li>
</ul>
</blockquote>
<ul>
<li>Interim patch(on, off) <ul>
<li>특정 이슈 1개를 bug fix</li>
</ul>
</li>
</ul>