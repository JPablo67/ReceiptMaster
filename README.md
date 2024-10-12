# ReceiptMaster - Efficient Receipt Management API

**ReceiptMaster** is a powerful and user-friendly API designed to help users manage and organize their receipts, ingredients, recipes, and shopping lists in a collaborative environment. Built using **FastAPI** with an underlying **MySQL** database, the API is optimized for performance, scalability, and ease of use.

## Key Features

1. **User Management**:
   - Create, update, and manage users and their roles within groups.
   - Users can belong to multiple groups, allowing for collaborative management of receipts, menus, and shopping lists.

2. **Recipe and Menu Management**:
   - Store and categorize recipes, complete with ingredients, instructions, cooking time, and difficulty levels.
   - Group-based sharing of recipes, allowing users to contribute and manage shared menus.
   - Nutrition tracking with support for calorie units and dietary categories.

3. **Shopping List and Pantry Tracking**:
   - Automatically generate and manage shopping lists based on group menus and planned meals.
   - Track pantry items with expiration dates and quantities, ensuring efficient meal planning and minimizing food waste.

4. **Notifications and Alerts**:
   - Users can receive notifications for important events, such as when a recipe or menu is updated, or when pantry items are approaching expiration.

5. **Efficient API Key Authentication**:
   - Secure endpoints with API key-based authentication to ensure that only authorized users can access and modify data.

## Technologies Used

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) – A high-performance Python web framework for building APIs with async support.
- **Database**: [MySQL](https://www.mysql.com/) – A robust relational database system with support for advanced query handling.
- **ORM**: [Peewee](http://docs.peewee-orm.com/) for the application’s runtime data management, and [SQLAlchemy](https://www.sqlalchemy.org/)/[Alembic](https://alembic.sqlalchemy.org/en/latest/) for managing database migrations.
- **Docker**: The application is containerized using Docker for easy deployment and environment management.
- **Database Management**: Alembic is integrated for handling schema migrations, ensuring smooth updates to the database structure over time.

## Collaborative Group System

- **Groups** allow users to collaborate by sharing menus, recipes, and ingredients. 
- Each group can manage its own set of recipes, ingredients, and menus, with designated roles for managing content.
- Group members can work together to build shopping lists, manage pantries, and track shared inventories.

## Extensible Architecture

- **ReceiptMaster** is designed to be extensible, with a modular architecture allowing for easy expansion and integration with other services.
- Support for future enhancements, such as integrating external APIs to fetch ingredient data or expanding authentication methods.

## Use Case Scenarios

- **Personal Receipt Management**: Track your personal recipes and generate shopping lists based on meal planning.
- **Family or Group Meal Planning**: Collaborate with family or friends by sharing recipes, creating joint menus, and tracking pantry items.
- **Fitness and Nutrition Tracking**: Track calories and nutrition information for your recipes, helping users manage dietary needs and health goals.