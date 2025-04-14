# 📚 Library Management System


A modern, lightweight **Library Management System** built with Flask and JSON storage. Manage your book collection, track issued books, and streamline library operations with this easy-to-use web application.

## ✨ Features

- **📖 Book Management**
  - Add new books with details (Title, Author, Quantity)
  - View complete book inventory
  - Remove books from collection
  - Prevent removal of issued books

- **🎫 Issuance System**
  - Issue books to students
  - Track due dates
  - Mark books as returned
  - View all issued books

- **🎨 Modern Interface**
  - Sleek dark theme
  - Responsive design
  - Intuitive navigation
  - Flash notifications

- **⚙️ Technical Highlights**
  - JSON file storage (no database required)
  - Password hashing for security
  - Clean Flask backend
  - Easy deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the system at:
   ```
   http://localhost:5000
   ```

## 🛠️ Usage Guide

1. **Add Books**  
   Navigate to *Add Book* and fill in book details

2. **View Books**  
   Check *Book List* to see all available books

3. **Issue Books**  
   Go to *Issue Book* to lend books to students

4. **Track Issued Books**  
   View all active loans in *Issued Books*

5. **Remove Books**  
   Delete books from collection (when not issued)

## 🌐 Deployment

Easily deploy to Render with one-click:

[![Deploy to Render]([https://render.com/deploy](https://library-management-e471.onrender.com/))]

## 📂 Project Structure

```
library-management/
├── app.py                  # Main application
├── data/                   # JSON data storage
│   ├── books.json          # Book records
│   └── issued_books.json   # Issued books records
├── templates/              # HTML templates
├── static/                 # CSS/JS assets
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



Project Link: [https://github.com/yourusername/library-management-system](https://github.com/yourusername/library-management-system)

---

Made with ❤️ and Python 🐍
