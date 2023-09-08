



# 테스트 환경 : usdview
# Traverse() != TraverseAll() != PrimRange
from pxr import Usd
from path_module import data_02, resource_ldv_00

tar_stage = Usd.Stage.Open(resource_ldv_00)

for x in tar_stage.Traverse():
    print(x)



primIter = iter(Usd.PrimRange.PreAndPostVisit(tar_stage.GetPseudoRoot()))
for x in primIter:
    print(x, primIter.IsPostVisit())




for x in tar_stage.TraverseAll():
    print(x)

