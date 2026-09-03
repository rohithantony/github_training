import subprocess

def run_command():
    command = input("Enter a command: ")

    # Vulnerable: completely user-controlled input reaches a shell
    result = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output, error = result.communicate()

    print(output.decode())
    print(error.decode())

if __name__ == "__main__":
    run_command()