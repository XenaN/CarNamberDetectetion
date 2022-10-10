# CarNumberDetection

This project is experiment with yolo for detecting car numbers on dataset *nomeroff*, which is the most complete for numbers from several coutries. 
Dataset you can load [here](https://nomeroff.net.ua/datasets/). Choose *autoriaNumberplateDataset-2022-08-01* 

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

PS: if you want to pass train stage, load [weights](https://drive.google.com/file/d/1B1XhgSm56yyJch8oecdDtbb4qdJa496g/view?usp=sharing) and put it to yolov7 folder (check that yolov7 is loaded as submodule)

```bash
dvc repro test --single-item
dvc repro recognize --single-item
```

## DVC Dag
DVC pipline contains several steps:
* preparation datasets into coco data format
* creation test datasets
* creation lists of images (yolo requirements)
* creation yolov5 and yolov7 configs
* train (you should choose stage accoding to version of yolo)
* test (only for yolov7, test for yolov5 is inside train part)
* recognize letters from number plate, which was detected by yolo. Here we use tesseract.

For yolov7 you can see dag for pipline 

![image](docs/images/other/image_2022-10-04_23-05-45.png)


# Learning process screenshot
Training part looks like this

![image](docs/images/other/image_2022-10-04_22-38-37.png)


# Experiments
We conducted several experiments.
At first we choose the most used version of yolo - 5 and the newest version - 7.
Then we change several hypetparameters: learning rate, epochs, optimizers.

We compared models by metrics Precision, Recall, mAP50 as the most useful for detection problem. 

Common params were batch size 4, image size 640

| Model  | Changed Parameters | P | R | mAP50 |
| ------------- | ------------- |------------- |------------- |------------- |
|  Yolov5m   |  Adam; 20 epochs | 0.991 | 0.962 | 0.988 |
|  Yolov5m   |  Adam; 40 epochs  | 0.985 | 0.961 | 0.984 |
|  Yolov5m   |  SGD; 20 epochs  | 0.991 | 0.962 | 0.988 |
|  Yolov5n   |  Adam; 20 epochs | 0.988 | 0.958 | 0.981 |
|  Yolov5n   |  Adam; 40 epochs | 0.985 | 0.961 | 0.984 |
|  Yolov5n   |  SGD; 20 epochs  | 0.988 | 0.958 | 0.981 |
|  Yolov7n   |  40 epochs  | 0.978 | 0.943 | 0.977 |
|  Yolov7n   |  40 epochs; lr=0.001  | 0.988 | 0.965 | 0.989 |

# Speed
For Intel Core i7-9750H 2.60GHz 

GPU - NVIDIA GeForce RTX 2060

(WSL)

Yolov7 - 0.23 s

Yolov5 - 0.17 s

## License

BiFolio is licensed under the MIT License. See [LICENSE](LICENSE) for the full license text.
