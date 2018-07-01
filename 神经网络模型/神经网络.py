import pybrain
import csv
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, TanhLayer, FullConnection
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

def netBuild(ds):
    #net = buildNetwork(8, 13,13,13, 1)

    # 建立神经网络fnn
    fnn = FeedForwardNetwork()

    # 设立三层，一层输入层（3个神经元，别名为inLayer），一层隐藏层，一层输出层
    inLayer = LinearLayer(8, name='inLayer')
    hiddenLayer0 = TanhLayer(13, name='hiddenLayer0')
    hiddenLayer1 = TanhLayer(13, name='hiddenLayer1')
    hiddenLayer2 = TanhLayer(13, name='hiddenLayer2')
    outLayer = LinearLayer(1, name='outLayer')

    # 将五层层都加入神经网络（即加入神经元）
    fnn.addInputModule(inLayer)
    fnn.addModule(hiddenLayer0)
    fnn.addModule(hiddenLayer1)
    fnn.addModule(hiddenLayer2)
    fnn.addOutputModule(outLayer)

    # 建立五层之间的连接
    in_to_hidden = FullConnection(inLayer, hiddenLayer0)
    hidden_to_hidden0 = FullConnection(hiddenLayer0, hiddenLayer1)
    hidden_to_hidden1 = FullConnection(hiddenLayer1, hiddenLayer2)
    hidden_to_out = FullConnection(hiddenLayer2, outLayer)

    # 将连接加入神经网络
    fnn.addConnection(in_to_hidden)
    fnn.addConnection(hidden_to_hidden0)
    fnn.addConnection(hidden_to_hidden1)
    fnn.addConnection(hidden_to_out)

    # 让神经网络可用
    fnn.sortModules()

    print("Trainging")
    trainer = BackpropTrainer(fnn, ds, verbose=True, learningrate=0.01)
    # trainer.train()
    trainer.trainUntilConvergence(maxEpochs=500)
    print("Finish training")
    return fnn

def readData(path):
    reader = csv.reader(open(path, 'rt'))
    data = []
    for line in reader:
        data.append((float(line[1]),float(line[2]),float(line[3]),float(line[4]),float(line[5]),float(line[6]),float(line[7]),float(line[8]),float(line[0])))
    return data



def dsBuild(data):
    ds = SupervisedDataSet(8, 1)
    for ele in data:
        ds.addSample((ele[0],ele[1],ele[2],ele[3],ele[4],ele[5],ele[6],ele[7]),(ele[8]))
    dsTrain,dsTest = ds.splitWithProportion(0.7)
    return dsTrain,dsTest


dsTrain,dsTest = dsBuild(readData(path='model.csv'))
netModel = netBuild(dsTrain)
#dsTest = dsTrain
#pred=[]
for i in range(0,len(dsTest['input'])):
    error = dsTest['target'][i]-netModel.activate((dsTest['input'][i][0],dsTest['input'][i][1],dsTest['input'][i][2],dsTest['input'][i][3],dsTest['input'][i][4],dsTest['input'][i][5],dsTest['input'][i][6],dsTest['input'][i][7]))
    print(error)


