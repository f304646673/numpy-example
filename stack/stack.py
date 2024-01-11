import numpy as np
from PIL import Image

correlateImg = Image.open('correlate.png')
correlateData = np.array(correlateImg)

gaussianLaplaceImg = Image.open('gaussianlaplace.png')
gaussianLaplaceData = np.array(gaussianLaplaceImg)

morphoLogicalLaplaceImg = Image.open('morphologicallaplace.png')
morphoLogicalLaplaceData = np.array(morphoLogicalLaplaceImg)

whiteTophatImg = Image.open('whitetophat.png')
whiteTophatData = np.array(whiteTophatImg)

top = np.hstack((correlateData, gaussianLaplaceData))
bottom = np.hstack((morphoLogicalLaplaceData, whiteTophatData))

full = np.vstack((top, bottom))

fullImg = Image.fromarray(full)
fullImg.save('full.png')