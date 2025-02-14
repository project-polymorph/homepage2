import json

def load_repo_data():
    with open('independence_repo.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_markdown():
    repos = load_repo_data()
    
    # Split repositories by type
    general_repos = [repo for repo in repos if not repo['is_restricted']]
    restricted_repos = [repo for repo in repos if repo['is_restricted']]
    
    # Calculate statistics
    total_size = sum(repo['size'] for repo in repos)
    
    markdown = f"""---
hide:
  - navigation
  - toc
---    
# 多元性别中文数字图书馆

用技术保存历史，用文化点亮未来：一个致力于传承、传播跨性别与多元性别的知识与故事的中文平台。

<div class="grid cards" markdown>

-   :material-library:{{ .lg .middle }} __资料库__

    ---

    共 {len(repos)} 个专题资料库
    
-   :material-book-multiple:{{ .lg .middle }} __资料总量__

    ---

    {total_size:,} 份文档资料

-   :material-magnify:{{ .lg .middle }} __高效检索__

    ---

    使用强大的搜索系统快速找到所需内容

-   :material-robot:{{ .lg .middle }} __智能归档__

    ---

    通过 AI 自动收集、整理和归档

</div>

## 一般存档库

<div class="grid cards" markdown>

"""

    # Add general repositories
    for repo in general_repos:
        markdown += f"""
-   :material-folder-open:{{ .lg .middle }} __{repo['name']}__

    ---
    
    {repo['description']}
    
    [:octicons-arrow-right-24: 访问资料库]({repo['url']})
"""

    markdown += """
</div>

## 限制级存档库

!!! warning "内容警告"

    以下资料库包含成人内容，仅供成年人访问。

<div class="grid cards" markdown>
"""

    # Add restricted repositories
    for repo in restricted_repos:
        markdown += f"""
-   :material-folder-alert:{{ .lg .middle }} __{repo['name']}__

    ---
    
    {repo['description']}
    
    [:octicons-arrow-right-24: 访问资料库]({repo['url']})
"""

    markdown += """
</div>
"""

    # Write to file
    with open('docs/index.md', 'w', encoding='utf-8') as f:
        f.write(markdown)

if __name__ == '__main__':
    generate_markdown() 
