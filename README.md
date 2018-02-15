# machine-learning

```
python ./resize_image.py --source_dir=images/jobs/train --target_dir=target/train --img_width=28 --img_height=28
```

```
python ./pickle_images.py --img_source_dir=target/train --classes_map_file=class_mapping.json --data_file=data/sample.pkl
```

```
python ./multi_classifier.py --mode train --classes 1 --steps 300 --model_dir=model/ --data_set=data/sample.pkl
```

```
python ./multi_classifier.py --mode eval --classes 1 --model_dir=model/ --data_set=data/sample.pkl
```

```
python ./multi_classifier.py --mode test --classes 2 --model_dir model/
```

