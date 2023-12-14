cdimport os
import re

class InMemoryFileSystem:
    def __init__(self):
        self.fs = {'/': {'type': 'dir', 'content': {}}}
        self.current_path = '/'

    def mkdir(self, directory_name):
        new_path = os.path.join(self.current_path, directory_name)
        if new_path in self.get_current_directory_content():
            print(f"Error: Directory '{directory_name}' already exists.")
        else:
            self.fs[new_path] = {'type': 'dir', 'content': {}}
            print(f"Directory '{directory_name}' created.")

    def cd(self, path):
        if path == '/':
            self.current_path = '/'
        elif path == '..':
            self.current_path = os.path.dirname(self.current_path)
        elif path.startswith('/'):
            self.current_path = path
        else:
            new_path = os.path.join(self.current_path, path)
            if new_path in self.fs and self.fs[new_path]['type'] == 'dir':
                self.current_path = new_path
            else:
                print(f"Error: Directory '{path}' not found.")

    def ls(self, path=None):
        if path is None:
            path = self.current_path
        if path not in self.fs or self.fs[path]['type'] != 'dir':
            print(f"Error: Directory '{path}' not found.")
        else:
            print("Contents:")
            for item in self.fs[path]['content']:
                print(item)

    def grep(self, pattern, file_path):
        if file_path not in self.fs or self.fs[file_path]['type'] != 'file':
            print(f"Error: File '{file_path}' not found.")
        else:
            content = self.fs[file_path]['content']
            matches = re.findall(pattern, content)
            print(f"Matches in '{file_path}':")
            for match in matches:
                print(match)

    def cat(self, file_path):
        if file_path not in self.fs or self.fs[file_path]['type'] != 'file':
            print(f"Error: File '{file_path}' not found.")
        else:
            content = self.fs[file_path]['content']
            print(content)

    def touch(self, file_name):
        new_path = os.path.join(self.current_path, file_name)
        if new_path in self.get_current_directory_content():
            print(f"Error: File '{file_name}' already exists.")
        else:
            self.fs[new_path] = {'type': 'file', 'content': ''}
            print(f"File '{file_name}' created.")

    def echo(self, text, file_path):
        if file_path not in self.fs or self.fs[file_path]['type'] != 'file':
            print(f"Error: File '{file_path}' not found.")
        else:
            self.fs[file_path]['content'] = text
            print(f"Text written to '{file_path}'.")

    def mv(self, source_path, destination_path):
        if source_path not in self.fs:
            print(f"Error: Source path '{source_path}' not found.")
        elif destination_path not in self.fs or self.fs[destination_path]['type'] != 'dir':
            print(f"Error: Destination path '{destination_path}' not found.")
        else:
            self.fs[destination_path]['content'][os.path.basename(source_path)] = self.fs.pop(source_path)
            print(f"Moved '{source_path}' to '{destination_path}'.")

    def cp(self, source_path, destination_path):
        if source_path not in self.fs:
            print(f"Error: Source path '{source_path}' not found.")
        elif destination_path not in self.fs or self.fs[destination_path]['type'] != 'dir':
            print(f"Error: Destination path '{destination_path}' not found.")
        else:
            destination_name = os.path.basename(source_path)
            self.fs[destination_path]['content'][destination_name] = self.fs[source_path].copy()
            print(f"Copied '{source_path}' to '{destination_path}'.")

    def rm(self, path):
        if path not in self.fs:
            print(f"Error: Path '{path}' not found.")
        else:
            self.fs.pop(path)
            print(f"Removed '{path}'.")

    def get_current_directory_content(self):
        return self.fs[self.current_path]['content']

    def run_shell(self):
        while True:
            command = input(f"{self.current_path}$ ").strip().split(maxsplit=1)
            if not command:
                continue

            operation = command[0].lower()
            if operation == 'exit':
                break
            elif operation == 'mkdir':
                if len(command) > 1:
                    self.mkdir(command[1])
                else:
                    print("Error: Missing directory name.")
            elif operation == 'cd':
                if len(command) > 1:
                    self.cd(command[1])
                else:
                    print("Error: Missing directory path.")
            elif operation == 'ls':
                if len(command) > 1:
                    self.ls(command[1])
                else:
                    self.ls()
            elif operation == 'grep':
                if len(command) == 3:
                    self.grep(command[1], command[2])
                else:
                    print("Error: Incorrect number of arguments for 'grep'.")
            elif operation == 'cat':
                if len(command) > 1:
                    self.cat(command[1])
                else:
                    print("Error: Missing file path.")
            elif operation == 'touch':
                if len(command) > 1:
                    self.touch(command[1])
                else:
                    print("Error: Missing file name.")
            elif operation == 'echo':
                if len(command) == 3:
                    self.echo(command[1], command[2])
                else:
                    print("Error: Incorrect number of arguments for 'echo'.")
            elif operation == 'mv':
                if len(command) == 3:
                    self.mv(command[1], command[2])
                else:
                    print("Error: Incorrect number of arguments for 'mv'.")
            elif operation == 'cp':
                if len(command) == 3:
                    self.cp(command[1], command[2])
                else:
                    print("Error: Incorrect number of arguments for 'cp'.")
            elif operation == 'rm':
                if len(command) > 1:
                    self.rm(command[1])
                else:
                    print("Error: Missing path.")
            else:
                print(f"Error: Unknown command '{operation}'.")

if __name__ == "__main__":
    file_system = InMemoryFileSystem()
    file_system.run_shell()
