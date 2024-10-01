<blockquote>
<p>왜 대기와 오라클의 Lock을 배워야 하는가? </p>
</blockquote>
<ul>
<li><p>Lock 대기, Deadlock(교착 상태)와 같은 장애를 만날 수도 있다.</p>
</li>
<li><p>Lock의 본질: <code>다중 처리를 구현하기 위해 데이터를 보호한다</code></p>
</li>
<li><p>대기(wait): 기다린다를 표시하는 것</p>
<ul>
<li><code>Idle 대기</code>: 처리할 것이 있어 쉬고 있는 대기</li>
<li><code>Non-Idle 대기</code>: 이유가 있어 어쩔 수 없이 하는 대기, 이상 상태 등 쓸데없이 SQL을 기다리게 하는 대기</li>
</ul>
</li>
<li><p>대기 이벤트(wait event): 기다리게 만든 작업</p>
<ul>
<li>Idle 대기 이벤트<ul>
<li>성능 분석할 때에는 신경쓰지 않아도 된다. SQL의 처리를 기다리게 하지 않는다.</li>
<li>SQL *Net message from client(클라이언트에서 오는 SQL문 등을 기다리고 있다)</li>
<li>smon timer</li>
<li>pmon timer</li>
<li>rdbms ipc message</li>
<li>wakeup time manager</li>
<li>Queue Monitor Wait  등 </li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 id="non-idle-대기는-주의">Non-Idle 대기는 주의</h2>
<ul>
<li>이유가 있어 어쩔 수 없이 하는 대기: 디스크 I/O 대기</li>
<li>이상 상태 등 쓸데 없이 SQL을 기다리게 하는 대기<ul>
<li>ex) 한 사용자가 어떤 테이블에 Lock을 걸어버린 후에 식사하러 갔다 등</li>
</ul>
</li>
<li>디스크 장애로 인한 지연<ul>
<li>같은 대기 이벤트라도 이런 사례들처럼 <code>어쩔 수 없는 것</code>과 <code>이상한 (쓸데 없는) 것</code></li>
</ul>
</li>
</ul>
<blockquote>
<p>어쩔 수 없는 것이라 하더라도, 애플리케이션의 처리를 줄임으로써 전체 대기 시간을 단축하는 경우도 있다.</p>
</blockquote>
<ul>
<li>SQL 처리 과정을 튜닝한다는 관점으로 바라보면, Non-Idle 대기 이벤트 + SQL 처리에 사용하는 CPU 시간이 SQL이 걸린 시간이므로, 매우 중요하다. </li>
<li>대기 이벤트는 스태츠팩(또는 AWR), v$session_wait에서 볼 수 있다.</li>
</ul>
<h2 id="lock에-의한-대기는">Lock에 의한 대기는?</h2>
<ul>
<li><p>Lock을 걸었다는 것 자체만으로 대기가 발생하지 않으며, Lock이 걸려있는 대상에서 다시 Lock을 걸려할 떄 대기가 발생한다. </p>
</li>
<li><p>v$lock에서 확인할 수 있다.</p>
<ul>
<li>조회 시 REQUESTED 컬럼에 보이면, NONE이 아닌 X면, Lock을 요청ㅇ하고 있는 것이다.</li>
<li>Lock Type: TX, TM</li>
<li>MR이라는 lock이 여러 개 보이지만, 인스턴스가 기동하면 자동으로 얻는 Lock이므로 무시해도 괜찮다. 
<img alt="" src="https://velog.velcdn.com/images/greendev/post/cc1d981f-7647-4dc6-a8a1-453ac7e7399b/image.png" /></li>
</ul>
</li>
<li><p><code>/*+ ORDERED */</code> : 조인하는 순서를 정하는 힌트로, SQL문의 성능 저하를 막아준다. </p>
</li>
</ul>
<h2 id="lock-type--tx-tm">Lock Type : TX, TM</h2>
<h3 id="tx">TX</h3>
<ul>
<li>row와 관련된 lock</li>
<li>MODE는 동시성 제어를 위한 것: Lock이 어떤 형태로 걸려있는지를 표시해준다.<ul>
<li>예를 들어, TX Lock의 X(배타적, Exclusive)는 같은 row에 대하여 다른 MODE의 Lock을 허용하지 않는다. <h3 id="tm">TM</h3>
</li>
</ul>
</li>
<li>테이블에 거는 Lock</li>
</ul>
<h2 id="deadlock의-구조">Deadlock의 구조</h2>
<ul>
<li>고장난 열쇠: 고장나서 작동하지 않는 열쇠</li>
<li>서로가 상대방이 보유하고 있는 Lock을 기다리느라, 영원히 작업 처리를 진행할 수 없는 상태를 말한다.</li>
<li>Deadlock(ORA-00060 발생) 일 때는 한쪽의 처리가 오라클에 의해 자동으로 롤백되며, 
<code>alert 파일과 트레이스 파일에 정보가 표시된다.</code></li>
<li>오라클의 버전에 따라서는 기록되는 정보의 양이 다를 수 있지만, 9i 이후 버전이라면 Deadlock이 발생한 SQL문을 양쪽 모두 알 수 있어 애플리케이션 수정 시 도움이 된다.</li>
</ul>
<h2 id="latch의-구조">Latch의 구조</h2>
<ul>
<li><p>다중 처리를 구현하기 위한 Lock</p>
</li>
<li><p>일반적인 Lock과 다른 부분은, Latch는 오라클 내부에서 자동으로 얻으며, SQL을 한 번 실행하기 위해서는 여러 Latch를 얻고 해제하는 것을 반복한다는 것이다.</p>
</li>
</ul>
<h2 id="요약">요약</h2>
<blockquote>
<ul>
<li>대기는 단순히 기다리고 있는 상황을 표시하는 것에 지나지 않는다.</li>
</ul>
</blockquote>
<ul>
<li>Idle 대기 이벤트, Non-Idle 대기 이벤트</li>
<li>Lock은 데이터를 보호하기 위해 존재한다.</li>
<li>Deadlock은 상대방이 소유하고 있는 Lock을 요청해서 작업의 처리를 진행하지 못하는 상태.</li>
<li>Lock 경합을 해소하기 위해서는 애플리케이션 측에서 대처해야 할 때가 많다.</li>
<li>Latch는 오라클 내부의 중요한 것(특히 메모리)을 보호하기 위해 존재</li>
<li>대형 시스템이 아닌데, Latch 경합이 심하다면 CPU 자원이 부족하거나 페이징이 발생하는 등의 바람직하지 않은 상태인지를 확인한다.</li>
<li>오라클을 정상적으로 운영하기 위해서는 토대가 되는 OS도 정상적인 상태여야 한다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/c6d313d6-8ded-4d3c-8979-6f7644e1a776/image.png" /></p>