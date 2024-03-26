import subprocess
import time
import os

def test_run_gdb():
    # 示例GDB命令列表
    gdb_commands = [
        'break main',
        'run',
        # 'source gdb/printf.py',
        'info registers',
        # 'continue',
        'interrupt', 
        'set $cs=0xff',
        'info registers',
        # 'info registers',
        'continue',
        'quit'
    ]
    # 使用subprocess.Popen来运行GDB命令
    process = subprocess.Popen(['gdb',os.path.join(os.getcwd(),'debug','hello.exe')], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    # 发送GDB命令到gdb进程的标准输入
    for command in gdb_commands:
        process.stdin.write(f'{command}\n')   
        if command=='interrupt':
            time.sleep(1)
    # 等待GDB进程结束并获取输出
    output, _ = process.communicate()
    return output


 

if __name__=='__main__':
    # print(os.getcwd())
    # exit(0)
    # 运行GDB并获取输出
    gdb_output = test_run_gdb()
    print(gdb_output)