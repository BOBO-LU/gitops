from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.database import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.ADMIN_EMAIL)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.ADMIN_EMAIL,
            name=settings.ADMIN_NAME,
            password=settings.ADMIN_PASSWORD,
            is_admin=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
