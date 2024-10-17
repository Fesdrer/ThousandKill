# 导言

这是由 Fesdrer 独立开发的背诵软件，使用 python 3.12 编写，取名参考了著名的背诵软件百词斩，取名为：ThousandKill。它不只能用于背单词，更能用于帮助背诵其他东西。

使用者如果使用 windows11，则可以直接打开 `ThousandKill.exe` 来使用，否则不保证软件能正常使用。

使用者也可以下载 python 3.12，运行 `ThousandKill.py` 来使用，也可以用 `Pyinstaller` 转换成 exe 文件，这里不具体赘述。

如果使用 `ThousandKill.py` 运行，要保证下载下来的所有 .py 文件和背诵文件都在同一个文件夹下才能使用，使用 `ThousandKill.exe` 只要保证其和背诵文件在同一文件夹下就能使用。

# 引入

注意到，任何一个要背诵的知识点都能够总结成二元组 $(Q,A)$ 的形式，即通过一个提示问题 $Q$ 背出答案 $A$，例如根据单词的英文背出中文意思，根据公式名称背出具体公式形式，等等。特别的，对于背单词，我们还可以引入一个新的部分 $e.g.$，也就是例句，可以帮助背诵单词，如果知识点不是单词，也可以用 $e.g.$ 存储一些相关知识点的注释。

因此，对于一个背诵组（例如必修一的英语单词、基本微分公式），可以表示成若干个二元组 $(Q,A)$ 或三元组 $(Q,A,e.g.)$ 的排列，并存储在一个 .txt 文件中。在软件中，使用者首先需要自己编辑背诵组，在第一行写明这个是二元组性质文件还是三元组性质文件，然后每两行或每三行表示一个知识点，例如：

二元组性质的文件 `formula.txt`:

```
2
质能方程式
E=mc^2
中和热热化学方程式：
H+(aq)+OH-(aq)=H2O(l)  ▲H=57.3kJ*mol^-1
```

三元组性质的文件 `word.txt`：

```
3
abandon
v. 放弃
Their decision to abandon the trip.
homework
n. 家庭作业

teacher
n. 老师
Happy teacher's day.
pneumonoultramicroscopicsilicovolcanoconiosis
矽肺病
The longest word in English is pneumonoultramicroscopicsilicovolcanoconiosis.
```

注意，二元组性质的文件中不能放入三元组，三元组同理。但是三元组文件中如果有不需要例句的知识点可以把例句一行空出来。

相信大家都发现了，这种背诵文件是使用者编辑的，所以使用者可以写入需要背诵的任何东西，而不像其他背诵软件只能背诵词库里预设的单词。

运行软件并输入背诵文件名（包括扩展名）后，软件就会按照顺序输出 $Q$ 的部分，使用者在思索一部分时间后可以按下回车键来查看 $A$ 和 $e.g.$（如果有），如果使用者没想出来或者想出来的和答案不同，则可输入 `f` 来把这一知识点标记下来。如果使用者不小心没能输入 `f` 把这一知识点标记下来，也可以在下一个知识点输出 $Q$ 后输入 `mark the last` 来标记上一个。最后软件可以把被标记的知识点整合输出成一个新的背诵文件，方便下次复习。

**注意，请使用 `utf-8` 编码格式在编辑背诵文件。**

下面开始具体讲解软件使用方法。

# 测试

打开软件可以看到一个目录，根据提示输入 $1$ 到 $3$ 可以开启对应的功能。输入 $1$ 进入测试功能。你首先要输入背诵文件名（包括扩展名）（你可以同时测试多组背诵文件，只需要依次输入文件名并用空格隔开即可），然后选择要基本测试还是扇贝式测试。如果是扇贝式测试则不会的知识点会多次重复，具体的，你需要把标记为 `f` 的知识点连续答对 $2$ 次才算过关。如果不选择扇贝式测试则不会重复。

选择完是否使用扇贝式测试后需要选择是否打乱知识点（否则按照背诵文件的顺序依次测试）。然后你要选择以下 $5$ 种测试方式中的一种来测试：

- 问 $Q$ 答 $A$
- 问 $A$ 答 $Q$
- $Q$ 和 $A$ 互问（既会问 $Q$ 答 $A$ 也会问 $A$ 答 $Q$）
- 拼写模式（问 $A$ 写 $Q$）
- 反转拼写模式（交换 $A,Q$ 然后问 $A$ 写 $Q$）

然后就可以开始测试了。

这里介绍一下拼写模式，每个知识点会先输出 $Q$，你需要不断输入对应的 $A$ 直到输入的是对的。如果当前输入错误，软件会输出答案，按下回车后清空答案和你输入的错误答案，然后你要再次输入，直到输入正确。如果一次输入正确，则不标记，否则标记。拼写模式不支持也没必要支持“标记上一个”功能。

最后软件可以把被标记的知识点整合输出成一个新的背诵文件，方便下次复习，你可以输入新文件的名称，也可以不输入表示不要输出新文件。

输出完后就会返回目录页。

# 转换

在目录选择 $2$ 进入转换模式，提供了背诵文件的格式转换。输入要转换的文件名和文件是二元组文件还是三元组文件后，你可以选择以下操作进行转换：

- `t`：若转换文件为三元组性质文件，把它转化为二元组性质文件，$e.g.$ 部分自动删除，否则转化为三元组性质文件，$e.g.$ 部分自动为空。
- `tr`：交换每一个问题的 $Q$ 和 $A$。
- `txt`：输出转换后的背诵文件。
- `md`：输出为 markdown 格式的文件，里面是一个表格，表示所有知识点。

程序会先询问是否要进行 `t` 操作，再询问是否要进行 `tr` 操作，然后要输入转换类型（`txt` 或 `md`），最后输入转换后的文件的文件名，就会输出转换后的文件。

输出后就会回到目录。

# 退出

目录下选择 $3$ 就会终止程序。你也可以直接按窗口右上角的×键来强制终止程序。

# 附录

最新添加了英语高考3500词（按照出现频率排序）的pdf版、txt版，分成171组，每组20个词语，能被本软件使用。
