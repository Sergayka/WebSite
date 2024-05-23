from functools import wraps

from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from flask_session import Session
from sqlalchemy.orm import polymorphic_union

from hashing_password import hash_password, check_password
from DB.init_db import SessionLocal, User, Category, Shorts, TShirt, Shirt, Pants, Jacket, Shoes, Accessories, Cart, \
    CartItem, Wishlist, WishlistItem, Item

from datetime import timedelta




app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Установка времени жизни сеанса в 20 минут
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_TYPE'] = 'filesystem'

# Настройка сессии Flask
Session(app)
# session.init_app(app)
# Функция для создания пользователя
def create_user(db, username, email, password_hash):
    user = User(username=username, email=email, password_hash=password_hash)

    db.add(user)
    db.commit()
    db.refresh(user)

    # Создание пустой корзины для пользователя
    cart = Cart(user_id=user.id)
    db.add(cart)

    # Создание пустого списка желаемого для пользователя
    wishlist = Wishlist(user_id=user.id)
    db.add(wishlist)

    db.commit()
    return user


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function

# Главная страница
@app.route('/')
def index():
    # Проверка, залогинен ли пользователь
    logged_in = 'user_id'  # Или любая другая логика, которая определяет, залогинен ли пользователь
    with SessionLocal() as session:
        categories = session.query(Category).all()

    return render_template('index.html', categories=categories, logged_in=logged_in)


@app.route('/category/<int:category_id>')
def show_category_items(category_id):
    with SessionLocal() as session:
        category = session.query(Category).filter_by(id=category_id).first()
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        # Здесь мы создаем объединение всех таблиц, чтобы запросить все элементы
        items = session.query(polymorphic_union(
            {
                'shorts': Shorts.__table__,
                'tshirt': TShirt.__table__,
                'shirt': Shirt.__table__,
                'pants': Pants.__table__,
                'jacket': Jacket.__table__,
                'shoes': Shoes.__table__,
                'accessories': Accessories.__table__,
            },
            None, 'type'
        )).filter_by(category_id=category_id).all()
    return render_template('category.html', category=category, items=items)


# Добавить товар в корзину
@app.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    item_id = request.form.get('item_id')
    category_id = request.form.get('category_id')
    user_id = session['user_id']

    with SessionLocal() as db_session:
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()

        if not item_id or not category_id:
            flash('Item ID or category ID is missing.', 'error')
            return redirect(url_for('show_category_items', category_id=category_id))

        category_table_mapping = {
            '1': Shorts,
            '2': TShirt,
            '3': Shirt,
            '4': Pants,
            '5': Jacket,
            '6': Shoes,
            '7': Accessories
        }

        item_class = category_table_mapping.get(category_id)
        if not item_class:
            flash('Invalid category ID.', 'error')
            return redirect(url_for('show_category_items', category_id=category_id))

        item = db_session.query(item_class).filter_by(id=item_id, category_id=category_id).first()

        if not item:
            flash('Item not found.', 'error')
            return redirect(url_for('show_category_items', category_id=category_id))

        # Проверяем, есть ли уже этот товар в корзине
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, category_id=category_id, item_id=item.id).first()
        if cart_item:
            # Если товар уже есть, увеличиваем количество
            cart_item.quantity += 1
        else:
            # Если товара нет, добавляем новый элемент в корзину
            cart_item = CartItem(cart_id=cart.id, category_id=int(category_id), item_id=item.id, quantity=1)
            db_session.add(cart_item)

        db_session.commit()

    flash('Item added to cart successfully.', 'success')
    return redirect(url_for('show_category_items', category_id=category_id))


