<h2 id="상황">상황</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/3fa3cf1f-ce7a-4872-b992-8ffac9cb0022/image.png" /></p>
<ul>
<li>Github 를 통해 로그인이 완료되었음에도 불구하고 push가 안되고 있었다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/6046cd89-6403-4fde-aa79-4c2d589383a8/image.png" /></li>
<li>그래서 Github token으로 발급받아 로그인을 해야한다. </li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/ba9f6014-ca87-4886-a0a0-2c2caaf36d23/image.png" /></p>
<ul>
<li>생성 버튼 누르면 화면이 새 창으로 뜬다.</li>
</ul>
<p>선택돼 있는 설정값 그대로 하고,,, 생성을 눌러 값을 복사한 뒤 로그인 화면으로 돌아가 넣었더니 생성되었다.</p>
<hr />
<details>
  잘못 이해하고 만든 token 발급법
1. Github 우측 이모지를 눌러 아래 탭에서, Settings-Developer Settings
![](https://velog.velcdn.com/images/greendev/post/56c94dfa-4703-45a9-bfa1-f6c805db70c1/image.png)

<ol start="2">
<li>Register new GitHub App</li>
</ol>
<ul>
<li>2024도 기준 ui가 바뀐 모양이다...
<img alt="" src="https://velog.velcdn.com/images/greendev/post/99c13879-67e7-4ff2-b235-212670d1bf0e/image.png" /></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/a225d370-9668-4fda-9cc7-6bde0586a282/image.png" /></p>
<ul>
<li>Github App name은 Github/Gist로 시작하면 안된다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/a1ad1a2a-2cec-4b69-aaaa-ee9753350d53/image.png" /></li>
<li>내 계정명을 적어주었다..</li>
<li>아래 url은 github 주소 적었다. webhook 은 체크 해제 했다.!
create Github App 을 눌러 생성해보겠다..</details>
</li>
</ul>