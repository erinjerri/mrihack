vtk_module(vtkCommonCore
  GROUPS
    StandAlone
  TEST_DEPENDS
    vtkTestingCore
    vtkCommonSystem
    vtkCommonTransforms
    vtksys
  KIT
    vtkCommon
  DEPENDS
    vtkkwiml
  PRIVATE_DEPENDS
    vtksys
  )