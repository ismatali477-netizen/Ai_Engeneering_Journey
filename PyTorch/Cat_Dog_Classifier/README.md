# 🐱🐶 Cat-Dog Image Classifier

A deep learning image classification project built with **PyTorch** and **ResNet18** that classifies images as either a cat or a dog.

The project includes model training, evaluation, single-image prediction, and a simple desktop GUI application.

## 🚀 Features

- 🧠 ResNet18-based image classification
- 🐱 Cat vs Dog prediction
- 📊 Training and test accuracy evaluation
- 📈 Confusion matrix and classification report
- 🎯 Prediction confidence scores
- 🖼️ Single-image prediction
- 🖥️ Tkinter desktop GUI
- 💾 Saved PyTorch model
- 🛡️ Error handling for invalid images
- 📦 Reproducible dependencies with `requirements.txt`

## 🛠️ Technologies

- Python
- PyTorch
- Torchvision
- Pillow
- Scikit-learn
- Tkinter

## 📁 Project Structure

```text
Cat_Dog_Classifier/
│
├── datasets/                 # Local dataset (not tracked by Git)
│
├── model.py                  # ResNet18 model definition
├── train.py                  # Model training and evaluation
├── predict.py                # Prediction for individual images
├── app.py                    # Desktop GUI application
├── cat_dog_model.pth         # Trained model weights
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
⚙️ Installation

Clone the repository and move into the project directory:

git clone https://github.com/ismatali477-netizen/Ai_Engeneering_Journey.git
cd Ai_Engeneering_Journey/PyTorch/Cat_Dog_Classifier

Create and activate a virtual environment:

Windows
python -m venv .venv
.venv\Scripts\activate

Install the dependencies:

pip install -r requirements.txt
🧠 Training the Model

To train the model:

python train.py

The training process evaluates the model on the test dataset and reports the classification performance.

The trained weights are saved as:

cat_dog_model.pth
🔍 Making Predictions

To classify an image:

python predict.py "path/to/your/image.jpg"

Example:

python predict.py "C:\Users\YourName\Pictures\cat.jpg"

The program returns:

Predicted class
Confidence score

Example:

Prediction: CAT
Confidence: 93.73%
🖥️ Running the GUI

Launch the desktop application with:

python app.py

The application allows you to:

Select an image
Preview the image
Get the predicted class
View confidence scores for both CAT and DOG
📊 Model Performance

The trained model achieved:

Metric	Result
Training Accuracy	94.00%
Test Accuracy	95.50%
Confusion Matrix
[[99, 1],
 [8, 92]]

The model correctly classified most of the test images, with 99 cats and 92 dogs classified correctly.

🧪 Classification Report
Class	Precision	Recall	F1-Score
CAT	0.93	0.99	0.96
DOG	0.99	0.92	0.95
🎯 Example Predictions

The model was also tested on images outside the training/test dataset and successfully classified several unseen cat and dog images with varying confidence levels.

📚 What I Learned

Through this project, I practiced:

.Building image classification pipelines
.Working with PyTorch
.Using pretrained CNN architectures
.Transfer learning with ResNet18
.Image preprocessing and normalization
.Training and evaluating neural networks
.Using confusion matrices and classification reports
.Saving and loading PyTorch models
.Building a GUI around an AI model
.Managing Python dependencies
.Using Git and GitHub for version control

🔮 Future Improvements
Possible improvements include:

.Training with a larger dataset
.Data augmentation
.Fine-tuning more ResNet18 layers
.Comparing different CNN architectures
.Improving model generalization
.Building a web-based version
.Deploying the model with FastAPI

Built as part of my journey toward becoming an AI Engineer.