# cat_or_dog_prediction
# 🐱🐶 Cat vs Dog Image Classification

## 📌 Project Overview

This project is a **Deep Learning-based Image Classification system** that predicts whether an uploaded image is a **Cat 🐱 or Dog 🐶**.

It uses a **Convolutional Neural Network (CNN)** built with TensorFlow/Keras and provides a simple **Flask web interface** for real-time predictions.

---

## 🚀 Features

* Upload an image and get instant prediction
* Classifies images into **Cat or Dog**
* Built using **CNN (Deep Learning)**
* Simple and user-friendly web interface
* Real-time prediction using Flask

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Flask
* HTML

---

## 📁 Project Structure

```
cat_dog_prediction/
│
├── dataset/
│   ├── train/
│   │   ├── cats/
│   │   ├── dogs/
│   ├── test/
│       ├── cats/
│       ├── dogs/
│
├── static/
├── templates/
│   └── index.html
│
├── train.py
├── app.py
├── predict.py
└── model.h5
```

---

## 📊 How It Works

1. Images are preprocessed (resized, normalized)
2. CNN model is trained on cat & dog images
3. Model is saved as `model.h5`
4. Flask app loads the model
5. User uploads image → prediction displayed

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```
git clone <your-repo-link>
cd cat_dog_prediction
```

### 2️⃣ Install Dependencies

```
pip install tensorflow keras numpy flask pillow
```

### 3️⃣ Train the Model

```
python train.py
```

### 4️⃣ Run Flask App

```
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📷 Demo

Upload an image → Get prediction:

* 🐱 Cat
* 🐶 Dog

---

## ⚠️ Important Notes

* Make sure dataset is properly structured
* `model.h5` will be generated after training
* `static/` folder is required to store uploaded images

---

## 🔥 Future Improvements

* Use Transfer Learning (MobileNet, ResNet)
* Improve accuracy
* Deploy on cloud (Render / AWS)
* Add confidence score
* Better UI design

---

## 👨‍💻 Author

**Venkata Nagesh**
B.Tech (CSE - AI & ML)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
