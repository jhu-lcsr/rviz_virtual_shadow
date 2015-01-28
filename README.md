RViz Virtual Shadow
===================

This package simply clones an URDF with all `<visual>` elements set to appear
as flat black in RViz. This can be useful when visualizing augmented scenes in
teleoperation.

See [make_shadow_urdf.launch](example/make_shadow_urdf.launch) for example
usage.

When viewing in RViz, create a `RobotModel` display and set it to
`<<MODEL_PARAM>>_shadow` where `<<MODEL_PARAM>>` is the parameter where your
urdf is stored. Then use that display in conjunction with an RViz `Camera`
display which is set to `Backround + Overlay` compositing.
