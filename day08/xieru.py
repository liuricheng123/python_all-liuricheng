# f=open("a.txt","w+",encoding="utf-8")
# f.write("床前明月光，\n 疑是地上霜。\n  举头望明月，\n   低头思故乡。")
# f.close()

f=open("111.jpg","rb")
w=open("2.jpg","wb")
data=f.read()
w.write(data)
f.close()
w.close
