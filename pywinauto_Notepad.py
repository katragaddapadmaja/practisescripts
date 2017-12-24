from pywinauto import application
from pywinauto.keyboard import SendKeys
from time import sleep

# opening Notepad & writing & saving in C drive
app = application.Application()
app.start("Notepad.exe")
app.Notepad.edit.TypeKeys("Hello World")
app.UntitledNotepad.menu_select("Edit-> Replace")
#Identifiers are used to locate the options like Find Next,replace,replace all,cancel
# app.Replace.PrintControlIdentifiers()
app.Replace.Edit.TypeKeys("Hello")
app.Replace.Edit2.TypeKeys("Bye")
sleep(2)
app.Replace.Button3.Click()
app.Replace.Cancel.Click()
app.Notepad.MenuSelect("File -> SaveAs")
app.SaveAs.edit.SetText("C:\Users\Padmaja\PycharmProjects\Pywinauto_Notepad2.txt")
app.saveAs.Save.Click()
#################

app = application.Application()
app.start("Notepad.exe")
app.Notepad.edit.TypeKeys("Hello World")
app.UntitledNotepad.menu_select("Format-> Font")
#app.Font.PrintControlIdentifiers()
app.Font.Edit.TypeKeys("Arial")
app.Font.Click()
sleep(2)
app.FontDialog.Edit2.TypeKeys("Italic")
app.FontDialog.Click()
sleep(2)
app.Font.Button.Click()
app.Notepad.MenuSelect("File -> SaveAs")
app.SaveAs.edit.SetText("C:\Users\Padmaja\PycharmProjects\Pywinauto_Notepad_format1.txt")
app.saveAs.Save.Click()
#####################
#app.UntitledNotepad.menu_select("Help->View")
#app.UntitledNotepad.View.Click()
#app.Notepad.MenuItem("View")
#app.Notepad.MenuItem("View->Status Bar")
#app.Notepad.Edit.RightClick()
#app.PopupMenu.MenuClick("Select All")
#app.Notepad.Edit.RightClick()
#app.PopupMenu.MenuClick("Copy")