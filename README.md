
# LearnFlix 🎬

LearnFlix is a **Netflix-style learning platform** built using **Python and Flask**.  
It allows users to explore educational videos organized by technology domains and learning levels such as **Trending, Beginner, Advanced, and Recommended**.

The interface is inspired by streaming platforms like Netflix, making it easier to discover and watch learning content in a structured and visually appealing way.

---

## 🚀 Features

- Netflix-style interface for browsing educational videos
- Multiple learning profiles:
  - Data Science
  - Web Development
  - Artificial Intelligence
  - Programming
- Organized learning sections:
  - Trending
  - Beginner
  - Advanced
  - Recommended
- Embedded YouTube videos for interactive learning
- Dynamic filtering of videos using Flask
- JSON-based video database

---
Images of the home screen is in 
home.png
and interiror of the profile is in 
profile1.png and profile2.png

## 🛠 Tech Stack

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **JSON**

---

## 📂 Project Structure
learnflix
│
│ app.py
│ videos.json
│ README.md
│ requirements.txt
│
├── templates
│ index.html
│ profile.html
│
└── static
avatars/
## ⚙️ Installation

### 1️⃣ Clone the repository


git clone https://github.com/yourusername/learnflix.git


### 2️⃣ Navigate into the project folder


cd learnflix


### 3️⃣ Install dependencies


pip install -r requirements.txt


### 4️⃣ Run the application


python app.py


### 5️⃣ Open the application in your browser


http://127.0.0.1:5000


---

## 📚 How It Works

1. Users select a **learning profile** such as Data Science or Web Development.
2. Flask filters videos from the **videos.json database** based on the selected category.
3. Videos are grouped into sections:
   - Trending
   - Beginner
   - Advanced
   - Recommended
4. The interface displays videos in **Netflix-style horizontal rows**.

---

## 🔮 Future Improvements

Possible upgrades for the platform:

- 🔎 Search functionality for videos
- 👤 User authentication and profiles
- 🎯 Personalized recommendations
- 📊 Video progress tracking
- 🗄 Database integration (MongoDB / PostgreSQL)
- 🎨 Enhanced UI animations and transitions

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork the repository and submit a pull request to improve the project.

---

## 📄 License

This project is open-source and available under the **MIT License**.
