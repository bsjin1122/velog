<blockquote>
<p>목차</p>
</blockquote>
<ul>
<li><a href="https://velog.io/@gmlstjq123/Github-Organization-%EB%A7%8C%EB%93%A4%EA%B8%B0">Github Organization 만들기</a></li>
<li><a href="https://api.velog.io/rss/@greendev#jira-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0">Jira 사이트 생성하기</a></li>
<li><a href="https://velog.io/@sangpok/Github-%ED%98%91%EC%97%85-%EC%84%A4%EC%A0%95Github-Issue-Jira-%EC%97%B0%EB%8F%99">참고한 사이트!</a></li>
</ul>
<h2 id="jira-사이트-생성하기">jira 사이트 생성하기</h2>
<ul>
<li>로그인 후 이름 생성
<img alt="" src="https://velog.velcdn.com/images/greendev/post/301461fc-c2fd-4fdb-aa2e-3ea6831acb53/image.png" /><ul>
<li>jira - Github for Jira</li>
</ul>
</li>
<li>상단의 &quot;앱&quot;에서 Github for Jira를 검색합니다.</li>
</ul>
<pre><code class="language-text">  https://[이름].atlassian.net/jira/marketplace/discover/app/com.github.integration.production</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/64ef9995-f821-4020-b412-0ea9b26ad787/image.png" /></p>
<ul>
<li>Get app 누르면 
<img alt="" src="https://velog.velcdn.com/images/greendev/post/37ea1008-b510-40fb-a7af-e80058077515/image.png" /></li>
<li>좌측 하단에 설치 완료
<img alt="" src="https://velog.velcdn.com/images/greendev/post/72ef0fa6-a47e-4bb5-af9e-568306e69976/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/43a4751b-d1c1-4c81-8b3c-85136edb68c7/image.png" /></li>
<li>딱히 도메인명을 github.com 으로 할지 미정이라, 일단 Github Cloud로 선택했다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/f4ed703e-66bd-4688-ac37-16a719c6c94e/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/73825a35-4738-4218-89ed-eb40c3ae414f/image.png" /></li>
<li>한 리포지토리만 다룰 것이 아니기에, All Repositories로 선택
<img alt="" src="https://velog.velcdn.com/images/greendev/post/d95c34e8-361f-4938-bae4-c75692476582/image.png" /></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/88376160-8e66-492a-9307-931831a22b32/image.png" /></p>
<h3 id="issue-formyml">issue-form.yml</h3>
<pre><code class="language-yaml">name: 'Team lucky-vicky 이슈 생성'
description: 'lucky-vicky 백엔드 Repo에 이슈를 생성하며, 생성된 이슈는 Jira와 연동됩니다.'
labels: [order]
title: '이슈 이름을 작성해주세요.'
body:
  - type: input
    id: parentKey
    attributes:
      label: '상위 작업 Ticket Number'
      description: '상위 작업의 Ticket Number를 기입해주세요.'
      placeholder: 'LUCKY-00'
    validations:
      required: true

  - type: input
    id: branchName
    attributes:
      label: '브랜치 이름 (이슈 요약)'
      description: '영어 소문자로 이슈를 요약하여 브랜치 이름을 지어주세요. (ex: set-jira-issue)'
    validations:
      required: true

  - type: input
    id: branchPrefix
    attributes:
      label: '브랜치 전략(GitFlow)'
      description: 'feat/fix/docs/style/refactor/test/chore 중 해당 이슈와 걸맞게 작성해주세요.'
    validations:
      required: true

  - type: textarea
    id: details
    attributes:
      label: '상세 내용(Details)'
      description: '이슈 내용을 자세히 설명해주세요.'
      value: |
        - 상세 내용에 대해 작성해주세요.
    validations:
      required: true

  - type: textarea
    id: tasks
    attributes:
      label: '체크리스트(Tasks)'
      description: '해당 이슈에 대해 필요한 작업 목록을 작성해주세요.'
      value: |
        - [ ] Task1
        - [ ] Task2
    validations:
      required: true

  - type: textarea
    id: references
    attributes:
      label: '참조(References)'
      description: '해당 이슈와 관련된 레퍼런스를 참조해주세요.'
      value: | 
        - Reference1
    validations:
      required: false
</code></pre>
<h3 id="create-jira-issueyml">create-jira-issue.yml</h3>
<pre><code class="language-yaml">name: Create Jira issue
on:
  issues:
    types:
      - opened
jobs:
  create-issue:
    name: Create Jira issue
    runs-on: ubuntu-latest
    steps:
      - name: Login
        uses: atlassian/gajira-login@v3
        env:
          JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
          JIRA_USER_EMAIL: ${{ secrets.JIRA_USER_EMAIL }}

      - name: Checkout main code
        uses: actions/checkout@v4
        with:
          ref: main

      - name: Issue Parser
        uses: stefanbuck/github-issue-praser@v3
        id: issue-parser
        with:
          template-path: .github/ISSUE_TEMPLATE/issue_form.yml

      - name: Log Issue Parser
        run: |
          echo '${{ steps.issue-parser.outputs.jsonString }}'

      - name: Convert markdown to Jira Syntax
        uses: peter-evans/jira2md@v1
        id: md2jira
        with:
          input-text: |
            ### Github Issue Link
            - ${{ github.event.issue.html_url }}

            ${{ github.event.issue.body }}
          mode: md2jira

      - name: Create Issue
        id: create
        uses: atlassian/gajira-create@v3
        with:
          project: DIAR
          issuetype: Subtask
          summary: &quot;${{ github.event.issue.title }}&quot;
          description: &quot;${{ steps.md2jira.outputs.output-text }}&quot;
          fields: |
            {
              &quot;parent&quot;: {
                &quot;key&quot;: &quot;${{ steps.issue-parser.outputs.issueparser_parentKey }}&quot;
              }
            }

      - name: Log created issue
        run: echo &quot;Jira Issue ${{ steps.issue-parser.outputs.parentKey }}/${{ steps.create.outputs.issue }} was created&quot;

      - name: Checkout develop code
        uses: actions/checkout@v4
        with:
          ref: develop

      - name: Create branch with Ticket number
        run: |
          BRANCH_NAME=&quot;${{ steps.issue-parser.outputs.issueparser_branchPrefix }}/#${{ steps.issue-parser.outputs.issueparser_parentKey }}-${{ steps.issue-parser.outputs.issueparser_branchName }}&quot;
          git checkout -b &quot;$BRANCH_NAME&quot;
          git push origin &quot;$BRANCH_NAME&quot;

      - name: Update issue title
        uses: actions-cool/issues-helper@v3
        with:
          actions: &quot;update-issue&quot;
          token: ${{ secrets.GITHUB_TOKEN }}
          title: &quot;${{ steps.create.outputs.issue }} ${{ github.event.issue.title }}&quot;</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/a67a630b-000c-48b8-ad03-33c2efa9c7d8/image.png" /></p>
<ul>
<li>value에는 해당하는 키값을 넣어주었다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/481a7251-2175-4922-9f8a-63e9f372b0cc/image.png" /></li>
</ul>