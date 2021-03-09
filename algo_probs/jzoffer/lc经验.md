- 先考虑边界情况，如if not obj

- 对于动态规划问题，先确定状态，想象一个状态数组，写出状态方程，再分析边界情况

- 用数据结构解决，比如栈，双栈，堆，队列等

- dfs和bfs
  - dfs主要用递归，或者暴力for来代替dfs
  - bfs主要用队列，while迭代

- 对于python的大数越界问题，虽然python的大数可以不考虑，但若要考虑可以考虑转换成字符串问题

- lc问题种类：
  - 数学问题
    - 约瑟夫环问题 
      - 一群人从0:n-1围着做，杀一个人，被杀的人下一个开始计0:n-2，计算最后一个剩下的人初始时候的坐标。
        - 用列表代替环，环结构用%运算来实现。这是一个动态规划问题，已知幸存者最后（当环内只剩下它一个人）的坐标0，逆推在n-1人的环中的位置。但我们在讨论的时候需要从n-1推到0，从n-1到n-2可发现之后的坐标是（之前坐标-m）%（n-1+1）即f(n-1)=(f(n)-m) % n，n即len(环)，所以我们有f(n)=(f(n-1)+m)%n。
  - 数据结构问题
    - 定义数据结构实现函数功能
      - 注意函数功能的时间复杂度要求
      - 应用额外指针，额外数据结构，一个或多个基础数据结构来实现功能
      - e.g. 用额外队列实现队列数据结构的最大值，这里用一个额外队列来维护一个递减序列，当前元素比队列-1尾大则尾一直pop弹出，再插入，这样保证只有比队头元素小且在对头元素之后出现的元素会被记录，比当前元素小且在之前出现的属于冗余可以去掉。
  - 位运算问题
    - 利用python的数据存储特性来运算问题
      - 用位运算模拟加减乘除
        - 要注意python中数据不定长，不会判断最高位是符号位且用补码表示的特性，通过位运算符号来实现需求
          - 不定长：限制长度 &0xffffffff
          - 不判断最高位: a if a<=0x7fffffff else ~(a^0xffffffff) 
          - 用补码表示：~a 为 (-a-1)
        - ``` python
              def add(a,b):
                  mask = 0xffffffff
                  a,b = a&mask,b&mask
                  while b!=0:  # b==0时convergence
                      a,b = a^b,(a&b)<<1 & mask  # 分别位不进位部分和进位部分，进位部分要&以下mask的意义是当最高位为1和1的时候会移位到第33位，这时候要消除掉，因为a^b对于1和1的话还是1，保留负数符号，所以直接消除即可。
                  return a if a<=0x7fffffff else ~(a^mask)  # 对正数和负数判断 
    - 找重复/特异数问题，找不重复的两个数字，或找不重复的一个数字等。用O(n)和O(1)空间复杂度完成
      - 异或和与
        - 异或：
          - 两个数字异或的结果a^b是将a和b的二进制每一位进行运算，得出的数字。运算的逻辑是如果同一位的数字相同则为0，不同则为1。
          - 异或满足交换率
          - **任何数和本身异或为0**, i.e. a^a=0.
          - 任何数和0异或是本身, i.e. a^0=a.\
        - 与
          - 1&1=1其余为0
          - a^a=1, a^0=0.
      - 思路:
        - 1.若有一个列表的数，有2个不重复，其他都重复一次，那么列表数依次相互异或，结果为不重复的数字相异或的结果。可区分开重复数字。
        - 2.若两个数异或，结果中为1的位代表两个数在改位是特异的（一个为0一个为1）。
        - 3.设一个异或结果中从右到左第一个为1的位为1，其余为0的数，将该数和之前2个重复数字相与，必定一个为1（在该位置为1）一个为0（在该位置为0）。可用于将不重复数字异或结果中将数字分开。、
        - 4.返回ab或做其他的操作
      - e.g. 找不重复的两个数
        - ``` python
              # 1. 结果为不重复数字相异或
              res = 0
              for item in nums:
                  res ^= item
              # 2. 找出第一个为1的位
              x = 1  # e.g.00001, 00010, 00100, ...
              while x&res == 0: x<<=1  # 不能!=1因为按位与返回的是数
              # 3.
              a,b = 0,0
              for item in nums:
                  if item & x:
                      a ^= item
                  else:
                      b ^= item
              # 最后，ab是那两个数
              operations()
              return [a,b]
        - e.g. 找只出现一次的数字
          - 只出现一次：全员异或后剩下的
          - 除了一个数字出现一次，其他都出现了三次，让我们找到出现一次的数
            - 变式。对每一位统计所有数的1的个数，若能被3整除则是重复的数字，若不能则是特异数，对每位循环再|=上每一位就构成了特异数，返回即可             
  - 查找/搜索问题
    - 线性查找：
      - 可能会需要借助各种数据结构
      - 可能涉及动态规划
      - 双指针问题：查找符合条件的区间，累加值等。
        - 双指针和滑动窗口
          - 灵活用窗口，不一定要暴力遍历所有窗口或者用窗口遍历所有位置  
          - 指针相对位置变化=窗口大小
        - 快慢指针问题
          - 一个指针先走，另一个当满足条件自增或变成变成先走指针的位置 
            - e.g. 反转字符串单词，先让快指针走遍历到单词头部，慢指针在单词尾部，输出word[fast:slow]即可
              - 一般是while中套两个while分别是快慢指针
        - 对撞指针问题
          - e.g. 递增数列找两个和为target的数，需要左右指针从数列两端出发
            - 用while让指针对撞
    - 二分查找
      - 排序数组中的搜索问题，首先想到二分法解决，双指针也可以
      - 是多数考题的考察重点
      - 掌握二分法的模版（以后补充）
         - ```python
              def bisearch():
                mid = left + (right-left) // 2
                if data[mid] == target:
                  operations()
               elif data[mid] > target:
                 right = mid - 1  # or other operations like right=mid, notice the boundary!
               else:
                  left = mid + 1  # or other operations
       - 模版的基础上要会变化，注意边界条件！
       - 变式：
         - e.g.统计一个数字在排序数组中出现的次数（jz53）
           - 不仅查找target，是要查找到target的左右边界，此时需要改变算式。
           - 也可以用统计计数，维护一个递增的计数变量。  
  - topk问题
    - 先排序再取前k：可以sorted，可以快排，可以堆排
    - 快速选择算法：再快排基础上加一层判断
  - 非链表双指针问题
    - e.g. 最大不重复子数组问题
      - 分析现在循环的这一位在之前重复的位置和现在循环之前重复位置的大小，若小则当前结尾的长度是当前循环之前的最大长度+1，若大则以当前位结尾的长度就是当前-当前重复位 
      - 也可用动态规划 
  - 数组
    - 和最大的子数组问题
      - 贪心，linear time algorithm
      - 动态规划
    - 众数问题
      - 哈希
      - 排序 后的中位数
      - linear time algorithm: 根据投票抵消，记录一个cnt(票数)和number(众数)   
  - 大数越界问题
    - 转换成字符串
    - 分治
  - 路径问题
    - dfs
    - bfs
      - BFS有两种写法。第一种，从队列pop出来的，若有左孩子则入队列，若有右孩子则入队列。第二种，从队列出来的，若为None则不操作，若部位none则左右孩子入队列。要根据实际情况来选择BFS的写法。
        - 比如要在BFS遍历中print出二叉树的空节点，那么第二种就能实现，而第一种不能在BFS中实现，因为若无左孩子就输出的话不符合broad search定义。
  - 链表（ListNode）问题
    - 双指针
      - pre和cur经常要在while之前先定义
      - 双指针问题一般涉及迭代和递归
    - 三指针
      - 三指针问题一般能转化为双指针
    - 链表的reference问题，用来保存整体，可以在while改变链表结构之前先把整个链表（头节点）赋值给一个reference
    - 链表问题的边界情况
      - 链表是否为空
      - 若有多个链表，链表等长问题（三元表达式）
    - 链表反转
      - 三指针：用while即可 
      - 双指针 
        - ``` python
          def solution(): 
            def reverseList(self, head):
                # inputs: listnode
                # outputs: listnode
                if not head:
                    return 
                def recur(pre,cur):
                    if not cur: 
                        return pre
                    res = recur(cur,cur.next)
                    cur.next = pre
                    return res  # 返回链表头节点
            return recur(None, head)
               
  - 动态规划问题
    - 对于动态规划问题，先确定状态，想象一个状态数组，写出状态方程，再分析边界情况，步骤和代码模版为
      - 步骤
        - 想象我们线性遍历数据就能得出答案
        - 写出状态转移关系式，当前状态由前面状态决定
          - 一般的转移关系都是: dp[i] = dp[i-1]+xxxx 或 dp[i] = max(dp[i-1],xxxxx), 转移的if条件也要注意
        - 找边界情况，初始化情况
        - 写代码
        ``` python
            def dynamic_programming():
                initialize_with_boudary()
                for loop:
                    solve_the_dp_bottom_up()  # to avoid recursion, from boudary initialization to the current state
                    operations()
                return dp[xxx] 
        ```
        - 经典例题: jz63.py简单的动态规划
    - 对以i位置之前的状态
      - 定义状态，看是否能用类似‘以i结尾’来定义
      - 确定dp[i]与dp[i-1]的关系
      - 临界条件等
    - 有时候不一定要设置动态规划数组，若要降低空间复杂度可以维护（一个或多个）全局变量替代dp数组。
  - 递归问题
    - 递归问题分为递和归两个部分。有三个要素。递归结束条件，递归等价关系式子，递归出口。
      - **边界+递归+返回**
    - 在设计和理解递归的时候，可以把递归过程想象成一个递归栈stack，每次递归都是将这行程序入栈，遇到边界条件返回后依次弹出。
    - 涉及代码时先考虑返回值。
    - skelton code:  
      - ```python
         def recur():
            if case: return res  # 边界条件
            return recur() + operation  # recur()是递，+operation是归
      - 递归思想：在这一步（递归）我要完成什么，剩下的交给余下所有的迭代。想象实现到最底层，然后依次往上推。
        - 若递归子结构，比如构建递归树。返回值是整体的root
          ``` python
              def build_tree(data):
                node = data.pop(0)
                # boundary
                if not node: return None
                # operation
                node.left = build_tree(data)
                node.right = build_tree(data)
                return node
        - 若递归输出某个值：参考skelton code。返回值是一个随着递归不断改变的变量。比如Boolean的True或False。
          - 或数值 e.g.找到二叉树的深度，类似于return recur(half)+val+recur(half)类型
            ``` python
                def maxDepth(self, root):
                  if not root: return root
                  return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1    
        - 若递归修改某个global量，不用return直接修改
      - 写完递归问题要仔细考虑是否能精简代码优化设计，代码风格很重要。
      - 短路递归：n>1 and self.sumNums(n-1) 这样的代码，当and前面一项不符合的时候就不会执行后面的代码，可以起到不用if即可完成短路。
  - 树（TreeNode）的问题
    - 树的知识：
      - 树的深度等于左子树的深度与右子树的深度中的最大值+1。  
    - 树的遍历问题
      - 前中后序遍历
        - 模版: 
          ``` python
              def traversal(root):
                tree = []
                def recur(root):
                  # there will be specific oprations after each line
                  if not root: return
                  recur(root.left)
                  tree.append(root.val)
                  recur(root.right) 
                recur(root)
                return tree   
        - 常用递归函数，当然可以先写递归函数，然后再看有无可能转化为调用递归traversal自身。
        - 上述代码属于修改某个global变量的递归
      - 层次遍历
        - 递归模版:
          ``` python
              def traversal(root):
                tree = []
                def recur(root, level):
                  if not root: return
                  if len(tree)==level:
                    tree.append([])
                  tree[level].append(root.val)
                  if node.left: recur(root,level+1)
                  if node.right: recur(root,level+1)
                recur(root,0)
                return tree
        - 想象最差情形，全是右子树，那么若tree中的节点==level的时候就得网tree中加一个list[]存当前层的节点。
        - BFS模版（层次遍历，记录每层，每层一个子list）
          ``` python
              def bfs(root):
                if not root: return []
                tree = []
                # 双端队列
                from collections import deque
                q = deque()
                q.append(root)
                while q:
                  cur = []  # 该层的临时list，最后要append到res总list中
                  length = len(q)  # 要
                  for i in range(length):  
                    temp = q.popleft()
                    cur.append(temp.val)
                    if temp.left: q.append(temp.left)
                    if temp.right: q.append(temp.right)
                  tree.append(cur)  # or other operations()
                return tree
        - 用双端队列的while来完成递归，注意临时list: cur的建立和使用。      

    - 树的路径匹配问题
      - 树的遍历、匹配等问题一般用递归来求解
      - 如何匹配路径？当采用深度优先搜索策略时：
        - 如何从根节点出发往下走，可以考虑运用前，中，后序遍历的递归形式作为框架
          - 比如
            ```python
                def preorder_trav(root):
                 # boundary
                  if not root: return op
                  # operations
                  op(root.val)
                  preorder_trav(root.left)
                  preorder_trav(root.left)
                  # operations
                  op()
        - 回溯问题：此路不通，原路返回，另寻他路。可建立一个数据结构（比如栈）保存中间结果，不符合条件需要回溯的时候对数据结构操作（比如栈的弹出）。
        - 剪枝问题：回溯问题本质上时暴力穷举，剪枝是对这类问题的优化，当中间结果不符合某个条件的时候就不往下搜索。
        - 回溯下的和为某值sum的路径问题
          ``` python
              temp, res = [],[]
              def dfs(root,sum):
                if not root: return 
                temp.append(root.val)
                sum -= root.val
                if not root.left and not root.right and sum==0: res.append(temp)
                dfs(root.left, sum)
                dfs(root.right, sum)
              dfs(root,sum)
              return res
    - 二叉树匹配问题
      - 匹配子树问题
        - 一般用递归来做，可能涉及多个递归。
        - 先将根节点匹配；根节点匹配后，对子树进行匹配。 
      - 匹配对称二叉树问题
        - 递归方法，属于递归输出某个值（boolen）的问题，return T or F即可，用逻辑表达式链接递归。
          ``` python
              def match(left,right):
                if not left and not right:
                  return True
                elif not left or not right or left.val!=right.val:
                  return False
                else:  # 左右都有且相等
                  return match(left.left,right.right) and match(left.right,right.left)
      - 验证二叉树是BST
        - 是一个递归求值问题，递归的返回用return recur and recur即可 
        - 关键在于设置一个左右inf界限值
          ``` python
              def validate_bst(root,l,r):
                if not root: return True
                if l<=root.val<=r:
                  return validate_bst(root.left,l,root.val) and validate_bst(root.right,root.val,r)
                else: return False
              return validate_bst(root,float('-inf'),float('inf'))
      - 树的查找问题
        - 查找最近公共祖先
          - 本题属于查找值的递归，找到则返回即可。 
          ``` python
              def lowestCommonAncestor(self, root, p, q):
                # boundary
                if not root or root == p or root == q:
                  return root
                # recurrence
                left = self.lowestCommonAncestor(root.left, p, q)  # left最后返回的是p或q，如果p或q存在与子树
                right = self.lowestCommonAncestor(root.right, p, q)
                if not left or not right:  # 若在同侧，返回从上到下先遍历到弹出的那个
                  return left or right
                else:  # 若在异侧，返回自己
                  return root  
          - 如果是二叉搜索树那么，可以根据值的大小来判断查找结果
  - 单调栈问题
    - 什么时候用？通常是一维数组，要寻找任一元素右边（左边）第一个比自己大（小）的元素，且要求 O(n) 的时间复杂度。（这类问题通常成为Next Greater Number问题，当然，有很多变式）
      - 对于NGN问题，通常的伪代码是
      - ```python d
           for item in the list:
              # 当然，这句话可和最后的append合并 
              if not stack or new<stack[-1]:
                  stack.append(new)
              else:
                  while stack and new>stack[-1]:
                      stack.pop()
              stack.append(new)
      - 但我们需要根据实际题目来微调
      - NGN问题也有多种变式，比如找每个元素后面第一个比他大的元素，我们可以维护一个从左到右的单调递减栈，也可以维护一个从右到左的单调递减栈，也可以维护一个从右到左的单调递增栈，只需改变条件。 
      - 一般这类问题通常有更差解，一般是暴力法和树的方法（递归），分别是O(n)和O(lgn)
    - 单调栈分为单调递增和单调递减，单调递增栈就是栈底到栈顶是递增的，只有当前元素比栈顶元素更大的时候才能入栈。
    - [单调栈总结](https://leetcode-cn.com/circle/discuss/kdY0zV/)
      - 对于用额外数据结构存储当前最大最小值也可以用单调栈思想，即维护一个单调递增/递减的数据结构。比如维护递减队列，那么当前元素进入时，比当前元素大的都弹出（用while来实现即可），这样队列头永远是当前最大，最大弹出后的队头也是当前最大。
        - e.g. 用额外队列实现队列数据结构的最大值，这里用一个额外队列来维护一个递减序列，当前元素比队列-1尾大则尾一直pop弹出，再插入，这样保证只有比队头元素小且在对头元素之后出现的元素会被记录，比当前元素小且在之前出现的属于冗余可以去掉。

- 遇到while问题，若很难放进一个while，可以先用for遍历到我们需要的地方再开始while，结合for和while一起使用。

- 对于listnode的while问题，注意while的条件，若while是head的时候，那么当指针直到最后一个节点的next，即None的时候，才不循环。