@app.route('/add_to_wishlist', methods=['POST'])
@login_required
def add_to_wishlist():
    item_id = request.form.get('item_id')
    category_id = request.form.get('category_id')
    user_id = session['user_id']

    with SessionLocal() as db_session:
        wishlist = db_session.query(Wishlist).filter_by(user_id=user_id).first()

        if not item_id or not category_id:
            flash('Item ID or category ID is missing.', 'error')
            return redirect(url_for('show_category_items', category_id=category_id))

        category_table_mapping = {
            '1': Shorts,
            '2': TShirt,
            '3': Shirt,
            '4': Pants,
            '5': Jacket,
            '6': Shoes,
            '7': Accessories
        }

        item_class = category_table_mapping.get(category_id)
        if not item_class:
            flash('Invalid category ID.', 'error')
            return redirect(url_for('show_category_items', category_id=category_id))

        item = db_session.query(item_class).filter_by(id=item_id, category_id=category_id).first()

        if not item:
            flash('Item not found.', 'error')
            return redirect(url_for('show_category_items', category_id=category_id))

        # Проверяем, есть ли уже этот товар в корзине
        wishlist_item = db_session.query(WishlistItem).filter_by(wishlist_id=wishlist.id, category_id=category_id,
                                                         item_id=item.id).first()
        if wishlist_item:
            flash('Subject already added', 'error')
            return redirect(url_for('show_category_items', category_id=category_id))
        else:
            # Если товара нет, добавляем новый элемент в корзину
            cart_item = WishlistItem(wishlist_id=wishlist.id, category_id=int(category_id), item_id=item.id)
            db_session.add(cart_item)

        db_session.commit()

    flash('Item added to wishlist successfully.', 'success')
    return redirect(url_for('show_category_items', category_id=category_id))



@app.route('/cart')
@login_required
def show_cart():
    user_id = session['user_id']
    with SessionLocal() as db_session:
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()
        if not cart:
            flash('Cart not found.', 'error')
            return redirect(url_for('index'))

        cart_items = db_session.query(CartItem).filter_by(cart_id=cart.id).all()
        items = []
        for cart_item in cart_items:
            item_class = {
                1: Shorts,
                2: TShirt,
                3: Shirt,
                4: Pants,
                5: Jacket,
                6: Shoes,
                7: Accessories
            }[cart_item.category_id]
            item = db_session.query(item_class).filter_by(id=cart_item.item_id).first()
            items.append({
                'item': item,
                'quantity': cart_item.quantity,
                'category_id': cart_item.category_id
            })

    return render_template('cart.html', items=items)


@app.route('/cart/increase', methods=['POST'])
@login_required
def increase_cart_item():
    item_id = request.form.get('item_id')
    category_id = request.form.get('category_id')
    user_id = session['user_id']

    with SessionLocal() as db_session:
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, item_id=item_id, category_id=category_id).first()
        if cart_item:
            cart_item.quantity += 1
            db_session.commit()
            item_class = {
                1: Shorts,
                2: TShirt,
                3: Shirt,
                4: Pants,
                5: Jacket,
                6: Shoes,
                7: Accessories
            }[cart_item.category_id]
            item = db_session.query(item_class).filter_by(id=cart_item.item_id).first()
            return jsonify({
                'item_id': cart_item.item_id,
                'category_id': cart_item.category_id,
                'quantity': cart_item.quantity,
                'name': item.name,
                'description': item.description,
                'price': item.price,
                'photo_url': item.photo_url
            })
    return jsonify({'error': 'Item not found'}), 404



@app.route('/cart/decrease', methods=['POST'])
@login_required
def decrease_cart_item():
    item_id = request.form.get('item_id')
    category_id = request.form.get('category_id')
    user_id = session['user_id']

    with SessionLocal() as db_session:
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, item_id=item_id, category_id=category_id).first()
        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                db_session.commit()
                item_class = {
                    1: Shorts,
                    2: TShirt,
                    3: Shirt,
                    4: Pants,
                    5: Jacket,
                    6: Shoes,
                    7: Accessories
                }[cart_item.category_id]
                item = db_session.query(item_class).filter_by(id=cart_item.item_id).first()
                return jsonify({
                    'item_id': cart_item.item_id,
                    'category_id': cart_item.category_id,
                    'quantity': cart_item.quantity,
                    'name': item.name,
                    'description': item.description,
                    'price': item.price,
                    'photo_url': item.photo_url
                })
            else:
                db_session.delete(cart_item)
                db_session.commit()
                return jsonify({'item_id': item_id, 'category_id': category_id, 'quantity': 0})
    return jsonify({'error': 'Item not found'}), 404



