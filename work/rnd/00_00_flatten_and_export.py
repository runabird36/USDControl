


from pxr import Usd


tar_stage = Usd.Stage.Open(...)
tar_stage = Usd.Stage.CreateNew(...)

...

flatten_stage = tar_stage.Flatten()
flatten_stage.Export("/usersetup/pipeline/playground/projects/2023_02_usdPipeline/data/aa.usda")
