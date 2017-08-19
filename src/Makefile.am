AUTOMAKE_OPTIONS = subdir-objects


GIT_REVISION = $(shell git describe --abbrev=6 --dirty --always --tags)

# UNAME := $(shell uname)
# ifeq ($(UNAME), Darwin)
#  LIBS += -lfst -lm -ldl 
#  CXX += -std=c++0x -Wall -Wno-sign-compare -Wno-unused-local-typedefs
# endif

# ifeq ($(UNAME), Linux)
# LIBS=-lfst -ldl -lm -lrt -fopenmp
# CXXFLAGS = -std=c++0x -Wall -Wno-sign-compare -Wno-unused-local-typedefs
# endif

bin_SCRIPTS =                      \
	bin/phonetisaurus-apply    \
	bin/phonetisaurus-train

bin_PROGRAMS =                     \
	phonetisaurus-align	   \
	phonetisaurus-arpa2wfst	   \
	phonetisaurus-g2pfst       \
	phonetisaurus-g2prnn       \
	rnnlm

AM_CPPFLAGS = -I$(top_srcdir) -DGIT_REVISION=\"$(GIT_REVISION)\" -std=c++0x -Wall -Wno-sign-compare -Wno-unused-local-typedefs

phonetisaurus_align_SOURCES = bin/phonetisaurus-align.cc include/PhonetisaurusRex.h lib/util.cc include/util.h lib/LatticePruner.cc include/LatticePruner.h lib/M2MFstAligner.cc include/M2MFstAligner.h
phonetisaurus_align_CXXFLAGS = $(OPENFST_CXXFLAGS)
phonetisaurus_align_LDADD = $(OPENFST_LDFLAGS)

phonetisaurus_arpa2wfst_SOURCES = bin/phonetisaurus-arpa2wfst.cc include/ARPA2WFST.h lib/util.cc include/util.h
phonetisaurus_arpa2wfst_CXXFLAGS = $(OPENFST_CXXFLAGS)
phonetisaurus_arpa2wfst_LDADD = $(OPENFST_LDFLAGS)

phonetisaurus_g2pfst_SOURCES = bin/phonetisaurus-g2pfst.cc include/PhonetisaurusScript.h include/PhonetisaurusRex.h lib/util.cc include/util.h
phonetisaurus_g2pfst_CXXFLAGS = $(OPENFST_CXXFLAGS) -I$(top_srcdir)/3rdparty/utfcpp -funroll-loops -ffast-math
phonetisaurus_g2pfst_LDADD = $(OPENFST_LDFLAGS)

phonetisaurus_g2prnn_SOURCES = bin/phonetisaurus-g2prnn.cc include/LegacyRnnLMHash.h include/LegacyRnnLMDecodable.h include/LegacyRnnLMReader.h include/RnnLMDecoder.h lib/util.cc include/util.h 3rdparty/rnnlm/rnnlmlib.cpp 3rdparty/rnnlm/rnnlmlib.h
phonetisaurus_g2prnn_CXXFLAGS = $(OPENFST_CXXFLAGS) -I$(top_srcdir)/3rdparty/rnnlm -funroll-loops -ffast-math
phonetisaurus_g2prnn_LDADD = $(OPENFST_LDFLAGS)
if OPENMP
  phonetisaurus_g2prnn_CXXFLAGS += $(OPENMP_CXXFLAGS)
  phonetisaurus_g2prnn_LDADD += $(OPENMP_LDFLAGS)
endif

rnnlm_SOURCES = bin/rnnlm.cc 3rdparty/rnnlm/rnnlmlib.cpp 3rdparty/rnnlm/rnnlmlib.h
rnnlm_CXXFLAGS = $(OPENFST_CXXFLAGS) -I$(top_srcdir)/3rdparty/rnnlm -funroll-loops -ffast-math
rnnlm_LDADD = $(OPENFST_LDFLAGS)
