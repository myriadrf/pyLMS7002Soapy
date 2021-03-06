# ***************************************************************
# * Name:      Si5351.py
# * Purpose:   Class implementing Si5351 functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************


class Si5351(object):

    def __init__(self, programmingFn):
        """
        Initialize Si5351.
        """
        self.programmingFn = programmingFn

    def uploadLimeSDRConfig(self):
        configData = [(3, 255), (16, 132), (17, 132), (18, 132), (19, 132), (20, 132), (21, 132),
                      (22, 132), (23, 132), (15, 0), (16, 79), (17, 79), (18, 143), (19, 143), (20, 143),
                      (21, 143), (22, 143), (23, 143), (24, 0), (25, 0), (26, 0), (27, 128), (28, 0),
                      (29, 15), (30, 209), (31, 16), (32, 235), (33, 128), (34, 0), (35, 0), (36, 0),
                      (37, 15), (38, 209), (39, 16), (40, 235), (41, 128), (42, 0), (43, 1), (44, 0),
                      (45, 14), (46, 128), (47, 0), (48, 0), (49, 0), (50, 0), (51, 1), (52, 0), (53, 14),
                      (54, 128), (55, 0), (56, 0), (57, 0), (58, 0), (59, 1), (60, 0), (61, 2), (62, 0),
                      (63, 0), (64, 0), (65, 0), (66, 0), (67, 1), (68, 0), (69, 2), (70, 0), (71, 0),
                      (72, 0), (73, 0), (74, 0), (75, 1), (76, 0), (77, 2), (78, 0), (79, 0), (80, 0),
                      (81, 0), (82, 0), (83, 1), (84, 0), (85, 2), (86, 0), (87, 0), (88, 0), (89, 0),
                      (90, 8), (91, 8), (92, 0), (149, 0), (150, 0), (151, 0), (152, 0), (153, 0),
                      (154, 0), (155, 0), (156, 0), (157, 0), (158, 0), (159, 0), (160, 0), (161, 0),
                      (162, 0), (163, 0), (164, 0), (165, 0), (166, 0), (167, 0), (168, 0), (169, 0),
                      (170, 0), (177, 172), (3, 252)]
        self.programmingFn(configData)
