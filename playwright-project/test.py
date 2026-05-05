import json

articles = []

articles.append({
    "title": "Sample News 1",
    "image_url": "img1.jpg",
    "author": "Author 1"
})

articles.append({
    "title": "Sample News 2",
    "image_url": "img2.jpg",
    "author": None
})

data = {
    "entertainment_news": articles,
    "cartoon_of_the_day": {
        "title": "Funny Cartoon",
        "image_url": "cartoon.jpg",
        "author": "Cartoonist"
    }
}

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON file created!")