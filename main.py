import sys
import lib.infra.modules as mods

def get_args():
    args = sys.argv
    args.pop(0)
    return args

def get_input(module_name):
    f = open('inputs/' + module_name + '.txt', 'r')
    response = f.read()
    f.close()
    return response

def write_output(module_name, output):
    f = open('outputs/' + module_name + '.txt', 'w')
    f.write(output)
    f.close()

if __name__ == '__main__':
    args = get_args()
    module = args[0]
    run = mods.get_module(module)
    input = get_input(module)
    res = run(input)
    write_output(module, res)
    print(res)

