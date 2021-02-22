- 先考虑边界情况，如if not obj

- 对于动态规划问题，先确定状态，想象一个状态数组，写出状态方程，再分析边界情况

- 用数据结构解决，比如栈，双栈，堆，队列等

- dfs和bfs
  - dfs主要用递归，或者暴力for来代替dfs
  - bfs主要用队列，while迭代

- 对于python的大数越界问题，虽然python的大数可以不考虑，但若要考虑可以考虑转换成字符串问题

- lc问题种类：
  - 查找问题
    - 线性查找：
      - 可能会需要借助各种数据结构
    - 二分查找
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
  - 动态规划问题
    - 对于动态规划问题，先确定状态，想象一个状态数组，写出状态方程，再分析边界情况
    - 对以i位置之前的状态
      - 定义状态，看是否能用类似‘以i结尾’来定义
      - 确定dp[i]与dp[i-1]的关系
      - 临界条件等
    - 有时候不一定要设置动态规划数组，若要降低空间复杂度可以维护（一个或多个）全局变量替代dp数组。
  - 递归问题
    - 递归问题分为递和归两个部分。有三个要素。递归结束条件，递归等价关系式子，递归出口。
    - 在设计和理解递归的时候，可以把递归过程想象成一个递归栈stack，每次递归都是将这行程序入栈，遇到边界条件返回后依次弹出。
    - 涉及代码时先考虑返回值。
    - skelton code:
      - ```python
         def recur():
            if case: return res  # 边界条件
            return recur() + operation  # recur()是递，+operation是归
        ```
      - 递归思想：在这一步（递归）我要完成什么，剩下的交给余下所有的迭代。想象实现到最底层，然后依次往上推。
        - 若递归子结构，比如构建递归树。返回值是整体的root
          ```python
             def build_tree(data):
                node = data.pop(0)
                # boundary
                if not node: return None
                # operation
                node.left = build_tree(data)
                node.right = build_tree(data)
                return node
        - 若递归输出某个值：参考skelton code。返回值是一个随着递归不断改变的变量
        - 若递归修改某个global量，不用return直接修改
      - 写完递归问题要仔细考虑是否能精简代码优化设计，代码风格很重要。
  - 树（TreeNode）的问题
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
    - 二叉树匹配问题
      - 比如匹配两个子树，比如匹配子树。
      - 一般用递归来做，可能涉及多个递归。
      - 先将根节点匹配；根节点匹配后，对子树进行匹配。 
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

- 遇到while问题，若很难放进一个while，可以先用for遍历到我们需要的地方再开始while，结合for和while一起使用。

- 对于listnode的while问题，注意while的条件，若while是head的时候，那么当指针直到最后一个节点的next，即None的时候，才不循环。