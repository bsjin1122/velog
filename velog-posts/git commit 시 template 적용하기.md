<h2 id="상황">상황</h2>
<ul>
<li>커밋 메시지에 어떤 전략으로 작성할지 헷갈릴 때가 많고, 놓칠 때가 많았다. 팀원분께서 적용해주시는 꿀팁을 알려주셔서 적어본다.</li>
</ul>
<h2 id="해결방법">해결방법</h2>
<blockquote>
<p>터미널에서 <code>git config commit.template [적용할템플릿.txt]</code></p>
</blockquote>
<ol>
<li>.gitmessage.txt 파일을 최상단에 만들어두었다.<pre><code class="language-txt">[Type] title
# [Type] 입력 목록
#  1. Feat: 새로운 기능 추가
#  2. Fix: 오류 및 문제 해결
#  3. Test: 테스트와 관련된 모든 것
#  4. Refactor: 코드 리팩토링
#  5. Style: 기능 수정 없이 코드 스타일만 변경한 경우 (코드 포매팅, 세미콜론 누락 등)
#  6. Chore: 빌드 업무 수정, 패키지 매니저 수정 (gitignore 수정 등)
#  7. Docs: 문서화에 관한 모든 것
#  8. Rename: 파일 혹은 폴더명을 수정만 한 경우
#  9. Remove: 파일을 삭제만 한 경우
#  10. Perf: 성능 개선
</code></pre>
</li>
</ol>
<p>```
2. 명령어를 입력하고 파일 변경을 해보았더니 
<img alt="" src="https://velog.velcdn.com/images/greendev/post/28122aac-4a00-48e1-b823-ba211accd490/image.png" /></p>
<p>반영 완료~~</p>