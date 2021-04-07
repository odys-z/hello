'''
   0 About
   -------

   This is a slightly modified exercises of https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html ,
   - suppose we have images with two classes of labels, machine & animal, for
   suppervised learning.

    loaded labels:
    --------------

        # classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
        # machine: 0, 1, 8, 9; animal: 2, 3, 4, 5, 6, 7
        classes = ('machine', 'animal')
        labels = torch.tensor([ 0 if x <= 1 or x >= 8 else 1 for x in labels ])

    output:
    -------

        Variable._execution_engine.run_backward(
        [1,  2000] loss: 0.522
        [1,  4000] loss: 0.321
        [1,  6000] loss: 0.296
        [1,  8000] loss: 0.281
        [1, 10000] loss: 0.268
        [1, 12000] loss: 0.268
        [2,  2000] loss: 0.262
        [2,  4000] loss: 0.254
        [2,  6000] loss: 0.249
        [2,  8000] loss: 0.245
        [2, 10000] loss: 0.238
        [2, 12000] loss: 0.243
        Finished Training
        Predicted:  machine /  animal /  animal /  animal
        Accuracy of the network on the 10000 test images: 90 %
        Accuracy of machine : 81 %
        Accuracy of animal : 95 %
        Segmentation fault (core dumped)
'''
import torch
import torchvision
import torchvision.transforms as transforms

import matplotlib.pyplot as plt
import numpy as np

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

'''
    1. Loading and normalizing CIFAR10
    ----------------------------------
'''
def imshow(img):
    '''
    functions to show an image
    '''
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    # plt.show()
    # https://stackoverflow.com/a/58181952
    plt.savefig("t04.png")

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)

# classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
# machine: 0, 1, 8, 9; animal: 2, 3, 4, 5, 6, 7
classes = ('machine', 'animal')

# get some random training images
dataiter = iter(trainloader)
images, labels = dataiter.next()

# show images
imshow(torchvision.utils.make_grid(images))
# print labels
print(' '.join('%7s' % classes[0 if labels[j] <= 1 or labels[j] >= 8 else 1] for j in range(4)))


'''
    2. Define a Convolutional Neural Network
    ----------------------------------------
'''
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()

'''
    3. Define a Loss function and optimizer
    ---------------------------------------
'''
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

'''
   4. Train the network
   --------------------
'''
for epoch in range(2):  # loop over the dataset multiple times
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        labels = torch.tensor([ 0 if x <= 1 or x >= 8 else 1 for x in labels ])
        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Finished Training')

PATH = './cifar_net_2.param'
torch.save(net.state_dict(), PATH)
net.load_state_dict(torch.load(PATH))
outputs = net(images)

_, predicted = torch.max(outputs, 1)
print('Predicted: ', ' / '.join('%7s' % classes[predicted[j]]
                              for j in range(4)))


'''
    5. Test the network on the test data
    ------------------------------------
'''
correct, total = 0, 0
with torch.no_grad():
    for data in testloader:
        images, labels = data

        labels = torch.tensor([ 0 if x <= 1 or x >= 8 else 1 for x in labels ])

        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))

class_correct = list(0. for i in range(10))
class_total = list(0. for i in range(10))
with torch.no_grad():
    for data in testloader:
        images, labels = data

        labels = torch.tensor([ 0 if x <= 1 or x >= 8 else 1 for x in labels ])

        outputs = net(images)
        _, predicted = torch.max(outputs, 1)
        c = (predicted == labels).squeeze()
        for i in range(4):
            label = labels[i]
            class_correct[label] += c[i].item()
            class_total[label] += 1


for i in range(2):
    print('Accuracy of %5s : %2d %%' % (
        classes[i], 100 * class_correct[i] / class_total[i]))
