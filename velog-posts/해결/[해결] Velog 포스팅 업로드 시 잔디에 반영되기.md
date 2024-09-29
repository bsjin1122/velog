<blockquote>
<p> 💥 scheduler를 적용해두었기 때문에, 잔디에 반영 여부는 추후에 다시 한 번 확인해봐야할 것 같다. </p>
</blockquote>
<img height="300" src="https://velog.velcdn.com/images/greendev/post/4998b59b-4638-4864-befe-ac68ef82c7ff/image.png" width="350" />

<h2 id="상황">상황</h2>
<blockquote>
<ul>
<li>왜 <code>velog에 자동으로 커밋하기</code>만 글이 잔뜩 있고, 
잔디로 반영되지 않는다는 건 왜 안 올라 오는거야..! <br /><del>(물론 나도 따라했었다)</del></li>
</ul>
</blockquote>
<ul>
<li><code>github-actions[bot]</code>이 github action으로 작업하는 경우, Contribution(잔디)에 반영이 안되는 것을 알게 되었다.. <ul>
<li><img alt="" src="https://velog.velcdn.com/images/greendev/post/0ed23725-301d-47fb-83ae-10f399dfca3d/image.png" /></li>
<li>어쩐지 commit은 trigger로 github action이 도는데, 잔디가 안심어지고 있었다.</li>
</ul>
</li>
</ul>
<h2 id="시도">시도</h2>
<ul>
<li><a href="https://velog.io/@think2wice/Github-%EB%B6%84%EB%AA%85-commit%EC%9D%84-%ED%96%88%EB%8A%94%EB%8D%B0-%EC%99%9C-contribution-%EA%B7%B8%EB%9E%98%ED%94%84%EB%8A%94-%EC%95%88%EC%B1%84%EC%9B%8C%EC%A7%80%EC%A7%80">Github Contributor의 기준(잔디가 심어지는 기준)</a></li>
<li><a href="https://www.hahwul.com/2020/10/18/how-to-trigger-github-action-manually/">[Github] 1. Contributions : 잔디밭에 대한 모든 것</a>
을 1-2일 찾아보면서, git config로도 시도해보고.. 머릿속으로 고민을 좀 했었다. </li>
</ul>
<img src="https://velog.velcdn.com/images/greendev/post/a034a3c7-5dd2-4b2b-b494-df8c0e584eb7/image.png" width="300" />


<ul>
<li>그러던 중, Pull request를 통하면, 잔디가 심어지지 않을까? 생각을 해보게 되었다.</li>
</ul>
<h2 id="해결">해결</h2>
<ul>
<li><p>Github Action marketpalce 의 </p>
<ul>
<li><a href="https://github.com/marketplace/actions/auto-pull-request">Auto Pull Request</a></li>
<li><a href="https://github.com/diillson/auto-pull-request">Github pull Request</a></li>
<li><a href="https://github.com/marketplace/actions/auto-approve">Auto Approve Github Action</a></li>
<li><a href="https://github.com/tgymnich/fork-sync?tab=readme-ov-file#auto-approve">Auto Approve Pull Reqeusts</a><ul>
<li><a href="https://github.com/tgymnich/fork-sync/issues/153">tgymnich/fork-sync@v1: 스스로 생성한 pr이 승인이 되지 않을 때(참고용..)</a></li>
</ul>
</li>
</ul>
</li>
<li><p>이 글을 전체 읽어보면서 하나하나씩 옵션값들을 대입해서 넣어보았다. 사실 나는 github action이 2번째 사용하는거라 까막눈이라 삽질을 너무 많이 했다..🥺</p>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/fa0b9432-18ed-4130-b451-6b246343f36b/image.png" /></p>
<h2 id="배운-것">배운 것</h2>
<h3 id="1-github의-작업단위">1. Github의 작업단위</h3>
<ul>
<li>Github의 작업 단위는 <code>Workflow, job, steps</code>로 구성되어 있다는 것</li>
</ul>
<h3 id="2---allow-empty">2. --allow-empty</h3>
<ol start="2">
<li>git commit <code>--allow-empty</code> 변경된 것이 없어도, 빈 껍데기 커밋을 올릴 수 있다. </li>
</ol>
<h3 id="3---set-upstream">3. --set-upstream</h3>
<ol start="3">
<li>로컬 브랜치를 원격 브랜치와 연결하기(--set-upstream)<ul>
<li><code>git branch --set-upstream-to=origin/&lt;remote-branch&gt; &lt;local-branch&gt;</code></li>
</ul>
</li>
</ol>
<h3 id="4-steps-간에-outputs값-참조하기">4. steps 간에 outputs값 참조하기</h3>
<ol start="4">
<li>github action에서는, steps 단위 사이에서 outputs으로 값을 받을 수 있는 경우도 있으니, 참조할 수 있다! <ul>
<li>ex) 앞 step에서 <code>id: create_pr</code>로 지정해놓고, 다음 step에서</li>
<li>ex) <code>${{ steps.create_pr.outputs.pr_number }}</code></li>
</ul>
</li>
</ol>
<h3 id="5-contributes">5. Contributes</h3>
<ol start="5">
<li>github-actions[bot]은 잔디에 반영이 안된다. 안되면,
<code>${{ secrets.GITHUB_TOKEN }}</code>나, <code>PAT(Personal Access Token)</code>를 사용해보자. <br />

