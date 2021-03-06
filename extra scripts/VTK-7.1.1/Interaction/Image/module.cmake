vtk_module(vtkInteractionImage
  GROUPS
    Imaging
    Rendering
  KIT
    vtkInteraction
  DEPENDS
    vtkCommonCore
    vtkRenderingCore
  PRIVATE_DEPENDS
    vtkCommonDataModel
    vtkCommonExecutionModel
    vtkImagingColor
    vtkImagingCore
    vtkInteractionStyle
    vtkInteractionWidgets
  )