vtk_module(vtkRenderingQt
  GROUPS
    Qt
  TEST_DEPENDS
    vtkTestingCore
  DEPENDS
    vtkCommonCore
    vtkCommonExecutionModel
    vtkRenderingCore
    vtkRenderingLabel
  PRIVATE_DEPENDS
    vtkCommonDataModel
    vtkCommonSystem
    vtkFiltersSources
    vtkFiltersTexture
    vtkGUISupportQt
  )