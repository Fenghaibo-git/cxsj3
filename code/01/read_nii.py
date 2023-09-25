import nibabel as nib
import numpy as np

def read_nii_by_nib(nii_path):
    image_nib = nib.load(nii_path)
    image = image_nib.get_fdata()
    header = image_nib.header
    affine = image_nib.affine
    return image, header, affine

def save_nii_by_nib(nii_path, image, affine, header):
    image_nib = nib.Nifti1Image(image, affine, header=header)
    nib.save(image_nib, nii_path)

# 写一个将多个3维nii文件转化为4维nii的函数
def convert_3d_to_4d_nii(nii_paths):
    images = []
    # 将n个3维nii文件的image取出来，放到一个list中，(120,120,80,1) -> (120,120,80,n)
    for nii_path in nii_paths:
        image_nib = nib.load(nii_path)
        image = image_nib.get_fdata()
        images.append(image)
    # 修改头文件的维度值
    header = image_nib.header
    header.set_data_shape((image.shape[0], image.shape[1], image.shape[2], len(nii_paths)))
    # 修改头文件的体素尺寸
    voxel_size = header.get_zooms()
    voxel_size = voxel_size[:3] + (1,)
    header.set_zooms(voxel_size)
    


    # 保存4维nii文件
    image_4d = np.concatenate(images, axis=3)
    image_nib = nib.Nifti1Image(image_4d, np.eye(4), header=header)
    nib.save(image_nib, nii_paths[0][:-6] + '_4d.nii.gz')


# 写一个将4维nii文件转化为多个3维nii的函数
def convert_4d_to_3d_nii(nii_path):
    image_nib = nib.load(nii_path)
    image = image_nib.get_fdata()
    for i in range(image.shape[3]):
        image_3d = image[:,:,:,i]
        image_nib = nib.Nifti1Image(image_3d, np.eye(4))
        nib.save(image_nib, nii_path[:-4] + '_' + str(i) + '.nii.gz')
    
