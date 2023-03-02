import os
import numpy as np
from PIL import Image


# 6.4 זכרו זכרו

def decode_img(path=None):
    if not path:
        path = os.path.join(os.getcwd(), 'resource', 'code.png')

    np_img_trans = np.array(Image.open(path)).transpose()

    ans = []
    for row in np_img_trans:
        if 1 in row:
            ans.append(chr(np.where(row == 1)[0][0]))

    return ''.join(ans)

    # 'Place gunpowder beneath the House of Lords. 11/05/1605'

