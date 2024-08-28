import feedparser
import git
import os

# ���α� RSS �ǵ� URL
# example : rss_url = 'https://api.velog.io/rss/@soozi'
rss_url = 'https://api.velog.io/rss/@greendev'

# ����� �������丮 ���
repo_path = '.'

# 'velog-posts' ���� ���
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' ������ ���ٸ� ����
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# �������丮 �ε�
repo = git.Repo(repo_path)

# RSS �ǵ� �Ľ�
feed = feedparser.parse(rss_url)

# �� ���� ���Ϸ� �����ϰ� Ŀ��
for entry in feed.entries:
    # ���� �̸����� ��ȿ���� ���� ���� ���� �Ǵ� ��ü
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # �����ø� ��÷� ��ü
    file_name = file_name.replace('\\', '-')  # �齽���ø� ��÷� ��ü
    # �ʿ信 ���� �߰� ���� ��ü
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)

    # ������ �̹� �������� ������ ����
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)  # �� ������ ���Ͽ� �ۼ�

        # ����� Ŀ��
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# ���� ������ ����꿡 Ǫ��
repo.git.push()