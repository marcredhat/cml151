#https://docs.activeloop.ai/getting-started/deep-learning/creating-datasets-manually
#https://github.com/activeloopai/deeplake
import deeplake
import torch
from torchvision import transforms, models


import deeplake
from PIL import Image
import numpy as np
import os

#If you want to create a new empty dataset, either 
#specify another path or use overwrite=True. 
#If you want to load the dataset that exists at this path, 
#use deeplake.load() instead.

#ds1 = deeplake.empty('./animals_deeplake') # Create the dataset locally
ds1 = deeplake.load('./animals_deeplake') # Create the dataset locally


# Find the class_names and list of files that need to be uploaded
dataset_folder = './animals'

# Find the subfolders, but filter additional files like DS_Store that are added on Mac machines.
class_names = [item for item in os.listdir(dataset_folder) if os.path.isdir(os.path.join(dataset_folder, item))]

files_list = []
for dirpath, dirnames, filenames in os.walk(dataset_folder):
    for filename in filenames:
        files_list.append(os.path.join(dirpath, filename))


with ds1:
    # Create the tensors with names of your choice.
    ds1.create_tensor('images1', htype = 'image', sample_compression = 'jpeg',exist_ok=True)
    ds1.create_tensor('labels1', htype = 'class_label', class_names = class_names)
    
    # Add arbitrary metadata - Optional
    ds1.info.update(description = 'My first Deep Lake dataset')
    ds1.images.info.update(camera_type = 'SLR')
    

with ds1:
    # Iterate through the files and append to Deep Lake dataset
    for file in files_list:
        label_text = os.path.basename(os.path.dirname(file))
        label_num = class_names.index(label_text)
        
        #Append data to the tensors
        ds.append({'images': deeplake.read(file), 'labels': np.uint32(label_num)})
        
Image.fromarray(ds1.images[0].numpy())


ds1.summary()


ds1.tensors.keys()    # dict_keys(['images', 'labels'])
ds1.labels[0].numpy() # array([6], dtype=uint32)



tform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
])

deeplake_loader = ds.pytorch(num_workers=0, batch_size=1, transform={
                        'images': tform, 'labels': None}, shuffle=True)


net = models.resnet18(pretrained=False)
net.fc = torch.nn.Linear(net.fc.in_features, len(ds.labels.info.class_names))
    
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)


for epoch in range(2):
    running_loss = 0.0
    for i, data in enumerate(deeplake_loader):
        images, labels = data['images'], data['labels']
        
        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(images)
        loss = criterion(outputs, labels.reshape(-1))
        loss.backward()
        optimizer.step()
        
        # print statistics
        running_loss += loss.item()
        #if i % 100 == 99:    # print every 100 mini-batches
        print('[%d, %5d] loss: %.3f' %
        (epoch + 1, i + 1, running_loss / 100))
        running_loss = 0.0






