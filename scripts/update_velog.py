import feedparser
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
current_date = datetime.now().strftime("%y%m%d")
current_day = ["월", "화", "수", "목", "금", "토", "일"][datetime.now().weekday()]
date_prefix = f"{current_date}{current_day}"

# D-Day 계산 (2024년 9월 9일 기준)
base_date = datetime(2024, 9, 9)
dday_diff = (datetime.now() - base_date).days
dday_prefix = f"D+{dday_diff}" if dday_diff >= 0 else f"D{dday_diff}"

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    file_name = entry.title.replace('/', '-').replace('\\', '-').replace(':', '-')
    
    # 게시글 내용 확인
    post_content = entry.description.strip() if entry.description else None
    if not post_content:
        # print(f"Skipping post '{entry.title}' as it has no content.")
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
    commit_message = f"[{dday_prefix} | {date_prefix}] {entry.title}"
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
        print(f"origin/main과 변경된 사항이 있습니다. '{branch_name}'에 push를 진행합니다.")
        repo.git.fetch('origin')
        repo.git.checkout(branch_name)
        repo.git.pull('origin', branch_name, '--rebase')
        repo.git.push('origin', branch_name)
    else:
        print("origin/main과 변경사항이 없으므로 push하지 않습니다.")
else:
    print("Push할 변경사항이 없습니다.")

# 추후 .yml파일에서 환경변수로 사용할 예정 (예시 코드)
# with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
#     f.write(f"commit_message={commit_message}\n")
#     f.write(f"branch_name={branch_name}\n")
#     f.write(f"file_name={file_name}\n")
