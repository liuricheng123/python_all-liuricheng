class person:
    arm=0
    leg=0
    name=""
    age=0
    sex=""
    high=""
    weight=""
    color=""

    def walk(self):
        print("到处爬来爬去")
p=person()
p.walk()
p.arm=2
p.leg=2
p.age=20
p.name="洪小雅"
p.high="1.20"
p.weight="300"
p.color="绿色"
p.sex="女生"
print("我叫",p.name,",身高",p.high,",体重",p.weight,",我是",p.sex,"，我今年",p.age,"岁了，","我有",p.arm,"个胳膊，",p.leg,"条腿，我的肤色是",p.color)
