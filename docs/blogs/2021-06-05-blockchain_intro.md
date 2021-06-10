

# 用最通俗的方式聊聊区块链和比特币

近期因为虚拟货币价格大起大落，和其相关的话题，例如比特币，区块链等等又一次吸引了大家的注意。例如从谷歌趋势（google trends）里得到的数据来看，"比特币"的全球搜索热度从2020年底起和它的价格一样"一飞冲天"，"区块链"相关的搜索量也随之飙升。

![比特币趋势](https://user-images.githubusercontent.com/54601170/121392960-71604c80-c982-11eb-8015-f547e6e9262c.PNG)
![区块链趋势](https://user-images.githubusercontent.com/54601170/121393082-9228a200-c982-11eb-9ee6-37f65623e2c2.png)

看来人们除了想了解比特币行情以外，越来越多的人也想弄清楚究竟什么是区块链。作为对区块链一直很感兴趣的我也不例外。坦白的说，之前我对这一概念的理解只停留在"我的一个朋友告诉我区块链是XXX"的阶段，所以总觉得它神乎其神。最近因为实在想在近期"试水"币圈，所以下决心要好好弄清楚区块链，虚拟货币等等概念，争取做一名"死也瞑目"的韭菜。接下来我就想用最通俗的语言，介绍下我对区块链的理解，并且分享下如何尝试用Python代码实现一个简单的加密货币应用。

## 什么是区块链？

在解释区块链之前，我还想先聊聊区块链最初被发明出来的目的。区块链最早由计算机科学家于1991年提出，用于给文档打上时间戳。时间戳的记录对所有相关人员开放，一旦文档里的内容被修改，时间戳也会跟着变化，有关人员就知道该文档被修改过了。

2009年，一个（网）名叫中本聪的人，发布了一种点对点电子货币系统的白皮书，提出了一种不需要借助第三方机构，也可以避免双重支付问题（双重支付问题会在下面的文章中举例介绍），实现个人对个人交易的支付系统，也就是后人熟知的比特币。区块链（chain of blocks）的概念从此进入了大众的视野。比特币可能是区块链影响力最大的的早期应用之一， 区块链概念的成熟与比特币的关系密不可分，所以下文中如果有聊到比较抽象难以理解的概念时，可能会用比特币列举，希望能有助于大家理解~

ok，下面进入正题：

区块链，就是由一组包含信息的区块组成的链条。每一个区块大致包含以下三个内容：该区块的哈希值（可以理解成一个区块的"指纹"），上一个区块的哈希值，以及这一个区块里所存储的数据。学过数据结构的同学可能会感觉这和链表非常相似——没错，我一开始也是这么理解的。与链表不同的是，区块的哈希值是在该区块**创建**时，根据这个区块存储的数据信息和上一区块的哈希值一起作为输入生成的。这样一来区块链和链表不同的地方就体现出来了：在区块链里如果任何一个中间区块（block_K）的信息发生了改变，block_K就不再是之前的block_K了（哈希值改变了），又因为下一区块会存储前一区块的哈希值，链中任意区块的变化都能通过简单的哈希值校验来发现。

![区块链结构示意](https://user-images.githubusercontent.com/54601170/121362569-c3947400-c968-11eb-8928-05b4d9332a54.png)

这样一来，如果要修改存储在某个区块链里的信息，同时确保区块链的完整合理，则需要重新计算该区块后面所有区块的哈希值。因此在区块链中修改的记录都是"有迹可循"的。

### 共识机制

目前有了区块这种存储结构，拥有这个区块链的本人可以知道区块链里的信息是否有修改，但是如何让别人也能够验证呢？

为什么会有这样的问题？我们可以拿比特币举个栗子：比特币中区块存储的是账本信息（可以理解成很多转账记录，例如A支付给B 10块钱）。由于没有银行这种第三方机构，也没有实体的货币（如纸币），为了让转账生效，方法之一是让尽可能多的人作为见证者去验证这一转账，当这个转账被大多数人验证真实后，A如果想再用同样的10块钱支付给C以换取东西，并且把这笔交易广播给见证者们，见证者们就会提出这笔转账不合理。A的这类行为即为双重支付，这种通过判定足够数量的用户是否达成共识来验证的机制叫做"共识机制"。

回到最初的问题：把交易广播出去以后，如何让别人验证转账呢？比特币是这样实现的：让每个人都拥有一份完整的区块链账本，有人想要修改账本时候，其他人只需要验证修改的账本和自己已有的账本是否一致就可以，只要大多数人投反对票，那么这个账本的修改就会被作废了。

然而即使这样，如果想要篡改记录的攻击者无限制地发送虚假区块给他人验证，也会对整体网络其他帮助验证人（节点）造成资源的浪费。为了解决这一问题，比特币提供的方法是增加区块创建的时间成本、计算成本，这样即使有不怀好意的攻击者，攻击者篡改的成本大大增加，对全网其他的影响也大大减少，这也被称做工作量证明机制（proof of Work）。


### 工作量证明机制

在比特币中工作量证明是如何实现的呢？

我们知道，哈希算法类似于将一个简单输入值x，通过一个很复杂的函数（散列函数），计算出哈希值y。也就是

$f(x) = y$

其中，$f(x)$ 可以想象成是比$x^2+\sqrt{x}-\int ^4_3 \sum ^x_3 \frac{1}{x^2}{\rm d}x$ 复杂的多的公式。计算机通过$x$可以很容易解出$y$，但是如果知道$y$想要得到$x$几乎不可能。

如果人类给出一个$y$，让计算机根据函数反推x，计算机只能通过用一个个不同的$x$暴力尝试出刚好能计算出y的答案。在散列函数中，这对于计算机来说是个不可能完成的任务。所以为了控制难度，可以给计算机一个合适的答案范围，例如让计算机凑出前缀有4个0(格式类似'0000XXXXX')的散列函数。这样也许通过计算机的几千次尝试，可以找到符合条件的"$x$"。答案范围越小，计算机需要尝试的次数就越多，修改区块链需要的开销就越大。

以下是一个简单的代码实现:

```python
# We want the hash value starts with '00000'
difficulty = 5
answer = '0'*difficulty

def compute_hash(data,nonce):
    return sha256((data+str(nonce)).encode()).hexdigest()

data = '123'
nonce = 1 # data to change

# init hash_value    
hash_value = compute_hash(data,nonce)

# change nonce recursively until hash_value begins with the answer.
while hash_value[:difficulty] != answer:
    nonce += 1 
    hash_value = compute_hash(data,nonce)


print('tryout times:',nonce)
print('hash_value:',hash_value)


```
输出：
```
tryout times: 96064
hash_value: 00000bdebc0a945fcd1a1b6127267393dfc299c89b031b7879d926a32921e9f6
```

可以看到，计算机尝试了96064个不同的nonce值才让哈希值的前N位数符合我们的答案。

在比特币区块链中，产生一个区块平均时间在10分钟左右，同时考虑到全网算力的提升，比特币会通过提高难度（减小答案范围）的方式，让目前一个区块产生的平均时间不会因为算力的提升增长，甚至每隔一段时间比特币的产量会减半。


## 区块链有那些应用方向？

除了虚拟货币以外，区块链技术其实还有大量应用场景，习大大也曾强调"区块链技术的集成应用在新的技术革新和产业变革中起着重要作用"。一方面，只要是记录都可以保存在区块链中，例如可以存储税务信息，医保信息，食品溯源信息，甚至健康码的背后也是区块链技术的加持。另一方面，去中心化的概念和物联网也十分契合，依托物联网部署区块链，同时皆有区块链实现对数据的安全传输。如去中心化的无线通信网络，去中心化的云服务和数据交换服务等等。


## 代码实现简单的加密货币

为了更深地理解区块链，我参考了网上一些资料，简单地写了Python实现的区块链货币，供大家参考和理解:
```python
from hashlib import sha256
import time
import json
import logging
from typing import Dict, List
import rsa


# block + chain
class Block():
    def __init__(self, transactions: List, prev_hash):
        # transaction -> list of objects
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.nonce = 1  # use for mining
        self.timestamp = time.time()
        self.hash = self.compute_hash()

    def __repr__(self):
        return f"{self.transactions}"

    def compute_hash(self):
        block_string = "{}{}{}{}".format(json.dumps(
            self.transactions), self.prev_hash, str(self.nonce), self.timestamp)
        return sha256(block_string.encode()).hexdigest()

    def validate_transaction(self):
        for transaction in self.transactions:
            if not transaction.is_valid():
                return False
            else:
                return True

    def mine(self, difficulty: int):
        if not self.validate_transaction():
            raise Exception('Abnormal transaction found, abort.')

        answer = '0'*difficulty

        while self.hash[:difficulty] != answer:
            self.nonce += 1
            self.hash = self.compute_hash()

        print(f'Finished mining, tryout times:{self.nonce}')


class Transaction(Dict):
    def __init__(self, payer, payee, amount):
        self.update(payer=payer)
        self.update(payee=payee)
        self.update(amount=amount)
        # self.timestamp = timestamp
        self.update(hash=self.compute_hash())

    def __repr__(self):
        return json.dumps(self)

    def sign(self, private_key):
        self.signature = rsa.sign_hash(
            hash_value=self['hash'].encode("utf-8"),
            priv_key=private_key,
            hash_method='SHA-256')

    def is_valid(self):
        if not self['payer']:
            return False

        else:
            # 这里由于没有引入数字签名，暂不验证
            return True

    def compute_hash(self):
        Transaction_string = "{}{}{}".format(
            self['payer'], self['payee'], self['amount'])
        return sha256(Transaction_string.encode()).hexdigest()


class BlockChain():
    def __init__(self, difficulty):
        self.chain = [self.create_genesis()]
        self.transactionPool = []
        self.Reward = 1
        self.difficulty = difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def create_genesis(self) -> Block:
        genesis_block = Block(transactions=[], prev_hash=0)
        return genesis_block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block_to_chain(self, new_block: Block):
        if new_block.hash[:self.difficulty] == '0'*self.difficulty:
            new_block.prev_hash = self.get_latest_block().hash
            self.chain.append(new_block)
            print(f" a new block added to blockchain.")
        else:
            print('block validation failed.')

    def validate_chain(self):
        if len(self.chain) == 1:
            return self.chain[0].compute_hash() == self.chain[0].hash

        # validate block
        for i in range(1, len(self.chain)):
            block_to_validate = self.chain[i]

            # validate transactions in block
            if not block_to_validate.validate_transaction():
                logging.error('Fraud transactions!')
                return False

            # validate data in this block hasn't been tampered
            elif not block_to_validate.hash == block_to_validate.compute_hash():
                logging.error(
                    f'Data has been tampered! \n this hash:{block_to_validate.hash} \n computed hash:{block_to_validate.compute_hash()}')
                return False

            # validate block.prev_hash == previous block.hash
            elif not block_to_validate.prev_hash() == self.chain[i-1].hash:
                logging.error('Chain broke!')
                return False

            else:
                return True
    pass
```

看一些输出：
```
# test
# 创建区块链，同时生成创始区块
blockchain = BlockChain(4)

# 这里需要用公钥给payer,payee赋值，用payer的密钥给交易"签名"，但因为没有介绍暂不使用
transaction1 = Transaction(payer='Paparazzi', payee='Elephant', amount='666')

transaction2 = Transaction(payer='Elephant', payee='Sylar', amount='100')

# add one block to chain
block1 = Block(
    transactions=[transaction1],
    prev_hash=blockchain.get_latest_block().hash)
block1.mine(difficulty=4)
blockchain.add_block_to_chain(block1)
print(f"hash of block1: {block1.hash}")

# add another block to chain
block2 = Block(
    transactions=[transaction2],
    prev_hash=blockchain.get_latest_block().hash)
block2.mine(difficulty=5)
blockchain.add_block_to_chain(block2)
print(f"hash of block2: {block1.hash}")

# Output:
Finished mining, tryout times:222523
 a new block added to blockchain.
hash of block1: 0000d7f7e1018f498431eefa24faf7ab6b8ec9c42ecf89d1039939f8f74c15d5
Finished mining, tryout times:1321891
 a new block added to blockchain.
hash of block2: 0000018c800c81b750dae4785652efc679929177c6fed9b0d268627f038dde1c
```

```
print(f"previous hash of last block:{blockchain.chain[-1].prev_hash}")
print(f"hash of second last block:{blockchain.chain[-2].hash}")

# Output:
previous hash of last block:0000c245596fd46a0a8b80e8c2f84efb7f19b077a1a61881260f95dc6098d57a
hash of second last block:0000c245596fd46a0a8b80e8c2f84efb7f19b077a1a61881260f95dc6098d57a
```
参考资料：

Bitcoin: A Peer-to-Peer Electronic Cash System; 2009; Satoshi Nakamoto; https://bitcoin.org/bitcoin.pdf

科普短片：区块链如何工作？  bilibili.com

程序员手把手带你搭建一个简单易懂的区块链 bilibili.com

