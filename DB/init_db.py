from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# from sqlalchemy.ext.declarative import declarative_base


# Подключение к базе данных PostgreSQL
DB_URL = "postgresql://postgres:123321@localhost:5432/politex"
engine = create_engine(DB_URL)

# Создание сессии для взаимодействия с базой данных
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Базовый класс для определения моделей SQLAlchemy
Base = declarative_base()


# Модель пользователя
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связь с корзиной
    carts = relationship("Cart", back_populates="user")

    # Связь со списком желаемого
    wishlists = relationship("Wishlist", back_populates="user")


# Модель категории
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    photo_url = Column(String)

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    photo_url = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category")

# Модель шортов
class Shorts(Base):
    __tablename__ = 'shorts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    photo_url = Column(String)
    size = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))


# Модель футболок
class TShirt(Base):
    __tablename__ = 'tshirts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    photo_url = Column(String)
    color = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))


# Модель рубашек
class Shirt(Base):
    __tablename__ = 'shirts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    photo_url = Column(String)
    material = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))


# Остальные модели аналогично:
class Pants(Base):
    __tablename__ = 'pants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    photo_url = Column(String)
    length = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))


class Jacket(Base):
    __tablename__ = 'jackets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    photo_url = Column(String)
    warmth_rating = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))


class Shoes(Base):
    __tablename__ = 'shoes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    photo_url = Column(String)
    size = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))


class Accessories(Base):
    __tablename__ = 'accessories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric)
    photo_url = Column(String)
    type = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))

# Модель корзины
class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="carts")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Добавляем атрибут items и связь с CartItem
    items = relationship("CartItem", back_populates="cart")


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    cart = relationship("Cart", back_populates="items")
    category_id = Column(Integer, ForeignKey('categories.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    quantity = Column(Integer, default=1)

    category = relationship("Category")
    item = relationship("Item")

# Модель списка желаемого
class Wishlist(Base):
    __tablename__ = "wishlists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="wishlists")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Добавляем атрибут items и связь с WishlistItem
    items = relationship("WishlistItem", back_populates="wishlist")


class WishlistItem(Base):
    __tablename__ = "wishlist_items"

    id = Column(Integer, primary_key=True, index=True)
    wishlist_id = Column(Integer, ForeignKey('wishlists.id'))
    wishlist = relationship("Wishlist", back_populates="items")
    category_id = Column(Integer, ForeignKey('categories.id'))
    item_id = Column(Integer, ForeignKey('items.id'))

    category = relationship("Category")
    item = relationship("Item")


# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)
