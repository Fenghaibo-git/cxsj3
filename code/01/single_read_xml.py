import os

# 读取单个xml文件,并分割出bvalue, xgradient, ygradient, zgradient
def read_xml(in_path):
    f = open(in_path, 'r', encoding='utf-8')
    lines = f.readlines()
    bvalue = 0
    xgradient = 0.0
    ygradient = 0.0
    zgradient = 0.0
    for line in lines:
        # 如果line中包含<diffision>，则打印出来
        if '<diffision ' in line:
            # 分割字符串，依据"
            a = line.split('"')
            bvalue = int(a[1])
            xgradient = float(a[3])
            ygradient = float(a[5])
            zgradient = float(a[7])
    return bvalue, xgradient, ygradient, zgradient


if __name__ == '__main__':
    print(read_xml('1.xml'))
