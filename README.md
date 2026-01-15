# 🎨 Cartoonify: Image to Cartoon Web App

Cartoonify is a **Flask + OpenCV based web application** that allows users to upload an image and instantly convert it into a **cartoon-style image**.
The app provides a **modern UI**, **live image preview**, **remove image option**, and **download functionality**.

---

## ✨ Features

* 🖼 Upload any image (JPG, PNG, WEBP)
* 👁 Live preview before processing
* ❌ Remove uploaded image & upload a new one
* 🎨 Convert image into cartoon style using OpenCV
* ⬇ Download the cartoonized image
* 💻 Clean & responsive UI
* ⚡ Fast processing

---

## 🛠 Tech Stack

**Frontend**

* HTML5
* CSS3
* JavaScript

**Backend**

* Python
* Flask

**Image Processing**

* OpenCV
* NumPy

---

## 📁 Project Structure

```
Cartoonify/
│
├── app.py                  # Flask application
├── cartoon.py              # Cartoon image processing logic
├── README.md
│
├── static/
│   ├── uploads/             # Uploaded images
│   └── results/             # Cartoonized images
│
└── templates/
    └── index.html           # Frontend UI
```

---

## 🚀 How It Works

1. User uploads an image from the browser
2. Image is sent to Flask backend
3. OpenCV applies:

   * Edge detection
   * Bilateral filtering
   * Color quantization
4. Cartoon image is generated and saved
5. User can preview and download the result

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/cartoonify.git
cd cartoonify
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install flask opencv-python numpy
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots (Optional)

You can add screenshots here for better presentation.

---

## 📌 Future Improvements

* 🎚 Cartoon intensity slider
* ⏳ Loading animation
* 🤖 AI-based cartoon (AnimeGAN)
* ☁ Cloud deployment (Render / Railway)
* 🧹 Auto-clean old images

---

## 🎓 Use Cases

* University / Final Year Project
* Hackathon demo
* Portfolio project
* Startup MVP
* Learning Flask & OpenCV integration

---

## 👨‍💻 Author

**Hamza**
Founder & Community Lead – LoopLab
President, Student Community

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.

---
