# CarNumberDetection

This project is experiment with yolo dists for detecting car numbers.

### Requirements

- Python >= 3.8
- RAM >= 16GB
- GPU >= 8GB
- CUDA >= 11.0

### Used technologies

- YoloV5
- YoloV7
- Tessaract
- DVC

## Quick start

### Environment setup

Make executable file for environment setup:

```bash
chmod +x env_setup.sh
```

Run environment setup:

```bash
./env_setup.sh
```

### Usage with DVC

Run the following command to start the project:

```bash
dvc repro
```

## License

BiFolio is licensed under the MIT License. See [LICENSE](LICENSE) for the full license text.

# Learning process screenshot

![image](docs/images/other/image_2022-10-04_22-38-37.png)

## DVC Dag

![image](docs/images/other/image_2022-10-04_23-05-45.png)

# Experiments

# YOLOv5

<details>

## Images

### yolov5m_Adam_40
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5m_Adam_40/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5m_Adam_40/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5m_Adam_40/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5m_Adam_40/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5m_Adam_40/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5m_Adam_40/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5m_Adam_40/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5m_Adam_40/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5m_Adam_40/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5m_Adam_40/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5m_Adam_40/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5m_Adam_40/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5m_Adam_40/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5m_Adam_40/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5m_Adam_40/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5m_Adam_40/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5m_Adam_40/val_batch2_pred.jpg)
</details>

### yolov5m_SGD_20
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5m_SGD_20/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5m_SGD_20/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5m_SGD_20/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5m_SGD_20/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5m_SGD_20/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5m_SGD_20/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5m_SGD_20/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5m_SGD_20/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5m_SGD_20/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5m_SGD_20/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5m_SGD_20/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5m_SGD_20/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5m_SGD_20/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5m_SGD_20/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5m_SGD_20/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5m_SGD_20/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5m_SGD_20/val_batch2_pred.jpg)
</details>

### yolov5m_SGD_30
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5m_SGD_30/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5m_SGD_30/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5m_SGD_30/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5m_SGD_30/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5m_SGD_30/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5m_SGD_30/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5m_SGD_30/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5m_SGD_30/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5m_SGD_30/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5m_SGD_30/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5m_SGD_30/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5m_SGD_30/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5m_SGD_30/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5m_SGD_30/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5m_SGD_30/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5m_SGD_30/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5m_SGD_30/val_batch2_pred.jpg)
</details>

### yolov5m_SGD_40
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5m_SGD_40/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5m_SGD_40/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5m_SGD_40/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5m_SGD_40/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5m_SGD_40/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5m_SGD_40/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5m_SGD_40/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5m_SGD_40/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5m_SGD_40/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5m_SGD_40/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5m_SGD_40/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5m_SGD_40/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5m_SGD_40/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5m_SGD_40/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5m_SGD_40/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5m_SGD_40/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5m_SGD_40/val_batch2_pred.jpg)
</details>

### yolov5n_AdamW_20
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_AdamW_20/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_AdamW_20/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_AdamW_20/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_AdamW_20/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_AdamW_20/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_AdamW_20/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_AdamW_20/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_AdamW_20/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_AdamW_20/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_AdamW_20/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_AdamW_20/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_AdamW_20/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_AdamW_20/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_AdamW_20/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_AdamW_20/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_AdamW_20/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_AdamW_20/val_batch2_pred.jpg)
</details>

### yolov5n_AdamW_30
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_AdamW_30/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_AdamW_30/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_AdamW_30/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_AdamW_30/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_AdamW_30/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_AdamW_30/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_AdamW_30/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_AdamW_30/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_AdamW_30/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_AdamW_30/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_AdamW_30/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_AdamW_30/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_AdamW_30/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_AdamW_30/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_AdamW_30/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_AdamW_30/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_AdamW_30/val_batch2_pred.jpg)
</details>

### yolov5n_AdamW_40
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_AdamW_40/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_AdamW_40/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_AdamW_40/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_AdamW_40/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_AdamW_40/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_AdamW_40/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_AdamW_40/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_AdamW_40/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_AdamW_40/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_AdamW_40/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_AdamW_40/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_AdamW_40/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_AdamW_40/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_AdamW_40/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_AdamW_40/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_AdamW_40/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_AdamW_40/val_batch2_pred.jpg)
</details>

### yolov5n_Adam_20
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_Adam_20/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_Adam_20/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_Adam_20/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_Adam_20/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_Adam_20/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_Adam_20/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_Adam_20/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_Adam_20/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_Adam_20/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_Adam_20/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_Adam_20/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_Adam_20/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_Adam_20/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_Adam_20/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_Adam_20/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_Adam_20/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_Adam_20/val_batch2_pred.jpg)
</details>

