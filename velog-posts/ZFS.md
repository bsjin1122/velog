<ul>
<li><p><a href="https://www.fujitsu.com/jp/products/computing/servers/unix/sparc/technical/keytopia/expedition/22/">출처: 스냅샷</a></p>
</li>
<li><p>Oracle Solaris에서는 OS 표준의 Rollback이나 Backup/restore라는 기능으로, Snapshot에 기록한 과거의 한 순간으로 되돌리는 것이 가능하다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/13df3513-7436-4559-ae1c-822b78951b91/image.png" /></p>
</li>
</ul>
<h3 id="snapshot">Snapshot</h3>
<ul>
<li>이름 그대로 snap사진과 같은 것으로, 그 시점의 상태를 찍은 것을 말한다.</li>
<li>snapshot은 다양한 OS나 software에서 이용되고 있다.</li>
<li>Oracle Solaris(이후 solaris)에서는 zfs file system의 기능으로서 zfs snapshot을 제공하고 있다.</li>
<li><code># zfs snapshot rpool/data@snapshot1(임의의스냅샷명)</code> : 스냅샷 생성</li>
</ul>
<h3 id="rollback">rollback</h3>
<ul>
<li>스냅샷을 생성했을 때의 상태로 돌리는 rollback
<img alt="" src="https://velog.velcdn.com/images/greendev/post/a33a4db8-906f-4c2f-929d-0f40406f61bb/image.png" /></li>
<li>작업 전에 스냅샷을 찍어두는 것으로, 실수로 파일을 삭제한 경우에도 rollback으로 원래의 상태로 돌릴 수 있다.</li>
<li>또한 patch를 적용했더니 중대한 장애가 발생해버렸을 때 등, 생각 밖의 사건이 발생한 경우에도 장애 발생 전으로 snapshot을 찍어두는 것으로, 원래 상태로 돌릴 수 있다.</li>
</ul>
<blockquote>
<p>snapshot은, snapshot을 조회한 filesystem 상에서 만들어진다. 이번 예에서는, filesystem &quot;rpool/data&quot; 밑에 snapshot이 만들어져 있는데, file system인 rpool/data를 삭제하면 snapshot도 같이 삭제되어 rollback 할 수 없게 된다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/7f794932-bd63-4f39-960a-68d751436567/image.png" /></p>
</blockquote>
<ul>
<li>rollback 수행 시 <code>-r</code> 옵션을 지정하면, 대상의 snapshot보다 새로운 snapshot을 삭제하여 rollback이 실행된다.</li>
</ul>
<h3 id="backuprestore">Backup/Restore</h3>
<ul>
<li>rollback: 특정 스냅샷 상태로 돌리는 기능</li>
<li>backup: snapshot으로부터 archive를 생성하여, 지정한 장소에 백업(file 보관)하는 기능</li>
<li>restore: 저장해둔 backup을 사용하여 복원하는 기능</li>
</ul>