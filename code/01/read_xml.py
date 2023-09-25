import os

# 读取文件夹中所有xml文件的路径
import read_path

# 读取单个xml文件,并分割出bvalue, xgradient, ygradient, zgradient
import single_read_xml

# 读取文件夹中所有xml文件,并分割出bvalue, xgradient, ygradient, zgradient
def read_xml(in_path):
    xml_path_list = read_path.read_xml_path(in_path)
    bvalue_list = []
    xgradient_list = []
    ygradient_list = []
    zgradient_list = []
    for xml_path in xml_path_list:
        bvalue, xgradient, ygradient, zgradient = single_read_xml.read_xml(xml_path)
        bvalue_list.append(bvalue)
        xgradient_list.append(xgradient)
        ygradient_list.append(ygradient)
        zgradient_list.append(zgradient)
    return bvalue_list, xgradient_list, ygradient_list, zgradient_list

if __name__ == '__main__':
    bvalue_list, xgradient_list, ygradient_list, zgradient_list = read_xml('./')
    print(bvalue_list)
    print(xgradient_list)
    print(ygradient_list)
    print(zgradient_list)