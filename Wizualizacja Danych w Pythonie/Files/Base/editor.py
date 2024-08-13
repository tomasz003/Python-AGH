import sys


def main():
    script, filename = sys.argv
    print(f"We're going to erase {filename}.")
    print("If you don't want that, hit CTRL-C (^C).")
    print("If you do want that, hit RETURN.")
    input("?")
    print("Opening the file...")
    f=open(filename, 'w')
    print("Truncating the file. Goodbye!")
    f.truncate()
    print("Now I'm going to ask you for three lines.")
    f.write(input("line 1: "))
    f.write(input("line 2: "))
    f.write(input("line 3: "))
    print("I'm going to write these to the file")
    print("And finally, we close it.")
    f.close()


if __name__ == "__main__":
    sys.argv = ['editor.py', 'test.txt']
    main()
