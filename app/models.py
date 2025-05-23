from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db

class User(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sa.String(64), unique=True, index=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String(120), unique=True, index=True)
    password_hash: orm.Mapped[Optional[str]] = orm.mapped_column(sa.String(128))
    posts: orm.WriteOnlyMapped['Post'] = orm.relationship(back_populates='author')

    def __repr__(self) -> str:
        return f'<User {self.username}>'

class Post(db.Model):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(sa.String(140))
    body: orm.Mapped[str] = orm.mapped_column(sa.Text())
    timestamp: orm.Mapped[datetime] = orm.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey('user.id'), index=True)

    author: orm.Mapped['User'] = orm.relationship(back_populates='posts')

    def __repr__(self) -> str:
        return f'<Post {self.title}>'