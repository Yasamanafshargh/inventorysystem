# Inventory Management System

## Project Overview
The **Inventory Management System** is a web-based application built using **Python and Django**. It provides a structured platform for managing inventory, tracking orders, and analyzing product sales. The system differentiates between two user roles: **Admin** and **Staff**, each with distinct permissions and functionalities.

## Technologies Used
- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** MySQL (using Django ORM, CRUD-based)

## User Roles and Functionalities
### 1. Admin
Admins have full access to the system and can perform the following tasks:
- View, edit, and delete products.
- View staff profiles.
- View and manage orders.
- Access summary charts for:
  - Products per quantity.
  - Products per order.
  - Least sold products.
  - Most sold products.

### 2. Staff
Staff members have restricted access and can only:
- Purchase products.
- View a simplified dashboard with relevant functionalities.

## System Architecture
The system follows Django's **MTV (Model-Template-View)** architecture:
1. **Models:** Represent the database structure and define data relationships.
2. **Templates:** HTML files that handle the front-end display.
3. **Views:** Handle business logic and process user requests.

### Database Models
The system includes three primary models:
- **Profile:** Stores user details and role information (admin or staff).
- **Product:** Contains product information such as name, price, and stock quantity.
- **Order:** Tracks purchase details, including customer, product, quantity, and status.

The system's database follows the **CRUD (Create, Read, Update, Delete)** principles, ensuring smooth and efficient management of records.

## Django Apps
The system is divided into two Django apps for better modularity:
- **User:** Handles authentication, user profiles, and role management.
- **Dashboard:** Manages product inventory, orders, and analytics.

## Django ORM
The project utilizes Django's **Object-Relational Mapping (ORM)** to interact with the MySQL database efficiently. Key ORM operations used:
- **Querying data:** `Product.objects.all()`, `Order.objects.filter(status='Completed')`
- **Creating records:** `Product.objects.create(name='Laptop', price=1000, stock=10)`
- **Updating records:** `product.stock -= 1; product.save()`
- **Deleting records:** `product.delete()`

## Installation and Setup
Follow these steps to set up and run the project locally:

### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.7)
- Django
- MySQL

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yasamanafshargh/inventorysystem.git
   cd inventory-management-system
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the database in `settings.py`**
5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
8. **Access the application:** Open `http://127.0.0.1:8000/` in your browser.

## Summary
This **Inventory Management System** provides an intuitive interface for admins and staff to manage inventory efficiently. By leveraging Django’s powerful architecture and ORM, the system ensures smooth data management and scalability.


---

**Author:** Yasaman Afshar Ghasemloo  
**University:** Islamic Azad University Of Tehran Central Branch

