This project is a Telegram bot for an online shop, developed using aiogram, SQLAlchemy, and PostgreSQL.

## Description

The bot allows users to browse a product catalog, select products by category, and get information about selected products. It uses a PostgreSQL database to store information about users, categories, and products.

## Technologies

* **Python 3.13**
* **aiogram** - for creating the Telegram bot
* **SQLAlchemy** - for database interaction
* **PostgreSQL** - database
* **pytest** - for testing
* **Docker** - for containerization

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <your_repository>
    cd <your_repository>
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    TELEGRAM_BOT_TOKEN=your-telegram-bot-token
    ADMIN_USER_ID=your-admin-user-id
    
    POSTGRES_DB=your-database-name
    POSTGRES_USER=your-database-username
    POSTGRES_PASSWORD=your-database-password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**

    * Create a `.env` file in the project root.
    * Add the following variables:

        ```
        TOKEN=<your_bot_token>
        SQLALCHEMY_URL=postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}
        ```

        Replace `<your_bot_token>` with your Telegram bot token.

        If you are using docker, then SQLALCHEMY_URL should be the same as in docker-compose.yml.

5.  **Run Docker (recommended):**

    * Install Docker and Docker Compose.
    * Start the containers:

        ```bash
        docker-compose up -d
        ```

6.  **Run the bot without Docker:**

    * Install PostgreSQL and create a `postgres_db` database.
    * Run the bot:

        ```bash
        python main.py
        ```

## Testing

1.  **Install pytest:**

    ```bash
    pip install pytest pytest-asyncio
    ```

2.  **Run tests:**

    ```bash
    pytest tests/
    ```

## Project structure

```
your_project/
├── app/
│   ├── handlers.py       # Command and event handlers
│   ├── keyboards.py      # Bot keyboards
│   ├── database/
│   │   ├── models.py       # Database models
│   │   ├── requests.py     # Database requests
│   ├── __init__.py
├── tests/
│   ├── conftest.py       # Test fixtures
│   ├── test_handlers.py  # Tests for handlers
│   ├── test_database.py  # Tests for database
│   ├── test_keyboards.py # Tests for keyboards
├── main.py               # Bot startup
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Dockerfile configuration
└── README.md             # This file
```

## Usage

1.  Start the bot in Telegram.
2.  Use the `/start` command to begin.
3.  Click the "Catalog" button to view product categories.
4.  Select a category and a product to view information.

## Containerization

The project is containerized with Docker. `docker-compose.yml` defines services for the PostgreSQL database and the bot.

## License

[Specify license, if any]
