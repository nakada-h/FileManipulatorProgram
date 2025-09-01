# FileManipulatorProgram

`file_manipulator.py` は、ファイルの内容を操作するシンプルなPythonスクリプトです。  
コマンドライン引数として操作内容を指定することで、ファイルの内容を **反転・コピー・複製・文字列置換** などを行うことができます。

---

## 使用方法

```bash
python file_manipulator.py <command> <arguments...>

## サポートしているコマンド
1. reverse

入力ファイルの内容を逆順にして出力ファイルに書き込みます。

```bash
python file_manipulator.py reverse input.txt output.txt

2. copy

入力ファイルをそのままコピーします。

```bash
python file_manipulator.py copy input.txt output.txt

3. duplicate-contents

入力ファイルの内容を**n回**複製し、同じファイルに上書き保存します。

```bash
python file_manipulator.py duplicate-contents input.txt 3

上の例では、input.txt の内容が3回繰り返されます。

4. replace-string

入力ファイル内の特定の文字列を別の文字列に置き換えます。

```bash
python file_manipulator.py replace-string input.txt "置換前" "置換後"

上の例では、input.txt 内の "置換前" がすべて "置換後" に置き換わります。

---

## エラーハンドリング

不正なコマンドを指定した場合は、次のようなエラーメッセージが表示されます。

```bash
not a valid command
