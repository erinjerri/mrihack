vtk_module(vtkRenderingLOD
  GROUPS
    Rendering
  TEST_DEPENDS
    vtkTestingRendering
    vtkRendering${VTK_RENDERING_BACKEND}
    vtkInteractionStyle
  KIT
    vtkRendering
  DEPENDS
    vtkRenderingCore
  PRIVATE_DEPENDS
    vtkCommonCore
    vtkCommonDataModel
    vtkCommonExecutionModel
    vtkCommonMath
    vtkCommonSystem
    vtkFiltersCore
    vtkFiltersModeling
  )