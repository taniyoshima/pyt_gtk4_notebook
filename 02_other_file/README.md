# 02_other_file

[戻る](../README.md)

<br>

## 内容 

Gtk.NoteBookに複数のページを追加すると、その処理をおこなうクラスのコードが量が多くなり可読性が低下する。これを防ぐために、Gtk.NoteBookPageのChild部分を別ファイルで作成するようにしてファイルを分けることにしました。  

Gtk.NoteBookPageを別ファイルにしようとしましたが、cambalacheでGtk.NoteBookPageのtemplateにすることが出来なかった。このため、そのchild部分となるGtk.Boxを別ファイルにすることにしました。

<br>

## 参考にしたHP

[戻る](../README.md)
