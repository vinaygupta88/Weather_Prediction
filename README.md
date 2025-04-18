# Weather_Prediction
A repository for weather prediction using machine learning models. It forecasts conditions like rain, snow, drizzle, and sunny weather based on historical data. Includes data preprocessing, model training, evaluation, and deployment scripts for accurate, real-time weather insights.

## 📂 Project Structure

```
weather_project/
│
├── weather_app 
|    |──static/
|    | └── css/
|    |     └── style.css      
|    | └── image/
│    |  |── homebg                 
│    |  └── logo 
|    |
|    ├── templates/
│    |    ├── index.html          
│    |    ├── about.html          
│    |    ├── predict.html        
│    |    ├── submit.html         
│    |    ├── navbar.html 
|    |
|    ├── _init_.py
|    ├── admin.py
|    ├── apps.py
|    ├── models.py
|    ├── tests.py
|    ├── urls.py
|    ├── views.py
|
├── weather_project 
|    ├── _init_.py
|    ├── asgi.py
|    ├── setting.py
|    ├── urls.py
|    ├── wsgi.py 
|    
|                   
├── manage.py                
├── rfp.pkl              
├── requirements.txt  
│
|── data/
|   ├── productivity.csv    
|   └── train_model.ipynb   # Jupyter notebook for training the model 
|     
├── Procfile                
├── README.md                    

```

---

## ⚙️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- Bootstrap (Responsive UI)
- HTML, CSS, JavaScript (jQuery)
- Gunicorn (for deployment)
- Render (Free hosting)

---

## 💻 How to Run Locally

### 1. Clone the repo
 ''' clone my repo.......'''

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python manage.py runserver
```

Open [http://localhost:5000](http://localhost:5000) in your browser 🚀

---

## ✍️ Author

Made  by **[Vinay Kumar](https://vinaygupta88.github.io/Myportfolio/)**

---

## 📜 License

This project is open-source and free to use for learning, research, and personal projects. No formal license is attached—just give credit if you find it helpful!
