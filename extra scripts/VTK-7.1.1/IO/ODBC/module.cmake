vtk_module(vtkIOODBC
  TEST_DEPENDS
    vtkTestingCore
  KIT
    vtkIO
  DEPENDS
    vtkIOSQL
  PRIVATE_DEPENDS
    vtkCommonCore
    vtksys
  )