@app.route('/cart/remove', methods=['POST'])
@login_required
def remove_cart_item():
    item_id = request.form.get('item_id')
    category_id = request.form.get('category_id')
    user_id = session['user_id']

    with SessionLocal() as db_session:
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, item_id=item_id, category_id=category_id).first()
        if cart_item:
            db_session.delete(cart_item)
            db_session.commit()
            return jsonify({'item_id': item_id, 'category_id': category_id})

    return jsonify({'error': 'Item not found'}), 404


@app.route('/wishlist')
@login_required
def show_wishlist():
    user_id = session['user_id']
    with SessionLocal() as db_session:
        wishlist = db_session.query(Wishlist).filter_by(user_id=user_id).first()
        wishlist_items = []

        if wishlist:
            wishlist_items = db_session.query(WishlistItem).filter_by(wishlist_id=wishlist.id).all()

        items = []
        for wishlist_item in wishlist_items:
            category_table_mapping = {
                1: Shorts,
                2: TShirt,
                3: Shirt,
                4: Pants,
                5: Jacket,
                6: Shoes,
                7: Accessories
            }
            item_class = category_table_mapping.get(wishlist_item.category_id)
            if item_class:
                item = db_session.query(item_class).filter_by(id=wishlist_item.item_id).first()
                items.append(item)


    return render_template('wishlist.html', wishlist_items=items)



@app.route('/add_from_wishlist', methods=['POST'])
@login_required
def add_from_wishlist():
    item_id = request.form.get('item_id')
    category_id = request.form.get('category_id')
    user_id = session['user_id']

    with SessionLocal() as db_session:
        cart = db_session.query(Cart).filter_by(user_id=user_id).first()

        if not item_id or not category_id:
            flash('Item ID or category ID is missing.', 'error')
            return redirect(url_for('show_wishlist'))

        wishlist = db_session.query(Wishlist).filter_by(user_id=user_id).first()
        if not wishlist:
            flash('Wishlist not found.', 'error')
            return redirect(url_for('show_wishlist'))

        wishlist_item = db_session.query(WishlistItem).filter_by(wishlist_id=wishlist.id, category_id=category_id, item_id=item_id).first()
        if not wishlist_item:
            flash('Item not found in wishlist.', 'error')
            return redirect(url_for('show_wishlist'))

        # Проверяем, есть ли уже этот товар в корзине
        cart_item = db_session.query(CartItem).filter_by(cart_id=cart.id, category_id=category_id, item_id=item_id).first()
        if cart_item:
            # Если товар уже есть, увеличиваем количество
            cart_item.quantity += 1
        else:
            # Если товара нет, добавляем новый элемент в корзину
            cart_item = CartItem(cart_id=cart.id, category_id=int(category_id), item_id=item_id, quantity=1)
            db_session.add(cart_item)

        # Удаляем товар из списка желаемого
        db_session.delete(wishlist_item)
        db_session.commit()

    flash('Item added to cart from wishlist successfully.', 'success')
    return redirect(url_for('show_wishlist'))


@app.route('/remove_from_wishlist', methods=['POST'])
@login_required
def remove_from_wishlist():
    item_id = request.form.get('item_id')
    category_id = request.form.get('category_id')
    user_id = session['user_id']

    with SessionLocal() as db_session:
        wishlist = db_session.query(Wishlist).filter_by(user_id=user_id).first()

        if wishlist:
            wishlist_item = db_session.query(WishlistItem).filter_by(wishlist_id=wishlist.id, category_id=category_id,
                                                                     item_id=item_id).first()
            if wishlist_item:
                db_session.delete(wishlist_item)
                db_session.commit()

    return redirect(url_for('show_wishlist'))