### yolov5n_Adam_30
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_Adam_30/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_Adam_30/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_Adam_30/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_Adam_30/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_Adam_30/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_Adam_30/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_Adam_30/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_Adam_30/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_Adam_30/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_Adam_30/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_Adam_30/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_Adam_30/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_Adam_30/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_Adam_30/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_Adam_30/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_Adam_30/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_Adam_30/val_batch2_pred.jpg)
</details>

### yolov5n_Adam_40
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_Adam_40/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_Adam_40/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_Adam_40/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_Adam_40/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_Adam_40/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_Adam_40/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_Adam_40/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_Adam_40/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_Adam_40/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_Adam_40/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_Adam_40/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_Adam_40/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_Adam_40/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_Adam_40/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_Adam_40/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_Adam_40/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_Adam_40/val_batch2_pred.jpg)
</details>

### yolov5n_SGD_20
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_SGD_20/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_SGD_20/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_SGD_20/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_SGD_20/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_SGD_20/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_SGD_20/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_SGD_20/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_SGD_20/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_SGD_20/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_SGD_20/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_SGD_20/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_SGD_20/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_SGD_20/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_SGD_20/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_SGD_20/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_SGD_20/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_SGD_20/val_batch2_pred.jpg)
</details>

### yolov5n_SGD_30
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_SGD_30/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_SGD_30/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_SGD_30/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_SGD_30/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_SGD_30/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_SGD_30/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_SGD_30/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_SGD_30/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_SGD_30/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_SGD_30/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_SGD_30/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_SGD_30/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_SGD_30/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_SGD_30/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_SGD_30/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_SGD_30/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_SGD_30/val_batch2_pred.jpg)
</details>

### yolov5n_SGD_40
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov5n_SGD_40/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov5n_SGD_40/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov5n_SGD_40/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov5n_SGD_40/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov5n_SGD_40/confusion_matrix.png)
</details>

#### labels

<details>

![labels.jpg](docs/images/yolov5n_SGD_40/labels.jpg)
</details>

#### labels_correlogram

<details>

![labels_correlogram.jpg](docs/images/yolov5n_SGD_40/labels_correlogram.jpg)
</details>

#### results

<details>

![results.png](docs/images/yolov5n_SGD_40/results.png)
</details>

#### train_batch0

<details>

![train_batch0.jpg](docs/images/yolov5n_SGD_40/train_batch0.jpg)
</details>

#### train_batch1

<details>

![train_batch1.jpg](docs/images/yolov5n_SGD_40/train_batch1.jpg)
</details>

#### train_batch2

<details>

![train_batch2.jpg](docs/images/yolov5n_SGD_40/train_batch2.jpg)
</details>

#### val_batch0_labels

<details>

![val_batch0_labels.jpg](docs/images/yolov5n_SGD_40/val_batch0_labels.jpg)
</details>

#### val_batch0_pred

<details>

![val_batch0_pred.jpg](docs/images/yolov5n_SGD_40/val_batch0_pred.jpg)
</details>

#### val_batch1_labels

<details>

![val_batch1_labels.jpg](docs/images/yolov5n_SGD_40/val_batch1_labels.jpg)
</details>

#### val_batch1_pred

<details>

![val_batch1_pred.jpg](docs/images/yolov5n_SGD_40/val_batch1_pred.jpg)
</details>

#### val_batch2_labels

<details>

![val_batch2_labels.jpg](docs/images/yolov5n_SGD_40/val_batch2_labels.jpg)
</details>

#### val_batch2_pred

<details>

![val_batch2_pred.jpg](docs/images/yolov5n_SGD_40/val_batch2_pred.jpg)
</details>

</details>

# YOLOv7

<details>

### yolov7_std
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov7_std/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov7_std/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov7_std/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov7_std/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov7_std/confusion_matrix.png)
</details>

### yolov7_lr001
#### F1_curve

<details>

![F1_curve.png](docs/images/yolov7_lr001/F1_curve.png)
</details>

#### PR_curve

<details>

![PR_curve.png](docs/images/yolov7_lr001/PR_curve.png)
</details>

#### P_curve

<details>

![P_curve.png](docs/images/yolov7_lr001/P_curve.png)
</details>

#### R_curve

<details>

![R_curve.png](docs/images/yolov7_lr001/R_curve.png)
</details>

#### confusion_matrix

<details>

![confusion_matrix.png](docs/images/yolov7_lr001/confusion_matrix.png)
</details>

</details>
