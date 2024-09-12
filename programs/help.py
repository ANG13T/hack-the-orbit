def read_contents(path):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_name = os.path.join(file_dir, path)
    f = open(file_name, 'r')
    file_contents = f.read()
    console.print("\n[cyan]" + file_contents + "[/]")
    f.close()

def help():
    read_contents('../options/commands.txt')