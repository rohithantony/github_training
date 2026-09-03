import subprocess

def main():
    user_input = input("Enter command: ")
    subprocess.call(user_input, shell=True)

if __name__ == "__main__":
    main()