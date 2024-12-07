from sqlalchemy.orm import Session
from models import Post

def add_several_posts(db:Session):
    db.add(Post(title="First", content="Some content", user_id="1"))

    db.add(Post(title="Second", content="Another content", user_id="1"))
    db.add(Post(title="Third", content="And more content", user_id="2"))

    db.commit()

def get_all_posts(db:Session):
    return db.query(Post).all()

def get_posts_by_user_id(user_id, db:Session):
    return db.query(Post).filter(Post.user_id == user_id).all()

def add_post(title, content, user_id, db:Session):
    db.add(Post(title=title, content=content, user_id=user_id))
    db.commit()

def update_content(post_id, content, db:Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    post.content = content
    db.commit()

def delete_post(post_id, db:Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    db.delete(post)
    db.commit()