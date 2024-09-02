<blockquote>
<p>github에 pr(pull request) 및 issue를 등록하면, discord에 push 알림이 가도록 설정해보기로 한다!</p>
</blockquote>
<h2 id="1-디스코드-채널에서-설정">1. 디스코드 채널에서 설정</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/2f241815-f688-4322-96bb-5133478bf71b/image.png" /></p>
<ul>
<li>연동 탭에서 <code>웹후크</code> 선택
<img alt="" src="https://velog.velcdn.com/images/greendev/post/166094fa-e2d2-4013-9379-aae91e429406/image.png" /></li>
<li>새 웹후크 선택
<img alt="" src="https://velog.velcdn.com/images/greendev/post/51302776-6547-401d-8045-5e121016eec3/image.png" /></li>
<li>웹후크 URL 복사 (URL은 노출되지 않도록 주의한다.)
<img alt="" src="https://velog.velcdn.com/images/greendev/post/392241d2-4695-4cbe-a15a-4af03fbb6067/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/4b8e007e-fced-49ca-bd69-dc75f0270528/image.png" /></li>
</ul>
<h2 id="2-github---settings">2. Github - Settings</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/629513b5-fbd3-487f-a27c-ee409a4ebf69/image.png" /></p>
<ul>
<li>Settings - Webhooks - Add webhook
<img alt="" src="https://velog.velcdn.com/images/greendev/post/9487e366-84d7-4e11-8229-7c22e5ef050c/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/2cd0c2ff-d0ec-4165-af5e-61d9144d5261/image.png" /></li>
</ul>
<blockquote>
<ul>
<li>Payload URL: 복사했던 웹후크 URL 뒤 <strong><code>/github</code></strong> 만 끝에 추가</li>
</ul>
</blockquote>
<ul>
<li><a href="https://discordapp.com/api/webhooks/%7B%EC%9B%B9%ED%9B%84%ED%81%AC%EC%95%84%EC%9D%B4%EB%94%94%7D/%7B%EC%9B%B9%ED%9B%84%ED%81%AC%ED%86%A0%ED%81%B0%7D/github%F0%9F%91%88">https://discordapp.com/api/webhooks/{웹후크아이디}/{웹후크토큰}/github👈</a><blockquote>
<ul>
<li>Content Type: application/json</li>
</ul>
</blockquote>
</li>
</ul>
<h3 id="3-어떤-이벤트일-때-트리거를-날릴지-선택하기">3. 어떤 이벤트일 때 트리거를 날릴지 선택하기</h3>
<blockquote>
<ul>
<li>✅ Just the push event. -- Push 이벤트만 trigger✅</li>
</ul>
</blockquote>
<ul>
<li><input disabled="" type="checkbox" /> Send me everything. -- 이벤트 전체에 trigger</li>
<li><input disabled="" type="checkbox" /> Let me select individual events. -- 이벤트 커스터마이징</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/46105233-ca13-452d-94e4-70f38040c55a/image.png" />
뭔가 3번째는 선택할 수 있는 것 같다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/f9a33577-a8b4-423d-895e-5342fcb4748a/image.png" /></p>
<ul>
<li><p>3개만 옵션 체크해주었다.</p>
</li>
<li><p>Issue를 한번 만들어봤더니 알림이 잘 와있는 것을 확인할 수 있었습니다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/29cfbcbb-1f23-4926-9cdb-062457047234/image.png" /></p>
</li>
</ul>