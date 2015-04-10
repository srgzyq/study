# taskmanager.py
# -*- coding: utf-8 -*-

import random, time, Queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = Queue.Queue()
# 接手结果的队列:
result_queue = Queue.Queue()

# 从BaseManager继承的QueueManaager
class QueueManaager(BaseManager):
    pass

# 把两个Queue都注册到网络上,callable参数关联了Queue对象:
QueueManaager.register('get_task_queue',callable=lambda: task_queue)
QueueManaager.register('get_result_queue',callable=lambda: result_queue)
# 绑定端口5000, 设置严重码'abc':
manager = QueueManaager(address=('',5000),authkey='abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d...' % n)
    task.put(n)

# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' %r)
# 关闭:
manager.shutdown()
