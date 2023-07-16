# DC-YOLO

This repository is build based on the paper DC-YOLO which is not yet published.
We will add the paper address when the paper is published.

#### Download the dataset, and set the directory like this :
    --datasets
        --coco
        --VOC
    --DC-YOLO
        ...
        ...

Install the envirment:
``` sh
cd DC-YOLO
pip install -r requirements.txt
```

To training DC-YOLO_s on coco dataset, run :
```sh
python train.py --data coco.yaml --epochs 100 --weights None --cfg DC_S.yaml  --batch-size 64
```
To test your results, run :

``` sh
python val.py --weights runs/train/best.pt --data coco.yaml --img 640
```
