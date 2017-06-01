if(BUILD_SHARED_LIBS)
  set(HDF5_USE_STATIC_LIBS FALSE)
else()
  set(HDF5_USE_STATIC_LIBS ON)
endif()
if(VTK_USE_SYSTEM_HDF5)
  set(vtkhdf5_LIBRARIES ${HDF5_LIBRARIES} ${HDF5_HL_LIBRARIES})
endif()
vtk_module(vtkhdf5
  EXCLUDE_FROM_WRAPPING
  DEPENDS
    vtkzlib
  )