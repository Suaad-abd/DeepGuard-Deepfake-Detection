# DeepGuard - Deepfake Detection Web Application

**DeepGuard** is a collaborative graduation project developed by a team of five cybersecurity students.  
It is a web-based application designed to detect fake (deepfake) images and videos.  
The project aims to fight misinformation by identifying manipulated media content and ensuring authenticity.  

---

## Features
- Upload and analyze **images** to check for authenticity.  
- Upload and analyze **videos** for potential deepfake manipulation.  
- User-friendly **web interface** built with Flask.  
- API endpoints for image and video detection.  
- Extendable design (additional endpoints like `about` and `contact` included).  

---

##  Technology Stack
- **Backend:** Python, Flask, Flask-CORS  
- **Frontend:** HTML, CSS (templates & static files)  
- **Libraries:** Jinja2, Werkzeug, Click, Colorama  
- **Environment:** Virtual Environment (`venv`)  

---

##  Project Structure
```
DeepGuard-Deepfake-Detection/
│
├── run.py               # Main application file
├── requirements.txt     # Dependencies
├── templates/           # HTML templates (home, detection, about, contact)
├── static/              # Static files (CSS, JS, images)
└── uploads/             # Saved images and videos (optional)
```

---

##  How to Run Locally
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/DeepGuard-Deepfake-Detection.git
   cd DeepGuard-Deepfake-Detection
   ```

2. Create and activate a virtual environment:  
   ```bash
   python -m venv my
   my\Scripts\activate   # On Windows
   source my/bin/activate  # On Mac/Linux
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:  
   ```bash
   python run.py
   ```

5. Open in browser:  
   ```
   http://127.0.0.1:5000/
   ```

---

##  About the Project
This project is a **team effort** to help combat misinformation by detecting deepfake content using advanced machine learning techniques.

- **Mission:** Provide tools to detect deepfakes and protect the authenticity of digital content.  
- **Technology:** Uses AI & machine learning algorithms to analyze inconsistencies in media.  
- **Impact:** Helps fight the spread of misleading information and strengthens trust in digital media.  

---

👩‍💻 **Team Members (Cybersecurity Students):**  
- Suaad Al-Ahmari  
- 4 other students  

📍 Imam Mohammed Ibn Saud Islamic University – 2025  

	
