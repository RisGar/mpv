#!/usr/bin/env python3

import vapoursynth as vs
from vsutil import depth, get_depth

core = vs.core


def IVTC(clip: vs.VideoNode, TFF: bool) -> vs.VideoNode:
    """"
        Experimental script for inverse telecining and deinterlacing.

        Requires VapourSynth <http://www.vapoursynth.com/doc/about.html>

        Additional dependencies:
            * vs-util <https://github.com/Irrational-Encoding-Wizardry/vsutil>

        :param clip:         Input clip
        :param TFF:          Top-Field-First

        :return:             IVTC'd clip
    """
    down = depth(clip, 8)
    vfm = core.vivtc.VFM(down, TFF)
    return depth(vfm, get_depth(clip))


IVTC(video_in, TFF=True).set_output()
