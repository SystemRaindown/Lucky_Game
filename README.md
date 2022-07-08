1.Lucky Game是什么？
- 它使用世界上最著名的**pyQt5**写成的图形系统，以**main.py**为主程序入口的窗口程序。

- 缺点是**gui.py**内部的*name_form*变量需要手动往内部导入，分隔字节之间的符号为*\n*。

2.如何把项目的2个python文件打包为可执行文件
- 可使用**pyinstaller**打包库并在命令行中输入**pyinstaller -F -w main.py -p gui.py**打包为可执行文件。

