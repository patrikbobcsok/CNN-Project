# Animals-10 Image Classification Project

##  Overview

This project applies Convolutional Neural Networks (CNNs) to classify images from the Animals-10 dataset into 10 animal categories. The project progresses through 3 stages: a basic CNN model, an improved version (V2), and a VGG16 transfer learning model.

##  Structure

```
CNN-Project/
├── CNN_Image_Classifier_v1/           # Baseline CNN model
├── CNN_Image_Classifier_v2/           # Improved CNN with BN, LR scheduling
├── CNN_Image_Classifier_VGG16/        # Transfer learning with VGG16
├── Streamlit App/                     # Web app interface 
├── Translating-Class_Names/           # Class name mapping
├── Testing/                           # Evaluation utilities
├── Animals-10 CNN Classification Project - Report.txt
├── app.ipynb
└── README.md
```

##  Goals

- Understand and build CNNs from scratch.
- Apply techniques to handle imbalanced datasets (e.g. class weights).
- Fine-tune a pre-trained model (VGG16).
- Compare performance across model versions.
- Visualize training results and predictions.

##  Deliverables

- Jupyter Notebooks for each model (`v1`, `v2`, `VGG16`)
- A final report comparing performance metrics.
- Visualizations: training curves, confusion matrix, precision-recall.
- A lightweight Streamlit app.

##  Results Summary

| Model              | Accuracy | Precision | Recall | F1 Score |
|-------------------|----------|-----------|--------|----------|
| Baseline (V1)     | ~59.10%  | ~56.03%   | ~54.48%| ~55.00%  |
| Improved (V2)     | ~81.18%  | ~80.57%   | ~79.69%| ~80.08%  |
| Transfer (VGG16)  | ~89.55%  | ~88.75%   | ~89.09%| ~88.86%  |

📎 [Read Full Report](Animals-10%20CNN%20Classification%20Project%20-%20Report.txt)

##  Tech Stack

- Python 
- TensorFlow / Keras
- Jupyter Notebook
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit (for deployment)

##  Author

*Patrik Bobcsok*

