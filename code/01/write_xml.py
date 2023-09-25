import os

# 读取文件夹中所有xml文件中的bvalue, xgradient, ygradient, zgradient
import read_xml

# 将bvalue, xgradient, ygradient, zgradient分别写入xml文件
def write_bval_bvec(bvalue_list, xgradient_list, ygradient_list, zgradient_list, save_path='./', save_name='temp'):
    # 将bvallue写入bval文件
    bval_path = os.path.join(save_path, save_name + '.bval')
    f = open(bval_path, 'w')
    for bvalue in bvalue_list:
        f.write(str(bvalue) + ' ')
    f.close()
    # 将gradient写入bvec文件
    bvec_path = os.path.join(save_path, save_name + '.bvec')
    f = open(bvec_path, 'w')
    # 逐行写入xgradient, ygradient, zgradient
    for xgradient in xgradient_list:
        f.write(str(xgradient) + ' ')
    f.write('\n')
    for ygradient in ygradient_list:
        f.write(str(ygradient) + ' ')
    f.write('\n')
    for zgradient in zgradient_list:
        f.write(str(zgradient) + ' ')
    f.write('\n')
    f.close()

if __name__ == '__main__':
    bvalue_list, xgradient_list, ygradient_list, zgradient_list = read_xml.read_xml('./')
    write_bval_bvec(bvalue_list, xgradient_list, ygradient_list, zgradient_list, save_path='./')