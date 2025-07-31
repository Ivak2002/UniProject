# 🖥️ UniProject – University E-Commerce Platform

UniProject is a Django-based web application developed as a final-year university project. It simulates a modern online store where users can browse, search, and purchase computers and computer components. The platform showcases full-stack development capabilities using Python and Django.

## 🚀 Features

- Browse and search products (computers and parts)
- Shopping cart functionality
- Secure user authentication and registration
- Staff controls for product management
- Admin panel for complete backend oversight

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap (optional enhancement)
- **Backend**: Python 3.x, Django Framework
- **Database**: SQLite (default) or PostgreSQL (optional)
- **Authentication**: Django's built-in user system

## 📦 Installation & Setup

To run the project locally:

```bash
# Clone the repository
git clone https://github.com/Ivak2002/UniProject.git
cd UniProject

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Apply migrations and start the development server
```
# 📄 Usage

- Sign up or log in with your credentials
- Browse products, add items to your cart, and simulate a checkout
- **Staff users** can:
  - Add new products
  - Edit existing listings
  - Delete products from the catalog
- **Admin users** manage everything via Django’s admin dashboard

# 🎓 Project Purpose

This application was built as part of a final university project to demonstrate practical web development skills. It serves as an educational showcase of how to construct a working e-commerce site using Django.

# 📢 Contributing

This is an academic project and not open to public contributions at this time. Feel free to fork the repo for educational or personal use.

# ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.

# 📬 Contact

For questions or feedback, reach out via GitHub Issues or connect through the repository.

python manage.py migrate
python manage.py runserver
