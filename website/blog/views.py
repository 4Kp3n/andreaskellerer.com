import markdown
import yaml
from django.conf import settings
from django.shortcuts import render, Http404
from pathlib import Path
from slugify import slugify


def get_markdown_posts():
    posts = []
    for file in sorted(Path(settings.BLOG_POSTS_DIR).glob("*.md"), reverse=True):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        # Frontmatter parsen
        if content.startswith("---"):
            parts = content.split("---", 2)
            meta = yaml.safe_load(parts[1])
            body = parts[2].strip()
        else:
            meta = {}
            body = content.strip()

        slug = meta.get("slug") or slugify(file.stem)
        posts.append({
            "slug": slug,
            "title": meta.get("title", file.stem),
            "date": meta.get("date", ""),
            "summary": meta.get("summary", body[:200] + "..."),
            "content": markdown.markdown(body, extensions=["fenced_code", "tables"])
        })

    return posts


def blog_index(request):
    posts = get_markdown_posts()
    print(posts)
    return render(request, "blog.html", {"posts": posts})


def blog_detail(request, slug):
    posts = get_markdown_posts()
    post = next((p for p in posts if p["slug"] == slug), None)
    if not post:
        raise Http404("Blogeintrag nicht gefunden")
    return render(request, "blog_detail.html", {"post": post})
