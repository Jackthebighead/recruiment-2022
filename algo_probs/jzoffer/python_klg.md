### python语法记录

- 代码中经常有三中方式判断变量是否为None，主要有三种写法:
(1) if x is None:
(2) if not x:
(3) if not x is None:
在python中None,False,空字符串，空列表，空字典，空元组都相当于False。
但在使用列表的时候，x=[]时，x is None 为False，not x 为True。当x=None时反之。
综上，使用is not None判断最好
<br>

- [0,0,0,0,0]
  - [0] * 5
  - [0 for _ in range(5)]
<br>

- 列表
  - list
  - 可以用来构建各种基于线性表的数据结构，栈，队列，等
  - list的pop(0)的复杂度高于pop()，因为python在底层对pop的实现是，若pop一个元素，后序操作是改变pop后所有元素的index，即如果pop第一个元素，那么剩下所有元素的index都得-1，所以worst case 时间复杂度是O(n)。这是一个tradeoff因为这样的机制让python list的index函数是O(1)复杂度。
<br>

- 字典使用
  - a = dict()
  - a.get(key)
  - dict.get(key, default=None), default的意思是当该键的值不存在的时候用default代替
  - 字典查找最大值的键:
    - max(dict, key=lambda x: d[x])
    - max(dict, key=d.get)
    - import operator
      max(dict, key=operator.itemgetter(d)) 
      - python的itemgetter：用于获取对象的哪些维的数据。返回一个函数，将函数作用在一个对象上才能获取值
        - itemgetter经常用在类似sorted函数的key参数中
        - 比如sorted(x,key=itemgetter(1,2),reverse=False)代表正序，按照x的第二个排序，若第二个相同则按照第三个排序
  - Python 3.6 后，默认字典就是有序的，因此无需使用 OrderedDict()
  - python中的dict实际上是哈希散列表，查找的时间是O(1)。首先python计算处key的hash值，再经过与等操作得到在哈希表中的index值，查表，若占用比较key，若不相同则hash冲突，再散列。若相同则更新value。
    - 不好之处是经过这一系列变换的操作，哈希表会稀疏。
    - 在新版python中好像微改了index的意义，index变成了字典的辅助indices表中的下标位置，改下标位置在indices表中存的是该值在哈希表中的位置（len(hash_table，是+1递增的）。
      - 这样的好处是哈希表不会稀疏，而indices表是稀疏的，因此哈希表的存储是随着插入操作而有序的，古在3.6版本后，dict也是有序的了。但空间占用更大。
    - dict类的哈希法是以空间换时间。 
    - python中list的存储结构是线性表，线性表的查找需要一个一个找O(n)。Python中的列表存放的不是值而是地址。
    - 解决hash冲突的算法是决定dict结构的时间复杂度的重要一环。
<br>

- 字符串str
.replace(old,new)
字符串添加: +
<br>

- 列表list
.append()
.pop(index)
.insert(pos, obj)
''.join(list): 字符串列表转字符串。join在python3中代表将list的每个元素之间用''链接
<br>

- math.pow()比**算的更快
<br>

- python的运算符：https://www.runoob.com/python/python-operators.html
python的位运算符，按位运算符是把数字看作二进制来进行计算的。& | ^ ~ << >>分别表示按位与，或，异或，取反，向左移动，高位丢低位补
特别的，对于二进制：n&1（与操作）：判断 nn 二进制最右一位是否为 1；n>>1（移位操作）：n 右移一位（可理解为删除最后一位）。
<br>

- python的字符串
python输入的是int的10进制整数，所以若要转换成2进制，可以用bin()函数转换为二进制的字符串
字符串的操作函数有：
  - string.lower()， string.lower()
  - string.count(str, beg=0, end=len(string))：count('x')函数统计x，beg和end范围内的个数
  - string.find(str, beg=0, end=len(string))
  - string.endswith(obj, beg=0, end=len(string))：检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
  - string.isnumeric()： 是否只包含数字字符
  - string.join(seq)：字符串合并
    - ''.join(list): 字符串列表转字符串。join在python3中代表将list的每个元素之间用''链接
  - string.partition(str)：有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
  - string.replace(str1, str2,  num=string.count(str1))：把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次
  - string.split(str="", num=string.count(str))：以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串
  - string.strip([obj])：截掉空格
<br> 

- python平行赋值的原理：
Python 利用平行赋值的写法（即 a, b = b, aa,b=b,a ），可省略暂存操作。其原理是先将等号右侧打包成元组 (b,a)(b,a) ，再序列地分给等号左侧的 a, ba,b 序列。
<br>

- python的正则表达式
  - 正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
  - 正则表达式 r'xxxx'
    - re regex包都是python正则表达式的包，其中regex包含re。
    - \s是匹配任何空白，比如空格或TAB键
    - 匹配[ ]中列举的字符 
  - import re，re有12类
  - flag是匹配方式，值有以下几种形式，default是flag=0
      - re.l: 匹配对大小写不敏感
      - re.M: 多行匹配，影响\^和$。当某字符串中有换行符\n，默认模式下是不支持换行符特性的。在单行模式下\^匹配行开头，如果字符串内有\n那么\^匹配不到\n之后的，切换到多行模式则没有问题。
      - re.S: 让.匹配包括换行符在哪的所有字符（一般.不匹配换行符\n）
      - re.A: 让模式只匹配ASCII码
      - re.DEBUG: 编译的时候现实debug信息
  - 第一类：查找一个匹配项
    - re.match(pattern, string, flags=0)
      - re.match：从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none，匹配成功返回一个匹配对象。
    - re.search()：查找任意位置的匹配项
    - re.fullmatch()：整个字符串和正则完全匹配，不匹配返回None
    - 用.group()返回匹配结果（group内加数字可以返回对应部分）
  - 第二类：查找多个匹配项
<br>

- python的工具类：collections
  - 双端队列(double ended queue)
    - from collections import deque
    - Python 中使用collections中的双端队列deque()，其popleft()方法可达到O(1)时间复杂度；列表list的pop(0)方法时间复杂度为O(N)。
    - 方法：
      - insert(index, x): 插入元素到指定位置 
      - remove(x)
      - reverse(): 翻转
      - append(x), appendleft(x): 添加元素
      - extend(x), extendleft(x): 添加一组元素，其中x是一组元素，i.e.一个列表
      - pop(), popleft(): 弹出
      - count()
      - rotate(n): 从尾部旋转到首部，若为负数则是从首部旋转到尾部
    - 黑科技：
      -  支持x in queue语法
      -  支持.copy()语法
  -  缺省字典
     - from collections import defaultdict
     - 因为普通的dict={}若查找的element不在字典里会报错，defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值。
     - 方法 
       - dict =defaultdict(factory_function)，其中factory_function是list、set、str等，list对应[ ]，str对应的是空字符串，set对应set( )，int对应0。
     - 例子:
     - ```python from collections import defaultdict
        s = 'mississippi'
        d = defaultdict(int)
        for k in s:
            d[k] += 1
        print(d)
  - 有序字典
    - from collections import OrderedDic 
    - 字典dict是无序的，按照hash存储不能顺序输出，如果我们想要有序的dict（比如按照插入时间有序），可以使用OrdereDict。  
    - 方法
      - dict.popitem(last=True): 移除最后（先进后出）一个key-value对。
      - dict.move_to_end('key', last=True)将指定key-value移动到最前/后。
    - 例子：
    - ```python
        from collections import OrderedDict
        d={'b':3,'a':4,'c':2,'d':1}
        # 将d按照key来排序
        OrderedDic(sorted(d.items(),key=lambda t:t[0]))
        # 返回OrderedDic([('a',4),('b',3),('c',2),('d',1)])
        # 按照value来排序
        OrderedDict(sorted(d.items(),key=lambda t:t[1]))
        # 返回OrderedDic([('d',1),('c',2),('b',3),('a',4)])
        # 按照key的长度来排序
        OrderedDic(sorted(d.items(),key=lambda t:len(t[0])))
    - 其中sort(iteration, key, reverse)：参数分别是可迭代对象，选取对象中参与比较的元素，是否倒叙
<br>

- python **zip**函数
  - zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
  - 比如一个matrix: list[list]:[[1,2],[3,4]\], res = zip(*matrix)意味着变成[(1,3),(2,4)\]，此时再list(res)[::1]就得到[[2,4],[1,3]\]，实现翻转90度。
    - 上面的方法也可以让list中list类型的矩阵翻转任意角度
<br>

- python的运算符
  - python的比较运算符优先级大于逻辑运算符
  - python的布尔变量，只有为0才为False其余都是True
  - python的and是有顺序的，只要第一个False就是False不会看第二个
  - python的or也是有顺序的
<br>

- python的拷贝
  - 设a = [1, 2, ['a','b']]，变量a指向这个list对象（的地址）
  - python拷贝分三种
    - 直接赋值：
      - b = a
      - b也指向a的引用，即b也指向这个list在内存中的位置
    - 浅拷贝:
      - 切片函数[:], 工厂函数(list(),dict()set()), copy.copy()
      - e.g. b = list(a)
      - 浅拷贝中b指向拷贝后的list对象，但b指向的list对象内部的子对象，比如1，2，['a','b']就是a指向的对象中的子对象。即浅拷贝拷贝父对象，不会拷贝对象的内部的子对象。 
      - 所以修改a[2].append(x)，b[1]也会修改。但a.append(x)，不会改变b
    - 深拷贝：
      - copy.deepcopy()
      - 深拷贝完全拷贝了父对象及其子对象
      - e.g. b = copy.deepcopy(a)
      - b指向的list和list内部的子对象（元素）都和a对应的不一致。
      - 所以修改a[2].append(x)，或a.append(x)，都不会改变b。
    - 浅拷贝: a!=b, a[1]==b[1]
    - 深拷贝: a!=b, a[1!]=b[1]
<br>

- python中sort()是list数据结构专用的函数，在原list上操作, l.sort(); l....
  - sorted()是针对所有可迭代对象，返回一个新的对象。l = sorted(l)

