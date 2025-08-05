🖥️ **UniProject – University E-Commerce Platform**

UniProject is a Django-based web application built as part of a final project at Software University (SoftUni). It simulates an online tech store where users can browse, search, and purchase computers and accessories. The project demonstrates full-stack development skills using Python and Django, with a clean modular structure and secure account handling.

---

## 🚀 Features

- 🛒 Browse and search products (computers, peripherals, and components)  
- 👤 Secure user registration and login via Django  
- 🧰 Product management for staff users  
- 🧑‍💻 Admin dashboard with full backend control  
- 🧾 Shopping cart and simulated checkout  
- ⚙️ Custom models with dynamic forms and validation  

---

## 🛠️ Tech Stack

| Layer       | Technology                   |
|------------|------------------------------|
| Frontend    | HTML5, CSS3, JavaScript       |
| Backend     | Python 3.13, Django Framework |
| Database    | SQLite (default)              |
| Environment | `python-dotenv` for `.env`    |
| Versioning  | Git & GitHub                  |

---

## 📦 Installation & Setup

To run UniProject locally:

```bash
# 1. Clone the repository
git clone https://github.com/Ivak2002/UniProject.git
cd UniProject

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Create a .env file with the following:
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=db.sqlite3

# 5. Apply migrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
```

---

📄 Usage Guide
🔐 Register or log in to your user account

🖱️ Browse the catalog and add products to your cart

🧮 Simulate checkout and cart updates

🛠️ Staff users can edit or remove product listings

🧑‍💼 Admins have complete oversight via Django admin panel

---

---

🎓 Project Purpose
This project was created as an educational final assignment to showcase web development capabilities. It serves as a full-stack example for managing user accounts, dynamic product listings, and secure admin workflows in Django.

---

📢 Contributing
This is an academic portfolio project and currently not open to public contributions. Feel free to fork it for learning purposes or personal experimentation.

---

⚖️ License
Licensed under the MIT License — see the LICENSE file for more details.

---

Questions or feedback? Open a GitHub Issue or get in touch through the repository: 🔗 https://github.com/Ivak2002/UniProject

---
---

## 🌐 Live Demo

Explore the full project in action:  
🔗 [ivakacomputers.ivakar.site](https://ivakacomputers.ivakar.site/)

---
