def blogEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "title":item["title"],
        "content":item["content"],
        "author":item["author"],
        "upvote":int(item["upvote"]),
        "downvote":int(item["downvote"])
    }

def blogsEntity(entity) -> list:
    return [blogEntity(item) for item in entity]

def blogEntityResume(item) -> dict:
    return {
        "id":str(item["_id"]),
        "title":item["title"],
        "content":item["content"][0:101],
        "author":item["author"],
        "upvote":int(item["upvote"]),
        "downvote":int(item["downvote"])
    }

def blogsEntityResume(entity) -> list:
    return [blogEntityResume(item) for item in entity]