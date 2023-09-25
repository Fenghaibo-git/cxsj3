import os

# 读取文件夹中所有xml文件的路径
def read_xml_path(in_path):
    xml_path_list = []
    for file in os.listdir(in_path):
        if os.path.splitext(file)[1] == '.xml':
            xml_path_list.append(os.path.join(in_path, file))
    # 排序
    xml_path_list.sort()
    return xml_path_list

# 读取文件夹中所有nii文件的路径
def read_nii_path(in_path):
    nii_path_list = []
    for file in os.listdir(in_path):
        if os.path.splitext(file)[1] == '.nii':
            nii_path_list.append(os.path.join(in_path, file))
    # 排序
    nii_path_list.sort()
    return nii_path_list

if __name__ == '__main__':
    print(read_xml_path('./'))