</li>
</ol>
<h3 id="6-github_env">6. $GITHUB_ENV</h3>
<ol start="6">
<li>날짜 형식을 커스터마이징하고 싶었다. ex) [240928]<ul>
<li>이때 shell명령어로 환경변수를 만들어주어, <code>$GITHUB_ENV</code>로 사용할 수 있었다!</li>
<li><code>run: echo &quot;PR_DATE=$(date '+%y%m%d')&quot; &gt;&gt; $GITHUB_ENV</code><h2 id="후기">후기</h2>
</li>
</ul>
</li>
</ol>
<ul>
<li><p>일주일동안 안돼서 github 블로그로도 시도해보고 난리를 부렸었다. <del><strong>이것도 해결할 .. 해야지..</strong></del></p>
</li>
<li><p>그래도 앉은 자리에서 물 마시기 외 6시간 앉아서 붙잡고 늘어졌더니 돼서 다행이다. 드디어 편하게 잠에 들 수 있겠다.</p>
</li>
</ul>
<hr />
<ul>
<li>잘못된 코드나 수정/개선 사항 있으면 알려주세요 :D<h2 id="작성한-코드">작성한 코드</h2>
<h3 id="update_blogyml">update_blog.yml</h3>
</li>
</ul>
<pre><code class="language-yaml">name: Update Blog Posts

on:
  push:
    branches:
      - update-blog-posts-branch
  schedule:
      - cron: '0 */8 * * *'
  workflow_dispatch: 
    inputs: 
      pullRequestNumber:
        description: Pull request number to auto-approve
        required: false

  pull_request:
    branches:
      - main

permissions:
  contents: write
  pull-requests: write


