import os
import yaml

yaml_path = "path/to/your/yaml"
label_lst = ["signboard"]

data_dict =
{
    
    'train': '/path/to/your/train'
    'test': '/path/to/your/test'
    'val': '/path/to/your/val'
    'nc': len(label_lst) #number of class
    'name': label_lst
}

with open(yaml_path, 'w') as f:
    yaml.dump(data_dict, f, sort_keys=False)

print("Completed")