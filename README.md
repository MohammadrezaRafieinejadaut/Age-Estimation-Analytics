# 👤 Deep Learning-Based Facial Age Estimation

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end Deep Learning pipeline to predict continuous human age from single facial images using Transfer Learning with **ResNet-50** in **PyTorch**.

---

## 📌 Key Highlights & Results
- **Task:** Continuous Age Regression
- **Dataset:** UTKFace (~23,165 cleaned aligned face images)
- **Architecture:** Pretrained ResNet-50 (ImageNet weights) with a custom single-neuron regression head.
- **Loss Function:** L1 Loss (Mean Absolute Error)
- **Performance:**
  - **Test MAE:** **3.86 years**
  - **Validation MAE:** **3.66 years**
  - **Training MAE:** **3.97 years**

---

## 📊 Dataset & Preprocessing
- Cleaned corrupted filenames and constrained age range to $\le 80$ years.
- Implemented **Stratified Splitting** across age distributions:
  - **Train:** 16,215 images (70%)
  - **Validation:** 3,475 images (15%)
  - **Test:** 3,475 images (15%)
- **Data Augmentations:** Random Horizontal Flip, Random Rotation ($\pm 10^\circ$), and ColorJitter (Brightness/Contrast).
- Input resolution: $128 \times 128$ normalized with ImageNet statistics.

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/your-username/face-age-estimation-pytorch.git
cd face-age-estimation-pytorch
pip install -r requirements.txt
