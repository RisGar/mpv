#!/usr/bin/env python3

import vapoursynth as vs

core = vs.core

clip = core.std.BlankClip(video_in)

clip = core.scrawl.Text(clip, "Moozzi2 bad", 5)

clip.set_output()
