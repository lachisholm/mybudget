# Overview

As a software engineer, I strive to enhance my skills by developing practical and impactful software solutions. This project is a Python-based Budget Tracker designed for single parents or single mothers to help users efficiently manage their finances by tracking income and expenses, setting up different types of budgets, and providing detailed transaction summaries. This is currently a work in progress.

The myBudget Tracker allows users to add, deduct, and transfer funds between categories, keep a record of transactions with timestamps, and view both budget summaries and detailed transaction logs. The purpose of this project is to create a user-friendly application that aids users in achieving better financial management and planning, helps to track additional flows of help outside of job related income.

[Software Demo Video - Under Construction](http://youtube.link.goes.here)

# Development Environment

To develop this software, I utilized the following tools and programming languages:

- **Development Tools:** Visual Studio Code (VSCode), Git
- **Programming Language:** Python 3.x
- **Libraries:** None required; the application here although does rely on Python's standard library, particularly `datetime`.

These tools provided a robust and efficient environment for coding, testing, and version control. Visual Studio Code offers a wide range of extensions and integrations that facilitated a seamless development experience. Using Git ensured that the code was versioned and collaborated upon efficiently.

# Useful Websites

The following websites were instrumental in the development of this project. They provided valuable resources, tutorials, and documentation that guided me through various aspects of Python programming and application development:

- [Python Official Documentation](https://docs.python.org/3/): This site offers comprehensive documentation on Python, including detailed explanations of modules, libraries, and language features. It is an indispensable resource for understanding Python's capabilities and best practices.
- [Real Python](https://realpython.com/): Real Python provides a wealth of tutorials and articles on Python programming. The practical examples and in-depth discussions helped me to understand complex concepts and apply them effectively in my project.
- [W3Schools](https://www.w3schools.com/python/): Known for its easy-to-follow tutorials, W3Schools was a great resource for quick references and learning Python syntax and basic programming techniques.
- [GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/): This site offers a variety of coding tutorials and algorithm explanations. It was particularly helpful for understanding the logic and structure required for developing robust Python applications.
- [Programiz](https://www.programiz.com/python-programming): Programiz provides clear and concise tutorials with examples, making it easier to grasp Python programming concepts and apply them to real-world scenarios.

# Future Work

There are several enhancements and features planned for future versions of this project. These improvements aim to expand the functionality and user experience of the Budget Tracker:

- \*\*Implement a Graphical User Interface (GUI)

- **Implement a Graphical User Interface (GUI):** While the current version is command-line based, I plan to add a GUI using libraries like Tkinter or PyQt to make the application more user-friendly and visually appealing. This will allow users to interact with the budget tracker through a more intuitive interface.
- **Data Visualization Tools:** I aim to integrate data visualization tools using libraries such as Matplotlib or Plotly to help users better understand their financial data. Graphs and charts illustrating income and expense trends would provide valuable insights and aid in financial planning.
- **Exporting and Importing Data:** I plan to enable the export and import of data to/from CSV files to make data management more flexible. Users could back up their data, share it with others, or import data from other financial management tools.
- **User Authentication and Profile Management:** Adding features for user authentication would allow multiple users to use the application with their personalized settings. Each user could have their own budget categories, transaction history, and preferences.
- **Mobile Version:** Developing a mobile version of the application using frameworks like Kivy would allow users to manage their finances on the go. A mobile app would offer convenience and accessibility, making the Budget Tracker a versatile tool for financial management.

# Code Explanation

The core functionality of the myBudget Tracker is implemented in the `myBudgetTracker` class. Below is a detailed explanation of its components:

### Class: `BudgetTracker`

- **Attributes:**

  - `categories`: A dictionary to store category names and their balances. This allows for easy tracking and updating of financial categories.
  - `transactions`: A list to store transaction records. Each record includes the date, category, type (add or deduct), and amount, providing a comprehensive transaction history.
  - `budget_type`: Stores the type of budget chosen (Real or Projected). This helps customize the budget setup based on the user's preference.

- **Methods:**
  - `__init__()`: Initializes the tracker with empty categories and transactions. This sets up the initial state of the budget tracker.
  - `add_category(category_name)`: Adds a new category if it doesn't exist. This method ensures that all financial activities are categorized.
  - `add_income(category_name, amount)`: Adds income to a category. It updates the balance and logs the transaction.
  - `deduct_expense(category_name, amount)`: Deducts an expense from a category. It adjusts the balance and records the transaction.
  - `move_money(from_category, to_category, amount)`: Transfers money between categories. This method combines deduction and addition operations to facilitate fund transfer.
  - `view_summary()`: Prints a summary of all categories and their balances. This provides a quick overview of the financial status.
  - `view_details()`: Prints all transactions. This offers a detailed log of all financial activities.
  - `setup_budget()`: Sets up the budget type (Real or Projected). This method guides the user through the initial budget setup process.
  - `handle_real_budget()`: Handles the setup for a real budget. It prompts the user to enter actual income details.
  - `handle_projected_budget()`: Handles the setup for a projected budg

## For Further information

### Contact me @

#### Lora Chisholm

#### loraperrychisholm@gmail.com
