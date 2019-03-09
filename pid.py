import os
from multiprocessing import Process
import subprocess


#子进程要执行的代码
#print("__name__:"+__name__)

def run_proc(name):
    print("子进程参数： %s ID: (%s)..." % (name, os.getpid()))
    os.system("pause")
if __name__ == '__main__' :
    print("主进程ID：%s." % os.getpid());
    p = Process(target=run_proc, args=('传入的参数',));
    print("启动子进程");
    p.start();
    p.join();
    print('子进程结束');
    os.system("pause")

'''print('---------------------------------');
print('Process (%s) start...' % os.getpid())
pid = os.getpid()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''