# Регистрация пользователя
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'Missing username, email, or password'}), 400

        db = SessionLocal()
        user = db.query(User).filter_by(username=username).first()
        if user:
            flash('Username already exists', 'error')
            db.close()
            return redirect(url_for('register'))

        user = db.query(User).filter_by(email=email).first()
        if user:
            flash('Email already registered', 'error')
            db.close()
            return redirect(url_for('register'))

        hashed_password = hash_password(password)

        new_user = create_user(db, username, email, hashed_password)

        db.close()

        flash('User registered successfully', 'success')
        return redirect(url_for('index'))

    return render_template('register.html')


# Аутентификация пользователя
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            flash('Missing email or password', 'error')
            return render_template('login.html')

        db = SessionLocal()
        user = db.query(User).filter_by(email=email).first()

        if not user:
            flash('User not found', 'error')
            return render_template('login.html')

        # Проверка пароля
        if not check_password(user.password_hash, password):
            flash('Invalid password', 'error')
            return render_template('login.html')

        # Сохранение идентификатора пользователя в сессии Flask
        session['user_id'] = user.id
        session.permanent = True  # Устанавливаем сессию на постоянную (длительность сеанса 20 минут)

        db.close()
        return redirect(url_for('index'))  # Перенаправляем пользователя на главную страницу

    return render_template('login.html')


# Выход пользователя
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Удаляем идентификатор пользователя из сессии
    return redirect(url_for('index'))  # Перенаправляем пользователя на главную страницу


@app.route('/add_item', methods=['POST'])
@login_required
def add_item():
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    photo_url = request.form.get('photo_url')
    extra_info = request.form.get('extra_info')
    category_id = request.form.get('category_id')

    if not all([name, description, price, photo_url, category_id]):
        flash('All fields except extra info are required.', 'error')
        return redirect(url_for('profile'))

    with SessionLocal() as db_session:
        category = db_session.query(Category).filter_by(id=category_id).first()
        if not category:
            flash('Invalid category selected.', 'error')
            return redirect(url_for('profile'))

        item = Item(
            name=name,
            description=description,
            price=float(price),
            photo_url=photo_url,
            category_id=int(category_id),
        )
        db_session.add(item)
        db_session.commit()
        db_session.refresh(item)

        # Определение таблицы категории и добавление элемента в нее
        category_table_mapping = {
            '1': Shorts,
            '2': TShirt,
            '3': Shirt,
            '4': Pants,
            '5': Jacket,
            '6': Shoes,
            '7': Accessories
        }

        item_class = category_table_mapping.get(category_id)
        if not item_class:
            flash('Invalid category selected.', 'error')
            return redirect(url_for('profile'))

        category_item = item_class(
            id=item.id,  # Использование ID, созданного в общей таблице Item
            name=name,
            description=description,
            price=price,
            photo_url=photo_url,
            category_id=category_id
        )
        db_session.add(category_item)
        db_session.commit()

        flash('Item added successfully.', 'success')
    return redirect(url_for('profile'))

@app.route('/category/all_items')
def show_all_items():
    with SessionLocal() as session:
        categories = session.query(Category).all()
        all_items = []
        for category in categories:
            items = session.query(polymorphic_union(
                {
                    'shorts': Shorts.__table__,
                    'tshirt': TShirt.__table__,
                    'shirt': Shirt.__table__,
                    'pants': Pants.__table__,
                    'jacket': Jacket.__table__,
                    'shoes': Shoes.__table__,
                    'accessories': Accessories.__table__,
                },
                None, 'type'
            )).filter_by(category_id=category.id).all()
            all_items.extend(items)
    return render_template('all_items.html', categories=categories, items=all_items)

@app.route('/profile')
@login_required
def profile():
    with SessionLocal() as session:
        categories = session.query(Category).all()
    return render_template('profile.html', categories=categories)


if __name__ == "__main__":
    app.run(debug=True)
