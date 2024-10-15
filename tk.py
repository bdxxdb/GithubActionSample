import os  
import xlwt  
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox  
  
def txt_to_xls(txtname, xlsname):  
    try:  
        txt = open(txtname, 'r')  
        xls = xlwt.Workbook()  
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)  
        x = 0  
  
        line = txt.readline()  
        list = []  
        while line:  
            a = line.split('\t')  # 将数据以空格的方式分隔开  
            b = a[0:2]  # 这就是选择前四行保存下来（如果想保存第2，3行就写成b = a[1,3]）即可  
            c = a[3:4]  
            d = a[5:7]  
            e = a[8:21]  
            list.append(b + c + d + e)  
            line = txt.readline()  
        txt.close()  
  
        with open('temp.txt', 'w') as temp:  # 提取后的数据文件  
            for line in list:  
                s = '\t'.join(line)  
                temp.write(s + '\n')  
  
        new_txt = open('temp.txt', 'r')  
        while True:  
            # 按行循环，读取文本文件  
            line = new_txt.readline()  
            if not line:  
                break  
            for i in range(len(line.split('\t'))):  
                item = line.split('\t')[i]  
                sheet.write(x, i, item)  
            x += 1  
        new_txt.close()  
        xls.save(xlsname)  # 保存xls文件  
        print("已完成文件转换！！！")  
        os.remove("temp.txt")  
        messagebox.showinfo("成功", "文件转换已完成！")  
    except Exception as e:  
        messagebox.showerror("错误", f"发生错误：{e}")  
  
def convert_file():  
    txt_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  
    xls_path = filedialog.asksaveasfilename(defaultextension=".xls", filetypes=[("Excel files", "*.xls")])  
      
    if txt_path and xls_path:  
        txt_to_xls(txt_path, xls_path)  
  
# 创建GUI  
root = Tk()  
root.title("TXT to XLS Converter")  
  
# 标签和输入框  
Label(root, text="请选择TXT文件并输入XLS文件名进行转换:").pack(pady=10)  
  
# 转换按钮  
convert_btn = Button(root, text="转换文件", command=convert_file)  
convert_btn.pack(pady=20)  
  
# 运行GUI  
root.mainloop()