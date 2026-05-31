
Intel Image Classification using Deep Learning

Project Overview

This project implements an automated image classification system for natural scene images using Deep Learning and Convolutional Neural Networks (CNNs). The objective is to classify images into one of six scene categories:

Buildings
Forest
Glacier
Mountain
Sea
Street
The project also focuses on model evaluation, failure analysis, model refinement using transfer learning, and deployment through a Streamlit application.

Dataset

Dataset: Intel Image Classification Dataset

Source:
https://www.kaggle.com/datasets/puneet6060/intel-image-classification

Classes

Buildings
Forest
Glacier
Mountain
Sea
Street
Dataset Structure

seg_train/

    buildings/

    forest/

    glacier/

    mountain/

    sea/

    street/

 

seg_test/

    buildings/

    forest/

    glacier/

    mountain/

    sea/

    street/

 

seg_pred/

seg_train: Training images
seg_test: Testing images
seg_pred: Unlabeled images for prediction
Project Tasks

Task 1: Dataset Exploration and Preparation

Load dataset
Explore classes and image distribution
Visualize sample images
Resize images to a uniform size
Create training, validation, and test datasets
Task 2: Data Preprocessing and Augmentation

Applied preprocessing techniques:

Rescaling
Rotation
Zoom
Horizontal Flip
Width Shift
Height Shift
Task 3: CNN Model Design and Training

Implemented a Convolutional Neural Network consisting of:

Convolution Layers
Max Pooling Layers
Fully Connected Layers
Dropout Regularization
Training and validation performance were tracked using:

Accuracy Curves
Loss Curves
Task 4: Model Evaluation

Evaluation techniques:

Test Accuracy
Classification Report
Confusion Matrix
Task 5: Error and Failure Analysis

Identified misclassified images
Visualized prediction errors
Analyzed common failure patterns
Task 6: Model Refinement

Transfer Learning was applied using MobileNetV2:

Pretrained ImageNet weights
Frozen feature extractor
Custom classification head
Performance was compared against the baseline CNN model.

Task 7: Streamlit Deployment

Developed an interactive Streamlit application that:

Accepts uploaded images
Predicts scene category
Displays classification results
Bonus Task: Model Interpretability

Implemented interpretability techniques to understand model decision-making and visualize important image regions influencing predictions.

Technologies Used

Python
TensorFlow / Keras
NumPy
Pandas
Matplotlib
Seaborn
Scikit-Learn
Streamlit
Pillow
Project Structure

Intel_Image_Classification_Project/

 

│

├── models/

│   ├── cnn_baseline.h5

│   └── intel_mobilenet.h5

│

├── greeshma_exit_exam.ipynb

│

├── app.py

│

├── requirements.txt

│

└── README.md

Installation

Clone Repository

git clone <repository-link>

cd Intel_Image_Classification_Project

Create Virtual Environment

python -m venv venv

Activate Virtual Environment

Windows:

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Running the Notebook

Open:

greeshma_exit_exam.ipynb

Run all cells sequentially.

Running the Streamlit Application

streamlit run app.py

The application will open in your browser.

Upload an image and the model will predict its scene category.

Model Performance

Two models were developed:

Baseline CNN

Custom CNN architecture
Trained from scratch
Improved MobileNetV2 Model

Transfer Learning
Better feature extraction
Improved classification accuracy
The MobileNetV2 model achieved superior performance compared to the baseline CNN.

Key Findings

Data augmentation improved model generalization.
Glacier and Mountain scenes were commonly confused due to visual similarities.
Buildings and Street scenes occasionally overlapped because of urban structures.
Transfer learning significantly improved classification performance.
Future Improvements

Fine-tuning MobileNetV2 layers
Hyperparameter optimization
Advanced augmentation techniques
Grad-CAM visualizations
Deployment using cloud platforms
Author

Greeshma P J

Data Analyst | AI & Machine Learning Enthusiast

 

