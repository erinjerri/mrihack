vtk_module(vtkCommonComputationalGeometry
  GROUPS
    StandAlone
  TEST_DEPENDS
    vtkTestingCore
    vtkRendering${VTK_RENDERING_BACKEND}
  KIT
    vtkCommon
  DEPENDS
    vtkCommonCore
    vtkCommonDataModel
  )