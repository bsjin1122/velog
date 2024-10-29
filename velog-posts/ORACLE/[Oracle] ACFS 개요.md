<ul>
<li><p>출처: <a href="https://docs.oracle.com/cd/F19136_01/ostmg/overview-acfs-advm.html">Oracle ACFS 개요</a></p>
</li>
<li><p>Oracle Automatic Storage Management Cluster File System(Oracle ACFS)</p>
</li>
<li><p>멀티플랫폼의 scalable한 파일 시스템</p>
</li>
<li><p>Oracle Automatic Storage Management(Oracle ASM) 기능을 확장하여 모든 커스텀 파일을 support하는 스토리지 관리 기술이다. </p>
</li>
<li><p>Oracle ACFS에서는 실행가능 파일, 데이터베이스, 데이터파일, 데이터베이스 trace 파일, 데이터베이스, alert log, application, repor, bfile 및 구성 파일 등, </p>
<ul>
<li>Oracle Database 파일 및 application file이 support된다. </li>
<li>그 밖에도, video, text, image, 설계도 그 밖의 범용 application 파일, 데이터가 서포트됨.</li>
</ul>
</li>
<li><p>Oracle ACFS는, Linux 및 Unix의 경우에 POSIX 표준에 준거</p>
</li>
<li><p>Oracle ACFS 파일 시스템은 Oracle ASM과 통신하여, Oracle ASM 스토리지를 사용하여 구성된다. 
<img alt="" src="https://velog.velcdn.com/images/greendev/post/1ca73a96-81f7-46f8-b010-903e73986da4/image.png" /></p>
</li>
</ul>
<blockquote>
<ul>
<li>Oracle ACFS의 동적인 파일, 시스템 사이즈 변경 </li>
</ul>
</blockquote>
<ul>
<li>Oracle ASM 디스크 그룹, 스토리지로의 직접 접근에 따른 수행을 최대화</li>
<li>I/O 병렬성 향상에 따른 Oracle ASM 디스크 그룹, 스토리지 전체에서의 oracle ACFS의 분산 평균화 </li>
<li>Oracle ASM 미러링 보호? 메커니즘에 따른 데이터 신뢰성 확보</li>
</ul>