jobs:
  update_blog:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          pip install feedparser gitpython

      - name: Configure Git
        run: |
          git config --global user.name 'bsjin1122'
          git config --global user.email 'kitty7579@hanmail.net'

      - name: Run script
        run: python scripts/update_velog.py

      - name: Check for Changes # Git 상태 확인
        run: |
          git status
          git diff
        id: check_changes

        # Current branch is: refs/heads/update-blog-posts-branch
      - name: Display Current Branch
        run: |
          echo &quot;Current branch is: $GITHUB_REF&quot;

      - name: Set Date Format for PR Title
        run: echo &quot;PR_DATE=$(date '+%y%m%d')&quot; &gt;&gt; $GITHUB_ENV

      - name: Create Pull Request (peter-evans)
        uses: peter-evans/create-pull-request@v7
        with:
          token: ${{ secrets.VELOG_TOKEN }}
          author: bsjin1122 &lt;kitty7579@hanmail.net&gt;
          body: | 
            :satisfied: [Velog 새 게시글 확인하기](https://velog.io/@greendev/posts)
          labels: velog
          title: &quot;[${{ env.PR_DATE }}]  Velog 게시글 업로드&quot;
          branch: main
          base: update-blog-posts-branch
          assignees: bsjin1122
        id: create_pr

      - name: Display PR Number # 날짜 형식
        run: |
          echo &quot;Pull Request Number: ${{ steps.create_pr.outputs.pull-request-number }}&quot; 

      - name: PR Auto Merge 
        # PR이 있는 경우에만 실행  
        if: steps.create_pr.outputs.pull-request-number != ''  
        uses: peter-evans/enable-pull-request-automerge@v3
        with:
          token: ${{ secrets.VELOG_TOKEN }}
          pull-request-number: ${{ steps.create_pr.outputs.pull-request-number }}
          # merge-method:

      ########### 시도 했던 방법들 -- 사용 가능한 스크립트들입니다.

      # 방법1. PR 자동 승인
      # - name: PR auto approval
      #   uses: tgymnich/fork-sync@v2.0
      #   with:
      #     token: ${{ secrets.GITHUB_TOKEN }}
      #     owner: bsjin1122
      #     base: main
      #     head: update-blog-posts-branch
      #     pr_message: &quot;velog 작성 - PR approve 완료&quot;

      # 방법2. PR 자동 승인 -- 본인이 생성한 pr은 본인이 승인 못하게 막아둠
      # - name: PR 자동 승인
      #   uses: hmarr/auto-approve-action@v4
      #   with:
      #     github-token: ${{ secrets.GITHUB_TOKEN }}
      #     pull-request-number: ${{ steps.create_pr.outputs.pr_number }}
      #     review-message: &quot;Auto approved automated PR Test&quot;

      # 방법3. PR 자동 생성 
      # - name: Create Pull Request
      #   uses: peter-evans/create-pull-request@v3
      #   with:
      #     token: ${{ secrets.GITHUB_TOKEN }}
      #     commit-message: &quot;Velog posts 업데이트&quot;
      #     branch: update-blog-posts-branch  # PR 생성 시 사용될 브랜치 이름
      #     title: &quot;PR 자동 생성&quot;
      #     base: main

      # 변경사항이 있는 경우에만 실행
      # - name: Create Pull Request
      #   uses: diillson/auto-pull-request@v1.0.1
      #   with:
      #     destination_branch: &quot;main&quot;
      #     github_token: ${{ secrets.VELOG_TOKEN }}
      #     pr_label: &quot;velog&quot;
      #     pr_title: &quot;[${{ env.PR_DATE }}]  Velog 게시글 업로드&quot;
      #     pr_allow_empty: false
      #     pr_body: |
      #       :satisfied: [Velog 새 게시글 확인하기](https://velog.io/@greendev/posts)
      #   id: create_pr  


</code></pre>
<hr />
<h3 id="update_velogpy">update_velog.py</h3>
<pre><code class="language-python">import feedparser
import git
import os
import re
from datetime import datetime

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@greendev'

# 깃허브 레포지토리 경로
repo_path = '.'
# 'C:/study/velog' # 실제 Git 저장소 경로

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
os.makedirs(posts_dir, exist_ok=True)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 현재 날짜와 요일 가져오기
current_date = datetime.now().strftime(&quot;%y%m%d&quot;)
current_day = [&quot;월&quot;, &quot;화&quot;, &quot;수&quot;, &quot;목&quot;, &quot;금&quot;, &quot;토&quot;, &quot;일&quot;][datetime.now().weekday()]
date_prefix = f&quot;{current_date}{current_day}&quot;

# D-Day 계산 (2024년 9월 9일 기준)
base_date = datetime(2024, 9, 9)
dday_diff = (datetime.now() - base_date).days
dday_prefix = f&quot;D+{dday_diff}&quot; if dday_diff &gt;= 0 else f&quot;D{dday_diff}&quot;

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    file_name = entry.title.replace('/', '-').replace('\\', '-')

    # 게시글 내용 확인
    post_content = entry.description.strip() if entry.description else None
    if not post_content:
        # print(f&quot;Skipping post '{entry.title}' as it has no content.&quot;)
        continue

    # 파일 이름에서 주제(subject) 추출
    match = re.search(r'\[(.*?)\]', file_name)
    subject = match.group(1).upper() if match else None # 대문자 설정
    print(subject)

    # 디렉토리 설정: subject가 있는 경우 해당 디렉토리, 없는 경우 'velog-posts'
    if subject:
        subject_dir = os.path.join(posts_dir, subject)
        os.makedirs(subject_dir, exist_ok=True)  # 해당 subject 디렉토리 생성
    else:
        subject_dir = posts_dir

    # Oracle 관련 글인 경우 ORACLE 폴더로 변경
    if subject and subject.startswith('ORACLE'):
        subject_dir = os.path.join(posts_dir, 'ORACLE')
        os.makedirs(subject_dir, exist_ok=True)

    # 파일 경로 설정
    file_path = os.path.join(subject_dir, file_name + '.md')

    # 이미 파일이 존재하면 작업을 건너뛰기
    if os.path.exists(file_path):
        continue

    # 파일 생성 및 내용 작성
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(post_content)

    # 깃허브 커밋
    commit_message = f&quot;[{dday_prefix} | {date_prefix}] {entry.title}&quot;
    repo.git.add(file_path)
    repo.git.commit('-m', commit_message)

# 커밋 여부 확인 후 변경 사항을 푸시
if repo.is_dirty(untracked_files=True):
    branch_name = 'update-blog-posts-branch'

    # origin/main과 현재 로컬 브랜치의 차이 확인
    main_branch = 'origin/main'

    # 'origin/main'과 현재 상태의 diff 확인
    diff_main = repo.git.diff(main_branch)

    if diff_main:  # 변경 사항이 있을 경우에만 push
        print(f&quot;origin/main과 변경된 사항이 있습니다. '{branch_name}'에 push를 진행합니다.&quot;)
        repo.git.fetch('origin')
        repo.git.checkout(branch_name)
        repo.git.pull('origin', branch_name, '--rebase')
        repo.git.push('origin', branch_name)
    else:
        print(&quot;origin/main과 변경사항이 없으므로 push하지 않습니다.&quot;)
else:
    print(&quot;Push할 변경사항이 없습니다.&quot;)

# 추후 .yml파일에서 환경변수로 사용할 예정 (예시 코드)
# with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
#     f.write(f&quot;commit_message={commit_message}\n&quot;)
#     f.write(f&quot;branch_name={branch_name}\n&quot;)
#     f.write(f&quot;file_name={file_name}\n&quot;)
</code></pre>
<ul>
<li>참고로 python은 velog 포스팅 제목의 <code>[주제명]</code>에서 대괄호를 따로 추출해서(subject라는 변수로), 
디렉토리를 만들어서 글을 분류하는 로직을 추가로 넣었다.</li>
</ul>
<h2 id="이어서-velog-쓸-수-있겠다">이어서 velog 쓸 수 있겠다...</h2>
<p><img alt="" src="https://velog.velcdn.com/images/greendev/post/59c768de-313a-4585-96b3-0c1227c417f4/image.png" /></p>