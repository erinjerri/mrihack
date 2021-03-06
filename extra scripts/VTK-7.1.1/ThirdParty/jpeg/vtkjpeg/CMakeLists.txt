PROJECT(VTKJPEG)

INCLUDE_REGULAR_EXPRESSION("^(jchuff|jconfig|jdct|jdhuff|jerror|jinclude|jmemsys|jmorecfg|jpegint|jpeglib|jversion|jpeg|vtk).*$")

INCLUDE_DIRECTORIES(${VTKJPEG_SOURCE_DIR})

# memmgr back ends: compile only one of these into a working library
# (For now, let's use the mode that requires the image fit into memory.
# This is the recommended mode for Win32 anyway.)
SET(systemdependent_SRCS jmemnobs.c)

# library object files common to compression and decompression
SET(common_SRCS
jcomapi.c jutils.c jerror.c jmemmgr.c
)

# compression library object files
SET(compression_SRCS
jcapimin.c jcapistd.c jctrans.c jcparam.c jdatadst.c jcinit.c
jcmaster.c jcmarker.c jcmainct.c jcprepct.c jccoefct.c jccolor.c
jcsample.c jchuff.c jcphuff.c jcdctmgr.c jfdctfst.c jfdctflt.c
jfdctint.c
)

# decompression library object files
SET(decompression_SRCS
jdapimin.c jdapistd.c jdtrans.c jdatasrc.c jdmaster.c
jdinput.c jdmarker.c jdhuff.c jdphuff.c jdmainct.c jdcoefct.c
jdpostct.c jddctmgr.c jidctfst.c jidctflt.c jidctint.c jidctred.c
jdsample.c jdcolor.c jquant1.c jquant2.c jdmerge.c
)


IF (WIN32)
  IF (BUILD_SHARED_LIBS)
    ADD_DEFINITIONS(-DJPEGDLL)
  ELSE ()
    SET(JPEGSTATIC 1)
  ENDIF ()
ENDIF ()


CONFIGURE_FILE(${VTKJPEG_SOURCE_DIR}/jpegDllConfig.h.in
               ${VTKJPEG_BINARY_DIR}/jpegDllConfig.h)

VTK_ADD_LIBRARY(vtkjpeg ${systemdependent_SRCS} ${common_SRCS} ${compression_SRCS} ${decompression_SRCS})

IF(NOT VTK_INSTALL_NO_DEVELOPMENT)
  INSTALL(FILES
    ${VTKJPEG_BINARY_DIR}/jpegDllConfig.h
    ${VTKJPEG_SOURCE_DIR}/jpeglib.h
    ${VTKJPEG_SOURCE_DIR}/vtk_jpeg_mangle.h
    ${VTKJPEG_SOURCE_DIR}/jconfig.h
    ${VTKJPEG_SOURCE_DIR}/jmorecfg.h
    ${VTKJPEG_SOURCE_DIR}/jerror.h
    DESTINATION ${VTK_INSTALL_INCLUDE_DIR}/vtkjpeg
    COMPONENT Development)
ENDIF()
