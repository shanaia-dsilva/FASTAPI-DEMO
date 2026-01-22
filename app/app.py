from fastapi import FastAPI, HTTPException

app=FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "This is a cool test post."},
    2: {"title": "Python Tip", "content": "Remember to use list comprehensions for cleaner code."},
    3: {"title": "Daily Motivation", "content": "Keep pushing forward, no matter the challenges."},
    4: {"title": "Tech News", "content": "AI is transforming the way we code and work."},
    5: {"title": "Quick Recipe", "content": "Try making avocado toast for a healthy snack."},
    6: {"title": "Book Recommendation", "content": "Read 'Atomic Habits' for better daily routines."},
    7: {"title": "Fitness Tip", "content": "Stretch every morning to keep your body flexible."},
    8: {"title": "Travel Idea", "content": "Plan a weekend getaway to a nearby town."},
    9: {"title": "Coding Challenge", "content": "Solve a small algorithm problem every day to improve skills."},
    10: {"title": "Random Thought", "content": "Sometimes the simplest ideas can spark the biggest changes."}
}

@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException (status_code=404, detail="Post not found")
    return text_posts.get(id)


