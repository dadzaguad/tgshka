
from sqlalchemy import BigInteger, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession

import os


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
if (
    not POSTGRES_USER
    or not POSTGRES_PASSWORD
    or not POSTGRES_DB
    or not POSTGRES_HOST
    or not POSTGRES_PORT
):
    raise ValueError(
        "POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT must be set"
    )


DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(url=DATABASE_URL)


async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(120))
    price: Mapped[int] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey("categories.id"))


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def seed_data():
    async with async_session() as session:
        # Проверяем, существуют ли уже категории
        existing = await session.scalars(select(Category).limit(1))
        if existing.first():
            # Если уже есть данные, сразу выходим
            return

        # Задаем имена категорий
        category_names = ["Electronics", "Books", "Clothing", "Home"]
        categories = []
        for name in category_names:
            cat = Category(name=name)
            session.add(cat)
            categories.append(cat)

        # Commit для фиксации категорий и получения их id
        await session.commit()

        # Теперь для каждой категории создаем 4 товара
        for cat in categories:
            for i in range(1, 5):
                item = Item(
                    name=f"{cat.name} Item {i}",
                    description=f"Description for {cat.name} Item {i}",
                    price=100 * i,  # Пример цены
                    category=cat.id
                )
                session.add(item)
                await session.commit()
