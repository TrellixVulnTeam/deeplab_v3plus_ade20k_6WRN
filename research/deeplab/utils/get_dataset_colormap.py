# Copyright 2018 The TensorFlow Authors All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Visualizes the segmentation results via specified color map.

Visualizes the semantic segmentation results by the color map
defined by the different datasets. Supported colormaps are:

1. PASCAL VOC semantic segmentation benchmark.
Website: http://host.robots.ox.ac.uk/pascal/VOC/
"""

import numpy as np

# Dataset names.
_CITYSCAPES = 'cityscapes'
_PASCAL = 'pascal'
_ADE = 'ade'

# Max number of entries in the colormap for each dataset.
_DATASET_MAX_ENTRIES = {
    _CITYSCAPES: 19,
    _PASCAL: 256,
    _ADE: 256
}


def create_cityscapes_label_colormap():
  """Creates a label colormap used in CITYSCAPES segmentation benchmark.

  Returns:
    A Colormap for visualizing segmentation results.
  """
  colormap = np.asarray([
      [128, 64, 128],
      [244, 35, 232],
      [70, 70, 70],
      [102, 102, 156],
      [190, 153, 153],
      [153, 153, 153],
      [250, 170, 30],
      [220, 220, 0],
      [107, 142, 35],
      [152, 251, 152],
      [70, 130, 180],
      [220, 20, 60],
      [255, 0, 0],
      [0, 0, 142],
      [0, 0, 70],
      [0, 60, 100],
      [0, 80, 100],
      [0, 0, 230],
      [119, 11, 32],
  ])
  return colormap


def get_pascal_name():
  return _PASCAL


def get_cityscapes_name():
  return _CITYSCAPES


def bit_get(val, idx):
  """Gets the bit value.

  Args:
    val: Input value, int or numpy int array.
    idx: Which bit of the input val.

  Returns:
    The "idx"-th bit of input val.
  """
  return (val >> idx) & 1


def create_pascal_label_colormap():
  """Creates a label colormap used in PASCAL VOC segmentation benchmark.

  Returns:
    A Colormap for visualizing segmentation results.
  """
  colormap = np.zeros((_DATASET_MAX_ENTRIES[_PASCAL], 3), dtype=int)
  ind = np.arange(_DATASET_MAX_ENTRIES[_PASCAL], dtype=int)

  for shift in reversed(range(8)):
    for channel in range(3):
      colormap[:, channel] |= bit_get(ind, channel) << shift
    ind >>= 3

  return colormap

def create_ade_label_colormap():
  """Creates a label colormap used in ADE20K segmentation benchmark.

  Returns:
    A Colormap for visualizing segmentation results.
  """
  colormap = np.zeros((_DATASET_MAX_ENTRIES[_ADE], 3), dtype=int)
  
  colormap[0:150,:]=np.array([
      [120,120,120],
      [180,120,120],
      [6,230,230],
      [80,50,50],
      [4,200,3],
      [120,120,80],
      [140,140,140],
      [204,5,255],
      [230,230,230],
      [4,250,7],
      [224,5,255],
      [235,255,7],
      [150,5,61],
      [120,120,70],
      [8,255,51],
      [255,6,82],
      [143,255,140],
      [204,255,4],
      [255,51,7],
      [204,70,3],
      [0,102,200],
      [61,230,250],
      [255,6,51],
      [11,102,255],
      [255,7,71],
      [255,9,224],
      [9,7,230],
      [220,220,220],
      [255,9,92],
      [112,9,255],
      [8,255,214],
      [7,255,224],
      [255,184,6],
      [10,255,71],
      [255,41,10],
      [7,255,255],
      [224,255,8],
      [102,8,255],
      [255,61,6],
      [255,194,7],
      [255,122,8],
      [0,255,20],
      [255,8,41],
      [255,5,153],
      [6,51,255],
      [235,12,255],
      [160,150,20],
      [0,163,255],
      [140,140,140],
      [250,10,15],
      [20,255,0],
      [31,255,0],
      [255,31,0],
      [255,224,0],
      [153,255,0],
      [0,0,255],
      [255,71,0],
      [0,235,255],
      [0,173,255],
      [31,0,255],
      [11,200,200],
      [255,82,0],
      [0,255,245],
      [0,61,255],
      [0,255,112],
      [0,255,133],
      [255,0,0],
      [255,163,0],
      [255,102,0],
      [194,255,0],
      [0,143,255],
      [51,255,0],
      [0,82,255],
      [0,255,41],
      [0,255,173],
      [10,0,255],
      [173,255,0],
      [0,255,153],
      [255,92,0],
      [255,0,255],
      [255,0,245],
      [255,0,102],
      [255,173,0],
      [255,0,20],
      [255,184,184],
      [0,31,255],
      [0,255,61],
      [0,71,255],
      [255,0,204],
      [0,255,194],
      [0,255,82],
      [0,10,255],
      [0,112,255],
      [51,0,255],
      [0,194,255],
      [0,122,255],
      [0,255,163],
      [255,153,0],
      [0,255,10],
      [255,112,0],
      [143,255,0],
      [82,0,255],
      [163,255,0],
      [255,235,0],
      [8,184,170],
      [133,0,255],
      [0,255,92],
      [184,0,255],
      [255,0,31],
      [0,184,255],
      [0,214,255],
      [255,0,112],
      [92,255,0],
      [0,224,255],
      [112,224,255],
      [70,184,160],
      [163,0,255],
      [153,0,255],
      [71,255,0],
      [255,0,163],
      [255,204,0],
      [255,0,143],
      [0,255,235],
      [133,255,0],
      [255,0,235],
      [245,0,255],
      [255,0,122],
      [255,245,0],
      [10,190,212],
      [214,255,0],
      [0,204,255],
      [20,0,255],
      [255,255,0],
      [0,153,255],
      [0,41,255],
      [0,255,204],
      [41,0,255],
      [41,255,0],
      [173,0,255],
      [0,245,255],
      [71,0,255],
      [122,0,255],
      [0,255,184],
      [0,92,255],
      [184,255,0],
      [0,133,255],
      [255,214,0],
      [25,194,194],
      [102,255,0],
      [92,0,255]], dtype='int')
  return colormap


def create_label_colormap(dataset=_PASCAL):
  """Creates a label colormap for the specified dataset.

  Args:
    dataset: The colormap used in the dataset.

  Returns:
    A numpy array of the dataset colormap.

  Raises:
    ValueError: If the dataset is not supported.
  """
  if dataset == _PASCAL:
    return create_pascal_label_colormap()
  elif dataset == _CITYSCAPES:
    return create_cityscapes_label_colormap()
  elif dataset == _ADE:
    return create_ade_label_colormap()
  else:
    raise ValueError('Unsupported dataset.')


def label_to_color_image(label, dataset=_PASCAL):
  """Adds color defined by the dataset colormap to the label.

  Args:
    label: A 2D array with integer type, storing the segmentation label.
    dataset: The colormap used in the dataset.

  Returns:
    result: A 2D array with floating type. The element of the array
      is the color indexed by the corresponding element in the input label
      to the PASCAL color map.

  Raises:
    ValueError: If label is not of rank 2 or its value is larger than color
      map maximum entry.
  """
  if label.ndim != 2:
    raise ValueError('Expect 2-D input label')

  if np.max(label) >= _DATASET_MAX_ENTRIES[dataset]:
    raise ValueError('label value too large.')

  colormap = create_label_colormap(dataset)
  return colormap[label]
