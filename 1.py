# Copyright (c) Hin-Tak Leung

# This is the rasterization parameter module, not intended to be called
# as script. Though it works, as below in __main__ .

import clr
import sys
import System
clr.AddReference("OTFontFileVal.dll")

from OTFontFileVal import ValidatorParameters

from System import Array, Single
from System.Collections.Generic import List

class validation_parameters:
    def __init__(self):
        vp = ValidatorParameters()
        ###############################################################
        # below are just the default values and can be deleted as is. #
        ###############################################################
        # SetAllTables() is the default, but an explicit list also works.
        vp.SetAllTables()
        vp.ClearTables()
        vp.tablesToTest = List[str](['BASE', 'CBDT', 'CBLC', 'CFF ', 'cmap', 'COLR',
                                     'CPAL', 'cvt ', 'DSIG', 'EBDT', 'EBLC', 'EBSC',
                                     'fpgm', 'gasp', 'GDEF', 'glyf', 'GPOS', 'GSUB',
                                     'hdmx', 'head', 'hhea', 'hmtx', 'JSTF', 'kern',
                                     'loca', 'LTSH', 'MATH', 'maxp', 'name', 'OS/2',
                                     'PCLT', 'post', 'prep', 'SVG ', 'VDMX', 'vhea',
                                     'vmtx', 'VORG'])
        vp.ClearTables()
        vp.doRastBW = True
        vp.doRastGray = False
        vp.doRastClearType = False
        vp.doRastCTCompWidth = False
        vp.doRastCTVert = False
        vp.doRastCTBGR = False
        vp.doRastCTFractWidth = False
        vp.xRes = 96
        vp.yRes = 96
        vp.xform.stretchX = 1.0
        vp.xform.stretchY = 1.0
        vp.xform.rotation = 0.0
        vp.xform.skew     = 0.0
        # Python does not have single precision, but C# does.
        # casting from int to Single is automatic, Double to Single isn't.
        vp.xform.matrix[0,0] = clr.Convert(1.0, Single)
        vp.xform.matrix[0,1] = 0
        vp.xform.matrix[0,2] = 0
        vp.xform.matrix[1,0] = 0
        vp.xform.matrix[1,1] = 1
        vp.xform.matrix[1,2] = 0
        vp.xform.matrix[2,0] = 0
        vp.xform.matrix[2,1] = 0
        vp.xform.matrix[2,2] = 1
        vp.sizes = List[int]([10])
        ###############################################################
        ################## default values end #########################
        ###############################################################
        self.vp = vp

    def GetValue(self):
        return self.vp

if __name__ == '__main__':
    obj = validation_parameters()
    vp = obj.GetValue()
    # Just to confirm expected type and content:
    print "object type %s, xRes = %d" % ( vp.GetType(), vp.xRes)
    # and tables within
    print "Tables to test:", vp.tablesToTest
