vtk_module(vtkIOGDAL
  TEST_DEPENDS
    vtkTestingCore
    vtkRendering${VTK_RENDERING_BACKEND}
    vtkTestingRendering
    vtkInteractionStyle
  KIT
    vtkIO
  DEPENDS
    vtkCommonCore
    vtkCommonExecutionModel
    vtkIOImage
  PRIVATE_DEPENDS
    vtkCommonDataModel
)