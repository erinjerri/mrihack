vtk_module(vtkIOMySQL
  IMPLEMENTS
    vtkIOSQL
  TEST_DEPENDS
    vtkTestingCore
    vtkTestingIOSQL
  KIT
    vtkIO
  DEPENDS
    vtkIOSQL
  PRIVATE_DEPENDS
    vtkCommonCore
    vtkCommonDataModel
    vtkCommonExecutionModel
    vtksys
  )