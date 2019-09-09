# -*- coding:utf-8 -*-
#20190909 peichenhao resample function for 2d 3d with label and image
import numpy as np
import nibabel as nib
from scipy import ndimage
import SimpleITK as sitk

def sitkresample(image, label, spacing=[0.5,0.5,12]):
    new_image = resamplewithinterpolator(image, sitk.sitkLinear,spacing)
    new_label = resamplewithinterpolator(label, sitk.sitkNearestNeighbor,spacing)
    return new_image, new_label
def resamplewithinterpolator(image, interpolator, spacing) :
    resample = sitk. ResampleImageFilter ()
    resample.SetInterpolator (interpolator)
    resample.SetOutputDirection(image.GetDirection())
    resample.SetOutputOrigin(image.GetOrigin())
    new_spacing = spacing
    orig_size = np.array (image.GetSize(),dtype=np.int)
    orig_spacing = list(image. GetSpacing())
    new_spacing[2]=orig_spacing[2]
    print(new_spacing)
    resample.SetOutputSpacing(new_spacing)
    new_size=[oz*os/nz for oz, os,nz in zip(orig_size, orig_spacing, new_spacing)]
    new_size = np.ceil (new_size). astype(np.int) # Image dimensions are in integers
    new_size = [int(s) for s in new_size]
    resample.SetSize(new_size)
    newimage = resample.Execute (image)
    return newimage
def resample():
    raw = 'image.nii.gz'
    datapath='label.nii.gz'
    itk_img = sitk.ReadImage(raw)
    itk_label = sitk.ReadImage(datapath)
    new_image, new_label=sitkresample(itk_img,itk_label,spacing=[0.5,0.5,12])
    savelabel = 'H:/1data/label/' + '.nii.gz'
    saveraw = 'H:/1data/raw/'  + '.nii.gz'
    sitk.WriteImage(new_image, saveraw)
    sitk.WriteImage(new_label, savelabel)
if __name__ == "__main__":
    print('Begin:')
    resample()