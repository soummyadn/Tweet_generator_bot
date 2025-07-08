# 🐦 Tweet Generator Bot

A smart, AI-powered Tweet Generator Bot that creates and posts engaging tweets automatically. Built with **FastAPI**, **SolidJS + Vite**, and **MongoDB**, this full-stack project is designed for simplicity, speed, and creativity.

---

## 🚀 Features

- ✨ Generate AI-powered tweets with a single click  
- 🔐 API key authentication for secure tweet posting  
- 📤 Auto-post tweets to Twitter clone UI via API  
- 📊 Track and display tweet history (optional MongoDB support)  
- ⚡️ Built with FastAPI (backend) + SolidJS (frontend) for lightning-fast performance  

---

## 🛠 Tech Stack

- **Frontend**: [SolidJS](https://www.solidjs.com/) + [Vite](https://vitejs.dev/)  
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)  
- **Database**: [MongoDB](https://www.mongodb.com/) (Optional)  
- **Hosting**: Render, Cloudflare Pages  

---

## 📦 Project Structure

```
tweet_generator_bot/
├── backend/
│   ├── main.py           # FastAPI app
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── src/
│   │   └── ...           # SolidJS components
│   └── vite.config.js    # Vite config
├── README.md
└── .gitignore
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/tweet-generator-bot.git
cd tweet-generator-bot
```

### 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

> 💡 Requires Python 3.9+ and `uvicorn`.

### 3. Frontend Setup (SolidJS + Vite)

```bash
cd frontend
npm install
npm run dev
```

---

## 📤 Tweet Posting API

To post a tweet, send a `POST` request to:

```
https://twitterclone-server-2xz2.onrender.com/post_tweet
```

### Headers:

| Key     | Value         |
|---------|---------------|
| api-key | your-api-key  |

### Body (JSON):

```json
{
  "tweet": "This is an awesome AI-generated tweet!"
}
```

✅ Check post success here: [Twitter Clone UI](https://twitter-clone-ui.pages.dev/)

---

## 📸 Screenshot

![Tweet Bot UI Preview](https://via.placeholder.com/800x400.png?text=Tweet+Bot+UI+Preview)

---

## 🤝 Contributing

1. Fork the repository  
2. Create your feature branch: `git checkout -b feature/your-feature`  
3. Commit your changes: `git commit -m 'Add some feature'`  
4. Push to the branch: `git push origin feature/your-feature`  
5. Open a Pull Request 🚀  

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- [OpenAI GPT](https://openai.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SolidJS](https://www.solidjs.com/)
- [MongoDB](https://www.mongodb.com/)
- [Render](https://render.com/)
- [Cloudflare Pages](https://pages.cloudflare.com/)

---

## 💬 Contact

Created with ❤️ by **[Soumya](https://github.com/yourusername)**  
DM for questions, feedback, or collaboration!
