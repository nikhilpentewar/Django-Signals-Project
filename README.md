# Django-Signals-Project

# Django Signals and Custom Python Classes Assignment

## ✅ Part 1: Django Signals

This assignment explores how Django signals behave by default in terms of **synchronization**, **threading**, and **transaction management**.

---

### 🔹 Question 1: Are Django signals executed synchronously or asynchronously by default?

**Answer:**  
Django signals are **synchronous by default**.

**Evidence:**
- We added a `time.sleep(5)` delay in the signal handler.
- When `TestModel.objects.create(name="Testing")` is called in the Django shell, the shell blocks for 5 seconds.
- This proves the signal runs **before** returning control, which confirms synchronous behavior.

```python
# coreapp/signals.py
@receiver(post_save, sender=TestModel)
def signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)
    print("Signal ended")
```

---

### 🔹 Question 2: Do Django signals run in the same thread as the caller?

**Answer:**  
Yes, Django signals run in the **same thread** as the caller by default.

**Evidence:**
We printed the thread ID in both the main thread and inside the signal handler using `threading.get_ident()`:

```python
# Shell
>>> import threading
>>> print("Main thread:", threading.get_ident())
Main thread: 14792
>>> TestModel.objects.create(name="Testing")

# Signal Output
Signal started  
Same thread? 14792
```

---

### 🔹 Question 3: Do Django signals run in the same database transaction as the caller?

**Answer:**  
No, by default, Django signals do **not necessarily run inside the same transaction** as the caller.

**Evidence:**
We checked the value of `transaction.get_connection().in_atomic_block` inside the signal, and it returned `False`.

```python
# Signal Output
Inside transaction block? False
```

> This shows the signal handler was outside an active `atomic()` block, and hence, not guaranteed to rollback if the transaction fails.

---

## ✅ Part 2: Custom Classes in Python

### 🎯 Task:
Create a `Rectangle` class with the following features:
- Accepts `length` and `width` as integers during initialization.
- Is iterable.
- On iteration, yields:
  - `{'length': value}`
  - `{'width': value}`

### ✅ Implementation

```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
```

### ▶️ Output

```python
r = Rectangle(10, 5)
for item in r:
    print(item)
```

**Result:**
```
{'length': 10}
{'width': 5}
```

---

## ✅ Setup Instructions

1. Clone or download this repo.
2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Create `.env` with:
```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Test in Django shell:

```bash
python manage.py shell
>>> from coreapp.models import TestModel
>>> import threading
>>> print("Main thread:", threading.get_ident())
>>> TestModel.objects.create(name="Testing")
```

---

## 📦 Project Structure

```
signals_project/
├── coreapp/
│   ├── models.py
│   ├── signals.py
│   ├── rectangle_demo.py
│   └── & other files
├── signal_project/
│   └── settings.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── manage.py
```

---

## ✅ Author

Assignment by: **Nikhil Pentewar**  
Date: **19th May 2025**
