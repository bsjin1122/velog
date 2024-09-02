<h1 id="설정-순서">설정 순서</h1>
<h2 id="1-파일-생성">1. 파일 생성</h2>
<ol>
<li>프로젝트에 .github 폴더 생성 후</li>
<li>하위에 폴더 <code>workflows</code>, <code>ISSUE_TEMPLATE</code> 생성</li>
<li><code>ISSUE_TEMPLATE</code>에는 issue_form.yml 파일을, <pre><code>  `workflows`에는 create-jira-issue.yml 파일을 생성하고 각각 알맞게 설정을 작업해준다.</code></pre></li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/9fa999ed-c1ff-4f39-9c42-7ce199344310/image.png" /></p>
<ul>
<li><p>issue_form.yml</p>
<pre><code class="language-yml">name: 'All-clear 이슈 생성'
description: 'TastyTrack Repo에 이슈를 생성하며, 생성된 이슈는 Jira와 연동됩니다.'
labels: [ order ]
title: '이슈 이름을 작성해주세요.'
body:
- type: input
  id: parentKey
  attributes:
    label: '상위 작업 Ticket Number'
    description: '상위 작업의 Ticket Number를 기입해주세요.'
    placeholder: 'TT-00'
  validations:
    required: true

- type: input
  id: branchName
  attributes:
    label: '브랜치 이름 (이슈 요약)'
    description: '영문 소문자로 브랜치 이름을 지어주세요. (ex: [스토리번호]-[도메인명]-[기능])'
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
</code></pre>
</li>
</ul>
<pre><code>- create-jira-issue.yml
```yml
name: Create Jira issue
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
          JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}👈
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}👈
          JIRA_USER_EMAIL: ${{ secrets.JIRA_USER_EMAIL }}👈

      - name: Checkout main code
        uses: actions/checkout@v4
        with:
          ref: dev

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
          project: TT
          issuetype: Sub-task
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
          ref: dev

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
          title: &quot;${{ steps.create.outputs.issue }} ${{ github.event.issue.title }}&quot;

</code></pre><ul>
<li>이부분은 github secrets 에 등록해야 한다.<blockquote>
<p>JIRA_BASE_URL: ${{ secrets.JIRA_BASE_URL }}👈</p>
<pre><code>    JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}👈
    JIRA_USER_EMAIL: ${{ secrets.JIRA_USER_EMAIL }}👈</code></pre></blockquote>
</li>
<li>PULL_REQUEST_TEMPLATE.md
```markdown<h2 id="📌-작업-내용-필수">📌 작업 내용 (필수)</h2>
</li>
<li>(기능에서 어떤 부분이 구현되었는지 설명해주세요.)</li>
<li>ex. <code>로그인 시, 구글 소셜 로그인 기능을 추가했습니다.</code></li>
</ul>
<br />

<h2 id="🌱-반영-브랜치">🌱 반영 브랜치</h2>
<ul>
<li>(반영 브랜치를 표시합니다. ex. <code>feat/login -&gt; dev</code> ) </li>
<li>(이슈를 완료했다면 닫을 이슈의 번호를 표기합니다. ex. <code>close #1</code> )</li>
<li>close #</li>
</ul>
<br />

<h2 id="🔥-트러블-슈팅-선택">🔥 트러블 슈팅 (선택)</h2>
<ul>
<li>(어려운 점이 있었다면 무엇이고 어떻게 해결했는지 작성해주세요.)</li>
</ul>
<p>```</p>
<h2 id="2-github-secrets-등록하기">2. github secrets 등록하기</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/f93669ae-5b7e-4a55-89d0-55b3c7df0563/image.png" /></p>
<ol>
<li>settings</li>
</ol>
<ul>
<li>settings에서 <code>JIRA_BASE_URL</code>, <code>JIRA_API_TOKEN</code>,<code>JIRA_USER_EMAIL</code>을 등록해준다. (Edit 연필아이콘 클릭!)</li>
</ul>
<blockquote>
<ul>
<li>JIRA_BASE_URL: <code>https://{작성한 도메인명}.atlassian.net</code></li>
<li>JIRA_API_TOKEN: <code>밑에 사이트에서 발급받은 토큰</code><ul>
<li><a href="https://id.atlassian.com/manage-profile/security/api-tokens">JIRA API Token발급하기</a></li>
</ul>
</li>
<li>JIRA_USER_EMAIL: <code>(토큰 발급받은 계정) JIRA에 로그인한 이메일주소</code></li>
</ul>
</blockquote>
<ol start="2">
<li>만약의 Organization에서 만든 Repository라면.. </li>
</ol>
<ul>
<li>organizations의 settings에 들어가서, 
<code>Actions/General - Workflow permissions</code></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/3294ab1e-254d-4a07-83f7-44ea2a48ce74/image.png" /></p>
<ul>
<li>Read and write permissions 로 체크 - Save </li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/27e13b34-ddfe-4211-b295-c8f813dd582d/image.png" /></p>
<h2 id="3-jira-설정해주기">3. JIRA 설정해주기</h2>
<ol>
<li>설정 - 세부사항
<img alt="" src="https://velog.velcdn.com/images/greendev/post/6fb0445c-4277-4eb0-a360-2cd47baecb9f/image.png" /></li>
</ol>
<ul>
<li>조금 전에 create-jira-issue.yml 에서 project 키를 TT라고 해주었으므로, jira에서도 같은 키로 맞춰준다. 
<img alt="" src="https://velog.velcdn.com/images/greendev/post/c37e95ae-163b-46cf-a55e-cc5ac09295c8/image.png" />
(jira에서 키를 먼저 설정하고, yml에 설정값을 맞춰준다고 생각하면 좋을 것 같다.)</li>
</ul>
<ol start="2">
<li>설정 - 이슈 유형
<img alt="" src="https://velog.velcdn.com/images/greendev/post/79ed2b4f-a2b4-44b2-b31d-c3a8b04ac9aa/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/75f770d6-0032-436c-999a-53d6d54d0ebf/image.png" /></li>
</ol>
<p>나는 이슈 단위를 <code>에픽 &gt; 스토리 &gt; Task &gt; Sub-task</code> 순으로 하게 되었다. 그래서 issue type을 Sub-task에서 브랜치들을 자동으로 생성하는 쪽으로 설정했기에 왼쪽처럼 유형을 맞춰준다.
<img alt="" src="https://velog.velcdn.com/images/greendev/post/a1ce14c9-7ad1-4bde-832c-4fff4431264f/image.png" /></p>
<ul>
<li>우리가 해야할 일(스토리;초록색 아이콘)에 수동으로 작성하여 추가해준 뒤 github issue 등록을 한다. 
30초 뒤 Sub-task(우측)에 브랜치가 자동으로 생성되는 것을 볼 수 있을 것이다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/b384406e-e27e-474b-8153-d4feab60a1cc/image.png" />
<img alt="" src="https://velog.velcdn.com/images/greendev/post/87db1b20-66ec-459b-803f-96b0b566743b/image.png" /></p>
<p>화이팅!!~~</p>