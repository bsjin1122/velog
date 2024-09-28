import feedparser
import git
import os
from datetime import datetime

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@greendev'

# 깃허브 레포지토리 경로
repo_path = '.'  # 실제 Git 저장소 경로

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 현재 파일 목록 가져오기
existing_files = set(os.listdir(posts_dir))

# 새로 추가될 파일 목록
current_files = set()

# 현재 날짜와 요일 가져오기
current_date = datetime.now().strftime("%y%m%d")
current_day = ["월", "화", "수", "목", "금", "토", "일"][datetime.now().weekday()]
date_prefix = f"{current_date}{current_day}"

# D-Day 계산 (2024년 9월 9일 기준)
base_date = datetime(2024, 9, 9)
current_datetime = datetime.now()
dday_diff = (current_datetime - base_date).days

# D-Day 표시 형식 설정
if dday_diff >= 0:
    dday_prefix = f"D+{dday_diff}"
else:
    dday_prefix = f"D{dday_diff}"


# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title.replace('/', '-').replace('\\', '-')
    current_files.add(file_name + '.md')  # 현재 파일 목록에 추가
    print(file_name)

    # 게시글 내용 확인
    post_content = entry.description.strip() if entry.description else None
    
    # 게시글 내용이 없을 경우 예외 처리
    if not post_content:
        print(f"Skipping post '{entry.title}' as it has no content.")
        continue
    
    # Oracle 관련 글인 경우 ORACLE 폴더에 저장
    if file_name.startswith('[Oracle]'):
        oracle_dir = os.path.join(posts_dir, 'ORACLE')
        if not os.path.exists(oracle_dir):
            os.makedirs(oracle_dir)
        file_path = os.path.join(oracle_dir, file_name + '.md')
        
        # Oracle 관련 글이 이미 존재하면 추가 작업을 건너뛰기
        if os.path.exists(file_path):
            # print(f"Skipping existing Oracle post: {file_name}")
            continue
    else:
        file_path = os.path.join(posts_dir, file_name + '.md')

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)  # 글 내용을 파일에 작성

        # 깃허브 커밋
        commit_message = f"[{dday_prefix} | {date_prefix}] {entry.title}"
        repo.git.add(file_path)
        repo.git.commit('--allow-empty', '-m', commit_message)

# 변경 사항을 깃허브에 푸시
# remote_url = f"https://{os.environ['GITHUB_TOKEN']}@github.com/bsjin1122/velog.git"
# repo.git.push(remote_url, f'HEAD:{name_of_remote_branch}')
repo.git.checkout('-b', 'update-blog-posts-branch')
repo.git.push('origin', 'update-blog-posts-branch')
