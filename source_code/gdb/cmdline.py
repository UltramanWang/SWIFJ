import sys
def hello_gdb():
    for i, arg in enumerate(sys.argv):
        print(f"参数 {i+1}:", sys.argv)
        
def test_print():
    print("Hello World!")

def run(command):
    return gdb.execute(command, to_string=True)


if __name__=='__main__':
    hello_gdb()
    gdb.execute('r', to_string=True)