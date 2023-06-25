import fiftyone as fo
import fiftyone.zoo as foz

# Download and load the validation split of COCO-2017
dataset = foz.load_zoo_dataset(name="coco-2017",
                               split="train",
                               dataset_dir='/data',
                               )

session = fo.launch_app(dataset)